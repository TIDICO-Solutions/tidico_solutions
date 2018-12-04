from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from itertools import chain

from . import forms
from e_reg.models import UserManager,User,GuestUser,HotelMembership,HotelProperty


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("welcome")
    template_name = "e_reg/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("welcome")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = forms.GuestUserCreateForm
    success_url = reverse_lazy("e_reg:login")
    template_name = "e_reg/signup.html"


@login_required
def my_profile(request):
    guestuser = request.user
    hotelmembership = guestuser.guestuser.membership.all
    return render(request, "e_reg/my_profile.html", {"hotelmembership": hotelmembership})


@login_required
def select_property(request):
    hotelproperties = HotelProperty.objects.order_by("name")
    return render(request, "e_reg/select_property.html", {"hotelproperty": hotelproperties})


@login_required
def contact_update(request):
    guestuser = request.user
    form = forms.GuestUserUpdateForm(instance=guestuser)

    if request.method == "POST":
        form = forms.GuestUserUpdateForm(instance=guestuser, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully updated your Contact Card")
            return HttpResponseRedirect(guestuser.get_absolute_url())
    return render(request, "e_reg/contact_update.html", {'form': form})


@login_required
def room_preference_update(request):
    guestuser = request.user
    form = forms.RoomPreferenceUpdateForm(instance=guestuser)

    if request.method == "POST":
        form = forms.RoomPreferenceUpdateForm(instance=guestuser, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully updated your Room Preferences")
            return HttpResponseRedirect(guestuser.get_absolute_url())
    return render(request, "e_reg/room_preference_update.html", {'form': form})


@login_required
def hotel_membership_update(request):
    guestuser = request.user
    formset = forms.HotelMembershipUpdateFormSet(queryset=guestuser.guestuser.membership.all())

    if request.method == "POST":
        formset = forms.HotelMembershipUpdateFormSet(request.POST, queryset=guestuser.guestuser.membership.all())

        if formset.is_valid():
            memberships = formset.save(commit=False)
            for membership in formset.deleted_objects:
                membership.delete()

            for membership in memberships:
                membership.guestuser = guestuser.guestuser
                membership.save()
            messages.success(request, "You have succesfully updated your Hotel Memberships")
            return HttpResponseRedirect(guestuser.get_absolute_url())
    return render(request, "e_reg/hotel_membership_update.html", {'formset': formset})
