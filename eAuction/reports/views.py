from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from django.utils import timezone
from .models import Report
from theme.templatetags.auth_extras import group_required
from django.contrib.auth.decorators import login_required

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['type', 'start_date', 'end_date']

    def clean(self):
        now = timezone.now()
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date >= end_date:
            raise ValidationError(
                'A data de fim deve ser depois da data de início',
            )
        if start_date > now:
            raise ValidationError(
                'A data e horário de início não devem ser depois de agora',
            )
        if end_date > now:
            raise ValidationError(
                'A data e horário de fim não devem ser depois de agora',
            )
        return self.cleaned_data

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def create_report(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        fs = form.save(commit=False)
        return fs.generateFile()
    return render(request, 'reports/report_form.html', {'form': form})