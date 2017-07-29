from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'forms-control',
            'placeholder': 'Username'
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
    date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'forms-control',
            'placeholder': 'Date'
        }
    ))

    class Meta:
        model = Order
        fields = (
            'date',
            'name_of_recipient',
            'address',
            'barangay',
            'city',
            'province',
            'phone',
            'quantity',
            'order',
            'special_instructions'
        )

        def save(self, commit=True):
            order = super(OrderForm, self).save(commit=False)
            order.date = self.cleaned_data['date']
            order.name_of_recipient = self.cleaned_data['name_of_recipient']
            order.address = self.cleaned_data['address']
            order.barangay = self.cleaned_data['barangay']
            order.city = self.cleaned_data['city']
            order.province = self.cleaned_data['province']
            order.phone = self.cleaned_data['phone']
            order.quantity = self.cleaned_data['quantity']
            order.order = self.cleaned_data['order']
            order.special_instructions = self.cleaned_data['special_instructions']

            if commit:
                order.save()

            return order
