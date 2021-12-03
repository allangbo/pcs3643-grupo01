from django.db import models
from django.http.response import FileResponse
from django.urls import reverse
from reportlab.lib import colors
from reportlab.pdfgen import canvas   
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from django.db.models import Q
import io

from auctions.models import Auction, Bid

class Report(models.Model):
    class ReportType(models.TextChoices):
        FATURAMENTO = 'Faturamento'
        DESEMPENHO = 'Desempenho'

    type = models.CharField("Tipo de relatório",
        max_length=11,
        choices=ReportType.choices,
        default=ReportType.FATURAMENTO,
    )
    start_date = models.DateTimeField("Data de início")
    end_date = models.DateTimeField("Data de fim")

    def __str__(self):
        return str(self.type)

    def generateFile(self):
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        date_time_format = "%d/%m/%Y, %H:%M:%S"
        auctions_in_interval = Auction.objects.filter(
                Q(end_date__gt=self.start_date) & Q(end_date__lt=self.end_date)
                )
        finished_auctions = auctions_in_interval.filter(Q(state__exact=Auction.StateType.FINISHED))
        invalid_auctions = auctions_in_interval.filter(Q(state__exact=Auction.StateType.INVALID))
        canceled_auctions = auctions_in_interval.filter(Q(state__exact=Auction.StateType.CANCELED))

        bids_in_interval = list(filter(lambda x: x.auction in list(auctions_in_interval), Bid.objects.all()))

        if self.type == 'Faturamento':
            filename = "relatório_de_faturamento.pdf"
            p.translate(0.7*inch,9*inch)
            p.rect(0,-8.5*inch,7*inch,10.7*inch, fill=0)

            title = p.beginText()
            title.setFont('Helvetica-Bold', 16)
            title.setCharSpace(2)
            title.setTextOrigin(2*inch, inch)
            title.textLine("Relatório de faturamento")
            p.drawText(title)

            subtitle = p.beginText()
            subtitle.setFont('Helvetica', 13)
            subtitle.setCharSpace(1)
            subtitle.setTextOrigin(1*inch, 0)
            subtitle.textLines("Período: \n " + self.start_date.strftime(date_time_format) + " - " + self.end_date.strftime(date_time_format))
            p.drawText(subtitle)

            # total_profit = sum(auctions_in_interval.values_list('profit', flat=True))
            total_profit_sellers = 0
            total_profit_buyers = 0
            for i in list(auctions_in_interval):
                if i.register_fee_paid:
                    total_profit_sellers += i.register_fee
                if i.buy_fee_paid and i.state == Auction.StateType.FINISHED:
                    total_profit_buyers += i.buy_fee

            profit = p.beginText()
            profit.setFont('Helvetica', 12)
            profit.setCharSpace(1)
            profit.setTextOrigin(0.3*inch, -1.5*inch)
            profit.textLines("O lucro total provieniente de taxas pagas por vendedores foi R$ " + "{:.2f}".format(total_profit_sellers) + "\n O lucro total provieniente de taxas pagas por compradores foi R$ " + "{:.2f}".format(total_profit_buyers))
            p.drawText(profit)
            # data = [['00', '01', '02', '03', '04'],
            # ['10', '11', '12', '13', '14'],
            # ['20', '21', '22', '23', '24'],
            # ['30', '31', '32', '33', '34']]
            # table = Table(data, 5*[0.4*inch], 4*[0.4*inch])
            # table.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
            # ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
            # ('VALIGN',(0,0),(0,-1),'TOP'),
            # ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
            # ('ALIGN',(0,-1),(-1,-1),'CENTER'),
            # ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
            # ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
            # ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            # ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            # ]))
            # table.wrap(3*inch, 3*inch)
            # table.drawOn(p, -inch, 0)
            

        else:
            filename = "relatório_de_desempenho.pdf"
            p.translate(0.7*inch,9*inch)
            p.rect(0,-8.5*inch,7*inch,10.7*inch, fill=0)

            title = p.beginText()
            title.setFont('Helvetica-Bold', 16)
            title.setCharSpace(2)
            title.setTextOrigin(2*inch, inch)
            title.textLine("Relatório de desempenho")
            p.drawText(title)

            subtitle = p.beginText()
            subtitle.setFont('Helvetica', 13)
            subtitle.setCharSpace(1)
            subtitle.setTextOrigin(1*inch, 0)
            subtitle.textLines("Período: \n " + self.start_date.strftime(date_time_format) + " - " + self.end_date.strftime(date_time_format))
            p.drawText(subtitle)

            auctions_quantity = len(list(finished_auctions))
            invalid_auctions_quantity = len(list(invalid_auctions))
            canceled_auctions_quantity = len(list(canceled_auctions))
            buyers = []
            auctioneers = []
            for bid in list(bids_in_interval):
                buyer = bid.buyer
                auctioneer = bid.auction.auctioneer
                if not buyer in buyers:
                    buyers.append(buyer)
                if not auctioneer in auctioneers:
                    auctioneers.append(auctioneer)

            performance = p.beginText()
            performance.setFont('Helvetica', 13)
            performance.setTextOrigin(0.3*inch, -1.5*inch)
            performance.setCharSpace(1)
            performance.textLines("Leilões arrematados: " + "{:.0f}".format(auctions_quantity) + "\nCompradores diferentes que deram lance: " + str(len(buyers)) + "\nVendedores que anunciaram lotes: " + str(len(auctioneers)) + "\nLeilões que finalizaram sem lance acima do valor de reserva: " +  str(invalid_auctions_quantity) + "\nLeilões cancelados: " + str(canceled_auctions_quantity))
            p.drawText(performance)

        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=filename)