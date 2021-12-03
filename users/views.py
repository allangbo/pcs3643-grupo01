from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import UserForm
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
from theme.templatetags.auth_extras import group_required
from django.contrib.auth.decorators import login_required

class CreateUser(CreateView):
    template_name = 'users/register_form.html'
    form_class = UserForm
    def get_success_url(self):
        return reverse('auth:login')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save(commit=False)
        user.save()
        user_group, created = Group.objects.get_or_create(name='seller-buyer')
        user.groups.add(user_group)
        return super().form_valid(form)


@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auctioneer_list(request):
    group = Group.objects.get(name="auctioneer")
    auctioneer_list = group.user_set.all()
    return render(request, 'users/auctioneer_list.html', {'auctioneer_list': auctioneer_list})

@login_required(login_url='/auth/login/')
@group_required('admin')
def auctioneer_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        user_group, created = Group.objects.get_or_create(name='auctioneer')
        user.groups.add(user_group)
        return redirect('auth:auctioneer_list')
    return render(request, 'users/register_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin')
def auctioneer_deactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect("auth:auctioneer_list")

@login_required(login_url='/auth/login/')
@group_required('admin')
def auctioneer_activate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect("auth:auctioneer_list")

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def seller_buyer_list(request):
    group = Group.objects.get(name="seller-buyer")
    seller_buyer_list = group.user_set.all()
    return render(request, 'users/seller_buyer_list.html', {'seller_buyer_list': seller_buyer_list})

@login_required(login_url='/auth/login/')
@group_required('admin')
def seller_buyer_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        user_group, created = Group.objects.get_or_create(name='seller-buyer')
        user.groups.add(user_group)
        return redirect('auth:seller_buyer_list')
    return render(request, 'users/register_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin')
def seller_buyer_deactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect("auth:seller_buyer_list")

@login_required(login_url='/auth/login/')
@group_required('admin')
def seller_buyer_activate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect("auth:seller_buyer_list")

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def manager_list(request):
    group = Group.objects.get(name="admin")
    manager_list = group.user_set.all()
    return render(request, 'users/manager_list.html', {'manager_list': manager_list})

@login_required(login_url='/auth/login/')
@group_required('admin')
def manager_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        user_group, created = Group.objects.get_or_create(name='admin')
        user.groups.add(user_group)
        return redirect('auth:manager_list')
    return render(request, 'users/register_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin')
def manager_deactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect("auth:manager_list")

@login_required(login_url='/auth/login/')
@group_required('admin')
def manager_activate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect("auth:manager_list")