from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home:dashboard')
        else:
            return render(request, 'home/index.html')



def redirect_user(request, short_code):
    from .models import Link
    url = Link.objects.get(short_code=short_code)
    url.amount_of_visits += 1
    url.save()
    return redirect(url.redirect_to)



def login_view(request):

    if request.method == 'GET':
        return render(request, 'home/login.html')

    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email.lower())
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('home:home')
        except:
            messages.add_message(request, messages.WARNING, 'email or password is incorrect')
            return redirect('home:login')


def signup_view(request):
    if request.method == 'GET':
        from home.forms import RegistrationForm
        form = RegistrationForm
        args = {'form': form}
        return render(request, 'home/signup.html', args)
    else:
        from home.forms import RegistrationForm
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email)
            print(user)
            if user.count() == 0:
                saved = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                saved.email = form.cleaned_data['email'].lower()
                saved.save()
                user = authenticate(username=username, password=password)

                if user is not None:
                    print(user)
                    if user.is_active:
                        login(request, user)
                        return redirect('home:home')
            else:
                messages.add_message(request, messages.ERROR, 'email has already been used')
                return render(request, 'home/signup.html', {'form': form})
        else:
            return render(request, 'home/signup.html', {'form': form})


@login_required
def dashboard(request):
    from .forms import LinkForm
    from .models import Link
    from ipaddr import client_ip
    import requests
    if request.method == 'GET':
        form = LinkForm()
        links = Link.objects.filter(user=request.user)
        total_clicks = 0
        for link in links:
            total_clicks += link.amount_of_visits
        client_address = client_ip(request)
        response = requests.get("http://ip-api.com/json/"+ client_address)
        args = {'form': form, 'links': links, 'total_clicks': total_clicks, 'ip_data':response.json()}

        return render(request, 'home/dashboard.html', args)
    else:
        form = LinkForm(request.POST)
        if form.is_valid:
            saved = form.save(commit=False)
            saved.user = request.user
            saved.save()
            return redirect('home:home')


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home:home')


def delete_link(request, short_code):
    from home.models import Link
    link = Link.objects.get(short_code=short_code)
    link.delete()
    return redirect('home:home')