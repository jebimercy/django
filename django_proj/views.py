from django.shortcuts import render
from .forms import MembersReg
from .forms import StudentReg
from .forms import UserReg


def reg(request):
    submit_button = request.POST.get("mercy")
    name = ''
    email = ''
    password = ''

    reg_form = UserReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context = {'reg_form': reg_form,
               'name': name,
               'email': email,
               'password': password,
               'submit_button': submit_button

               }

    return render(request, 'register.html', context)


def reg(request):
    submit_button = request.POST.get("student")
    name = ''
    age = ''
    email = ''
    school = ''

    reg_form = StudentReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        age = reg_form.cleaned_data.get("age")
        email = reg_form.cleaned_data.get("email")
        school = reg_form.cleaned_data.get("school")
    context = {'reg_form': reg_form,
               'name': name,
               'age': age,
               'email': email,
               'school': school,
               'submit_button': submit_button

               }

    return render(request, 'students.html', context)


def reg(request):
    submit_button = request.POST.get("student")
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''

    reg_form = MembersReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        age = reg_form.cleaned_data.get("age")
        phone = reg_form.cleaned_data.get("phone")
        city = reg_form.cleaned_data.get("city")
        country = reg_form.cleaned_data.get("country")
    context = {'reg_form': reg_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'country': country,
               'submit_button': submit_button

               }

    return render(request, 'member.html', context)














