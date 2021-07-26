from django.contrib.auth import login, authenticate, models, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUser, PostForm, AuthForm, ChangePasswordForm, EditForm
from .models import Post, CategoryClass, Place
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import UpdateView
from django.contrib.auth.forms import PasswordChangeForm

def logIn(request):
    if request.method == 'GET':
        form = AuthForm
    else:
        form = AuthForm(data=request.POST)
        username = form.data.get('username')
        raw_password = form.data.get('password')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('main-page')
        else:
            return redirect('login-page')

    return render(request, 'register/LogIn.html', {'form':form})

def logOut(request):
    logout(request)
    return redirect('login-page')

def main_page(request):
    user = request.user

    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    posts = Post.objects.all()
    return render(request, 'profilePage/main.html', {'post':posts, 'user':user, 'categories':categories, 'places':places})


def articles(request, slug):
    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    article = Post.objects.get(slug=slug)
    return render(request, 'profilePage/single.html', {'article':article, 'categories': categories, 'places': places,})


def create_user(request):

    if request.method == 'GET':
        form = CreateUser()
    else:
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
    return render(request, 'register/register.html', {'form': form})


def create_post(request):
    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    if request.method == 'GET':
        form = PostForm
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main-page')
    return render(request, 'profilePage/createPost.html', {'form': form, 'categories': categories, 'places': places,})


def filter_categories(request, slug):
    user = request.user
    posts = Post.objects.filter(categories__slug=slug)
    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    return render(request, 'profilePage/main.html',
                  {'post': posts, 'categories': categories, 'places': places, 'user':user})



def filter_place(request, slug):
    user = request.user
    posts = Post.objects.filter(places__slug=slug)
    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    return render(request, 'profilePage/main.html',
                  {'post': posts, 'categories': categories, 'places': places, 'user':user})


def user_page(request):
    user = request.user
    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    if request.method == 'POST':
        form = CreateUser(data=request.POST)
        user = get_user_model()
        user = user.objects.get(pk=form.data['user_id'])
        if user is not None:
            user.username = form.data['username']
            user.address = form.data['address']
            user.phone_number = form.data['phone_number']
            user.save()
            return redirect('main-page')
    return render(request, 'profilePage/cabinet.html',
                  {'categories': categories, 'places': places, 'user':user})


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = '/bosh-sahifa'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'profilePage/update_post.html'
    success_url = '/my-posts/'


def user_posts(request):
    user = request.user
    categories = CategoryClass.objects.all()
    places = Place.objects.all()
    post = Post.objects.filter(author=request.user.id)
    return render(request, 'profilePage/user_page.html',
                  {'user': user, 'post':post, 'categories': categories, 'places': places,})


