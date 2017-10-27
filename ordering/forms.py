from django import forms
from django.contrib.auth.models import User
from .models import Order, OrderHistory, Inventory
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
            'class': 'form-control',
        }
    ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    middle_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Order
        fields = (
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
            'special_instructions'
        )


class OrderHistoryForm(forms.ModelForm):

    class Meta:
        model = OrderHistory
        fields = (
            'shipment_provider',
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


class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = (
            'product',
            'stock_in',
            'stock_out',
            'balance',
            'particulars'
        )
