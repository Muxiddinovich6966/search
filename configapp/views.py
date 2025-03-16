from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from configapp.forms import NewsForm, UserLoginForm
from .models import News, Categories


@login_required(login_url='login')
def index(request):
    new = News.objects.all()
    cat = Categories.objects.all()
    return render(request, 'index.html', {'news': new, 'categories': cat})


@login_required(login_url='login')
def categories(request, category_id):
    cate = get_object_or_404(Categories, id=category_id)
    news = News.objects.filter(category=cate)
    return render(request, 'categories.html', {'news': news, 'category': cate})


@login_required(login_url='login')
def new_del(request, new_id):
    new = get_object_or_404(News, id=new_id)
    new.delete()
    return redirect('index')


@login_required(login_url='login')
def new_about(request, new_id):
    newx = get_object_or_404(News, id=new_id)
    cate = Categories.objects.all()
    return render(request, 'about.html', {'new': newx, 'categories': cate})


@login_required(login_url='login')
def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsForm()
    return render(request, 'news_add.html', {'form': form})


@login_required(login_url='login')
def new_update(request, new_id):
    new = get_object_or_404(News, id=new_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsForm(instance=new)
    return render(request, 'update.html', {'form': form, 'new': new})


@login_required(login_url='login')
def search_view(request):
    query = request.GET.get('q', '')
    results = News.objects.filter(
        Q(title__icontains=query) |
        Q(context__icontains=query)
    ) if query else News.objects.all()
    return render(request, 'search.html', {'news_list': results, 'query': query})


@login_required(login_url='login')
def new_detail(request, new_id):
    new = get_object_or_404(News, id=new_id)
    return render(request, 'detail.html', {'new': new})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logoutPage(request):
    logout(request)
    return redirect('login')
