from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import (login as auth_login, logout as auth_logout, authenticate)
from django.contrib import messages

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.forms import ModelForm
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Order, Inventory, OrderHistory
from .forms import RegistrationForm, EditProfileForm, OrderForm, InventoryForm


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class DetailView(ListView):
    model = Order  # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'ordering/detail.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    context_object_name = "all_order"  # default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 10  # and that's it !!


class OrderList(ListView):
    model = Order


class OrderCreate(SuccessMessageMixin, CreateView):
    model = Order
    success_url = reverse_lazy('ordering:order_create')
    success_message = "You successfully ordered to the system!"
    fields = ['shipment_provider', 'last_name', 'first_name', 'middle_name',
              'address', 'barangay', 'city_and_municipality', 'zip_code',
              'province', 'phone', 'quantity',
              'order', 'special_instructions']


class OrderSuccess(TemplateView):
    template_name = 'ordering/order_success.html'


class InventoryCreate(CreateView):
    model = Inventory
    success_url = reverse_lazy('ordering:inventory_menu')
    fields = ['date', 'product_logo', 'product', 'stock_in', 'stock_out', 'balance', 'particulars']


class InventoryDelete(DeleteView):
    model = Inventory
    success_url = reverse_lazy('ordering:inventory_menu')
    pk_url_kwarg = 'inventory_id'

    def get(self, request):
        messages.success(request, 'Successfully deleted this item.')


class LoginView(View):
    template_name = 'ordering/login_user.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            _username = request.POST['username']
            _password = request.POST['password']
            user = authenticate(username=_username, password=_password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect(reverse_lazy('ordering:home'))
                else:
                    messages.warning(request, 'Your account is not activated.')
            else:
                messages.error(request, 'Username or password are invalid.')
        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        auth_logout(request)
        messages.success(request, 'Your account has been logout successfully.')
        return redirect(reverse_lazy('ordering:login'))

def order_update(request, pk, template_name='ordering/form-template.html'):
    server = get_object_or_404(pk=pk)
    form = OrderForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})


def order_delete(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect(reverse_lazy('ordering:detail'))


class OrderHistoryForm(ModelForm):
    class Meta:
        model = OrderHistory
        fields = ['user', 'order']


def order_history(request, order_id):
    all_history = OrderHistory.objects.get(OrderHistory, pk=order_id)
    return render(request, 'ordering/ordering_history.html', {'all_history': all_history})


def order_success(request):
    return render(request, 'ordering/order_success.html')


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['date', 'product_logo', 'product', 'stock_in', 'stock_out', 'balance', 'particulars']


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


def inventory_delete(inventory_id):
    inventory = Inventory.objects.get(pk=inventory_id)
    inventory.delete()
    return redirect(reverse_lazy('ordering:inventory_menu'))


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
            return redirect(reverse_lazy('ordering:view_profile'))
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
            return redirect(reverse_lazy('ordering:view_profile'))
        else:
            return redirect(reverse_lazy('ordering:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'ordering/change_password.html', args)
