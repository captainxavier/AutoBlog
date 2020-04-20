from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from accounts.forms import AccountRegistrationForm,AccountAuthenticationForm

#Account Registration View.
def sign_up_view(request):
    context = {}
    redirect_to = request.POST.get('next', '/')
    if request.POST:
        form = AccountRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=email, password=raw_password)
            login(request, account)
            if 'next' in request.POST:
                return HttpResponseRedirect(redirect_to)
            else:
                return redirect('home')
        else:
            context['form'] = form
    else:
        form = AccountRegistrationForm()
        context['form'] = form
        print(context)
    return render(request, 'accounts/sign-up.html', context)


#User Login View
def sign_in_view(request):
    context = {}
    redirect_to = request.POST.get('next', '/')
    user = request.user

    if user.is_authenticated: 
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if 'next' in request.POST:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return redirect('home')


    else:
        form = AccountAuthenticationForm()

    context['form'] = form
    return render(request, "accounts/sign-in.html", context)  

    
        
#Logout User
def logout_view(request):
    logout(request)
    return redirect('home')
