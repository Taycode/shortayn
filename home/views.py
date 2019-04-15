from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def index(request):
    from .forms import LinkForm
    if request.method == 'GET':
        form = LinkForm()
        args = {'form': form}
        return render(request, 'home/index.html', args)
    else:
        form = LinkForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home:home')
    return render(request, 'home/index.html')


def redirect_user(request, short_code):
    from .models import Link
    url = Link.objects.get(short_code=short_code)
    return redirect(url.redirect_to)



def login_view(request):

    if request.method == 'GET':
        return render(request, 'home/login.html')

    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)
            print('authenticated', user)
            login(request, user)
            return redirect('home:home')
        except:
            return redirect('home:signup')


def signup_view(request):
    if request.method == 'GET':
        from home.forms import RegistrationForm
        form = RegistrationForm
        args = {'form': form}
        return render(request, 'home/signup.html', args)
    else:
        from home.forms import RegistrationForm
        form = RegistrationForm(request.POST)
        if form.is_valid:
            saved = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            saved.save()
            user = authenticate(username=username, password=password)
            print('authenticated', user)

            if user is not None:
                print(user)
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')


def shorten(request):
    pass