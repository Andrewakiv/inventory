from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegistrationForm


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("inventory:materials")
    form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})
