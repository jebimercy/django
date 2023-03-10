from django import forms


class UserReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()


class MembersReg(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)


class StudentReg(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    school = forms.CharField(max_length=100)