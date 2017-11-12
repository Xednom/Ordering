from django import forms
from django.contrib.auth.models import User
from .models import Order, Inventory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        }
    ))

    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First name',
        }
    ))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
        }
    ))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }
    ))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
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
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'.capitalize(),
            'autocomplete': 'off',
        }
    ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control capitalize',
            'autocomplete': 'off',
        }
    ))
    middle_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control capitalize',
            'autocomplete': 'off',
        }
    ))
    address = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    barangay = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    city_and_municipality = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    zip_code = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'size': '4',
        }
    ))
    province = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'size':'13',
        }
    ))
    quantity = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    special_instructions = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))

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
            'special_instructions',
        )


class OrderEditForm(forms.ModelForm):
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    middle_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    barangay = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    city_and_municipality = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    province = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    quantity = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    order = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    status = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
    special_instructions = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))


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


class InventoryForm(forms.ModelForm):
    stock_in = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
        }
    ))
    stock_out = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
        }
    ))
    balance = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
        }
    ))
    particulars = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Inventory
        fields = (
            # 'product_logo',
            'product',
            'stock_in',
            'stock_out',
            'balance',
            'particulars'
        )
