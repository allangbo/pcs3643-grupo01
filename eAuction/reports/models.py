from django.db import models
from django.http.response import FileResponse
from django.urls import reverse
from reportlab.pdfgen import canvas   
import io

class Report(models.Model):
    type = models.BooleanField("Relatório de faturamento?", default=False)
    start_date = models.DateTimeField("Data de início")
    end_date = models.DateTimeField("Data de fim")

    def __str__(self):
        return str(self.type)

    def generateFile(self):
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)

        if self.type:
            filename = "relatório_de_faturamento.pdf"
            p.drawString(20, 750, "Relatório de faturamento em relação ao período: " + self.start_date.strftime("%d/%m/%Y, %H:%M:%S") + " a " + self.end_date.strftime("%d/%m/%Y, %H:%M:%S"))
        else:
            filename = "relatório_de_desempenho.pdf"
            p.drawString(20, 750, "Relatório de desempenho em relação ao período: " + self.start_date.strftime("%d/%m/%Y, %H:%M:%S") + " a " + self.end_date.strftime("%d/%m/%Y, %H:%M:%S"))

        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=filename)