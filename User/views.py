from django.shortcuts import render
from .models import User
# from django.contrib.auth import authenticate,login,logout
from .forms import UserForm, UserFormLogin
from django.shortcuts import redirect
from django.contrib import auth
# from django.contrib.auth.models import User

# Create your views here.

def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users' : users})

# def register(request):
#     form = UserForm()
#     return render(request, 'user/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = UserFormLogin(request.POST)
        if form.is_valid():
            # print(form.data)
            # print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password)
            if (len(user) != 0):
                # auth.login(request, user)
                # return render(request, 'user/success.html', {})
                users = User.objects.all()
                return render(request, 'user/user_list.html', {'users': users})
            else:
                return render(request, 'user/fail.html', {})

    else:
        form = UserFormLogin()
        return render(request, 'user/login.html', {'form': form})

# def login(request):
#     if request.method == "GET":
#         return render(request, "user/login.html")
#     username = request.POST.get("username")
#     password = request.POST.get("pwd")
#     valid_num = request.POST.get("valid_num")
#     keep_str = request.session.get("keep_str")
#     if keep_str.upper() == valid_num.upper():
#         user_obj = auth.authenticate(username=username, password=password)
#         print(user_obj.username)


def index(request):
    return render(request, 'user/index.html')