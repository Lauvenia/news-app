from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, SelectPublisher


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            role = form.cleaned_data.pop("role")

            group_name = role.capitalize()
            group, _ = Group.objects.get_or_create(name=group_name)

            user.groups.add(group)
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def select_publisher(request):
    if request.method == "POST":
        user = request.user
        form = SelectPublisher(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SelectPublisher()

    context = {"form": form}
    return render(request, "accounts/select_publisher.html", context)
