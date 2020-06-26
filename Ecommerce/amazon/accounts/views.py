from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .forms import LoginForm,RegisterForm
from django.utils.http import is_safe_url
# from django.contrib.auth.views import logout

def login_form(request):
    form = LoginForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path,request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            messages.info(request,"invalid username and password")
            return HttpResponseRedirect('accounts/login.html')

    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login/")


User = get_user_model()
def register_form(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        password2 = form.cleaned_data.get("password2")
        new_user = User.objects.create_user("username","email","password")
        print("new_user")
        form.save()
        messages.success(request, 'Form submission successful')
        return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request,'accounts/register.html',{'form':form})

