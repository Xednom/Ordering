from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.forms import(
    UserChangeForm,
    PasswordChangeForm
)
from django.http import Http404, HttpResponse
from ordering.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import (login as auth_login, authenticate)
from django.forms import ModelForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from .models import Order, Inventory
from .forms import OrderForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['shipment_provider', 'last_name', 'first_name', 'middle_name', 'address', 'barangay', 'city_and_municipality', 'zip_code', 'province', 'phone', 'quantity', 'order', 'special_instructions']

def detail(request):
    all_order = Order.objects.all()
    return render(request, 'ordering/detail.html', {'all_order': all_order})

def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ordering:order_success')
    return render(request, 'ordering/dropship_form.html', {'form':form})

def order_update(request, pk, template_name='ordering/form-template.html'):
    server = get_object_or_404(Server, pk=pk)
    form = OrderForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

def order_delete(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect(reverse('ordering:detail'))

def order_history(request, order_id):
    order_history = Order.objects.get(Order, pk=order_id)
    return render(request, 'ordering/ordering_history.html', {'order_history': order_history})

def order_success(request):
    return render(request, 'ordering/order_success.html')

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['date', 'product_logo', 'product_name', 'stock_in', 'stock_out', 'balance', 'particulars']

def inventory_menu(request):
    all_inventorys = Inventory.objects.all()
    return render(request, 'ordering/inventory_sample.html', {'all_inventorys': all_inventorys})

def inventory_detail(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    context = {
    "inventory": inventory,
    }
    return render(request, "ordering/inventory_detail.html", context)

def inventory_create(request):
    form = InventoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        inventory = form.save(commit=False)
        inventory.product_logo = request.FILES['product_logo']
        file_type = inventory.product_logo.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'inventory': inventory,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
        inventory.save()
        return redirect(reverse('ordering:inventory_menu'))
    context = {
        "form": form,
    }
    return render(request, 'ordering/inventory_form.html', context)

def inventory_delete(request, inventory_id):
    inventory = Inventory.objects.get(pk=inventory_id)
    inventory.delete()
    return redirect(reverse('ordering:inventory_menu'))

def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('ordering:register'))
            else:
                _message = 'Your account is not activated'
        else:
            return render(request, 'ordering/register.html')
    context = {'message': _message}
    return render(request, 'ordering/register.html', context)

def home(request):
    return render(request, 'ordering/index.html')

def inventory(request):
    return render(request, 'ordering/inventory.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ordering/register_success.html')
        else:
            return render(request, 'ordering/register.html', {'form': form})
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'ordering/register.html', args)

def register_success(request):
    return render(request, 'ordering:register_success')


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'ordering/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('ordering:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'ordering/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('ordering:view_profile'))
        else:
            return redirect(reverse('ordering:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)
        args={'form': form}
        return render(request, 'ordering/change_password.html', args)
