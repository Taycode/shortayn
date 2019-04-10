from django.shortcuts import render, redirect


def index(request):
    from .forms import LinkForm
    if request.method == 'GET':
        form = LinkForm()
        args = {'form':form}
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
        pass
