from django import forms
from django.db.models import fields

from user.models import Address, Profile


class AddAdddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=('first_name','last_name','phone','email','address1','address2','country','state','city','pincode','add_type')

    def __init__(self, *args, **kwargs):
        super(AddAdddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name','last_name','phone','email','gender','profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'