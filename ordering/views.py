from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.http import JsonResponse

from django.conf import settings
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import (login as auth_login, logout as auth_logout, authenticate)
from django.contrib import messages

from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View
)
from django.forms import ModelForm
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Order, Inventory, OrderHistory
from .forms import RegistrationForm, EditProfileForm, OrderForm, InventoryForm

# third party apps
from fm.views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class DetailView(ListView):
    model = Order  # shorthand for setting queryset = models.Order.objects.all()
    template_name = 'ordering/detail.html'
    context_object_name = "all_order"
    ordering = ['-date']
    paginate_by = 10


class OrderList(ListView):
    model = Order


class OrderCreateView(SuccessMessageMixin, AjaxCreateView):
    form_class = OrderForm
    success_message = "Successfully added an order."

    class Meta:
        model = Order
        fields = (
            'shipment_provider',
            'last_name',
            'first_name',
            'middle_name',
            'address',
            'barangay',
            'city_and_municipality',
            'zip_code',
            'province',
            'phone',
            'quantity',
            'order',
            'status',
            'special_instructions',
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(OrderForm[user]).__init__(*args, **kwargs)
        if not user.is_superuser:
            del self.fields['status']


class OrderUpdateView(SuccessMessageMixin, AjaxUpdateView):
    form_class = OrderForm
    model = Order
    success_message = "Successfully updated this order."
    pk_url_kwarg = 'order_id'


class OrderDeleteView(AjaxDeleteView):
    model = Order
    pk_url_kwarg = 'order_id'


class OrderSuccess(TemplateView):
    template_name = 'ordering/order_success.html'


class InventoryMenu(ListView):
    model = Inventory
    template_name = 'inventory/inventory_sample.html'
    context_object_name = "all_inventorys"
    paginate_by = 10


# FM app views
class InventoryCreateView(SuccessMessageMixin, AjaxCreateView):
    form_class = InventoryForm
    success_message = "Successfully added an item to the inventory"


class InventoryDeleteView(AjaxDeleteView):
    model = Inventory
    pk_url_kwarg = 'inventory_id'


class InventoryUpdateView(SuccessMessageMixin, AjaxUpdateView):
    form_class = InventoryForm
    model = Inventory
    success_message = "Successfully updated this product."
    pk_url_kwarg = 'inventory_id'
# FM app views ends here


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


def inventory_detail(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    context = {
        "inventory": inventory,
        }
    return render(request, "inventory/inventory_detail.html", context)


def home(request):
    return render(request, 'ordering/index.html')


def register(request):
    if request.method == 'POST':
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
