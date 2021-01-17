from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url
from .models import GuestEmail
from accounts.forms import LoginForm, RegisterForm, GuestForm
from django.views.generic import CreateView, FormView

def guest_register_view(request):
    guest_form = GuestForm(request.POST or None)
    context = {
        'form': guest_form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if guest_form.is_valid():
        email = guest_form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')
    return redirect('/register/')


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = "accounts/login.html"

    def form_valid(self, login_form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(login_form)




class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

# User = get_user_model()
# def register_page(request):
#     register_form = RegisterForm(request.POST or None)
#     context = {
#         'form': register_form
#     }
#     if register_form.is_valid():
#         register_form.save()
#     return render(request, "accounts/register.html", context)



# def login_page(request):
#     login_form = LoginForm(request.POST or None)
#     context = {
#         'form': login_form
#     }
    
#     if login_form.is_valid():
#         username = login_form.cleaned_data.get('username')
#         password = login_form.cleaned_data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             print("Error")
#             # Return an 'invalid login' error message.

#     return render(request, "accounts/login.html", context)

