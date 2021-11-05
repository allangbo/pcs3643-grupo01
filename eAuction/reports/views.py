from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from .models import Report
from theme.templatetags.auth_extras import group_required
from django.contrib.auth.decorators import login_required

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['type', 'start_date', 'end_date']

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def create_report(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        fs = form.save(commit=False)
        return fs.generateFile()
    return render(request, 'reports/report_form.html', {'form': form})