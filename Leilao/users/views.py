from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'cpf', 'email', 'user_type', 'password']

def user_list(request, template_name='users/user_list.html'):
    user = User.objects.all()
    data = {}
    data['object_list'] = user
    return render(request, template_name, data)

def user_create(request, template_name='users/user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:user_list')
    return render(request, template_name, {'form':form})

def user_update(request, pk, template_name='users/user_form.html'):
    user= get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('users:user_list')
    return render(request, template_name, {'form':form})

def user_delete(request, pk, template_name='users/user_confirm_delete.html'):
    user= get_object_or_404(User, pk=pk)    
    if request.method=='POST':
        user.delete()
        return redirect('users:user_list')
    return render(request, template_name, {'object':user})