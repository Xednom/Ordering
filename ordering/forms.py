from django import forms
from django.contrib.auth.models import User
from ordering.models import Order, Inventory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        }
    ))

    first_name = forms.CharField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First name',
        }
    ))

    last_name = forms.CharField(required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
        }
    ))

    password1 = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }
    ))

    password2 = forms.CharField(required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class OrderForm(forms.ModelForm):
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'last name',
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'first_name',
        }
    ))
    middle_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'middle_name',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Address',
        }
    ))

    class Meta:
        model = Order
        fields = (
            'date',
            'last_name',
            'first_name',
            'middle_name',
            'address',
            'barangay',
            'city_and_municipality',
            'province',
            'phone',
            'quantity',
            'order',
            'special_instructions'
        )

        def save(self, commit=True):
            order = super(OrderForm, self).save(commit=False)
            order.date = self.cleaned_data['date']
            order.name_of_recipient = self.cleaned_data['last_name']
            order.name_of_recipient = self.cleaned_data['first_name']
            order.name_of_recipient = self.cleaned_data['middle_name']
            order.address = self.cleaned_data['address']
            order.barangay = self.cleaned_data['barangay']
            order.city = self.cleaned_data['city_and_municipality']
            order.province = self.cleaned_data['province']
            order.phone = self.cleaned_data['phone']
            order.quantity = self.cleaned_data['quantity']
            order.order = self.cleaned_data['order']
            order.special_instructions = self.cleaned_data['special_instructions']

            if commit:
                order.save()

            return order


class InventoryForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Product name',
        }
    ))

    class Meta:
        model = Inventory
        fields = (
            'date',
            'product_name',
            'stock_in',
            'stock_out',
            'balance',
            'particulars'

        )
