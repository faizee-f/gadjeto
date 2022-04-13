from django import forms
from django.contrib.messages.api import error
from django.db.models import fields

from user.models import Address, Profile


class AddAdddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "address1",
            "address2",
            "country",
            "state",
            "city",
            "pincode",
            "add_type",
        )

    def __init__(self, *args, **kwargs):
        super(AddAdddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,
        error_messages={"invalid": ("Images Only")},
        widget=forms.FileInput,
    )

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "profile_picture")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
