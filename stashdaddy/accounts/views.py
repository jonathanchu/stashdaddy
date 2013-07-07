from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView

# from .models import  User, AnonymousUser
from .forms import RegistrationForm


class Login(TemplateView):
    template_name = "accounts/login.html"


class RegistrationFormView(FormView):
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)

    def get_form_class(self, request=None):
        return super(RegistrationFormView, self).get_form_class()

    def form_valid(self, form, request=None):
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form, request=None):
        return super(RegistrationFormView, self).form_invalid(form)


class Register(FormView):
    template_name = "registration/registration_form.html"
    form_class = RegistrationForm
    nav = "register"

    def form_valid(self, form):
        # create the user
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1']
        )
        return super(Register, self).form_valid(form)

    def get_success_url(self):
        return "/thanks/"


# def login(request, custom_message=None):
#     """
#     View for logging in.
#     """
#     if not request.user.is_anonymous():
#         # if the user is already logged in, redirect to dashboard
#         next_url = reverse(dashboard)
#         return http.HttpResponseRedirect(next_url)
#     if request.method == 'POST':
#         form = forms.LoginForm(request, request.POST)
#         if form.is_valid():
#             # login the user
#             pass
#     else:
#         form = forms.LoginForm(request, initial={'email': initial_email})
#     return return_to_render('accounts/login_form.html', {
#         'form': form,
#         'custom_message': custom_message,
#     }, context_instance=RequestContext(request))


# def logout(request):
#     """
#     View for logging out.
#     """
#     if request.method == 'POST':
#         request.session.flush()
#         request.user = AnonymousUser()
#     return render_to_response('accounts/login_form.html', {}, context_instance=RequestContext(request))


# def register(request):
#     """
#     View for registering a new user.
#     """
#     if not request.user.is_anonymous():
#         return http.HttpResponseRedirect(reverse(dashboard))

#     if request.method == 'POST':
#         form = forms.EmailRegistrationForm(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = forms.EmailRegistrationForm()

#     return render_to_response('accounts/register_form.html', {
#         'form': form,
#     }, context_instance=RequestContext(request))


@login_required
def dashboard(request):
    """
    Profile view
    """
    try:
        profile_obj = request.user.get_profile()
    except ObjectDoesNotExist:
        return 0
    return render_to_response("accounts/profile.html", {
        "profile_obj": profile_obj,
    }, context_instance=RequestContext(request))


def password_change(request):
    pass


def password_change_done(request):
    pass


def password_reset(request):
    pass

def password_reset_done(request):
    pass
