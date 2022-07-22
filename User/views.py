from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# from django.contrib.auth import authenticate,login,logout
from .forms import UserForm, UserFormLogin
from django.shortcuts import redirect
from django.contrib import auth
# from django.contrib.auth.models import User

# Create your views here.

def user_list(request):
    login_id = int(request.COOKIES.get('login_id'))
    users = User.objects.all() # type(users):django.db.models.query.QuerySet.   <QuerySet [<User: 李岳峰>, <User: 梅西>]>
    return render(request, 'user/user_list.html', {'users' : users, 'login_id' : login_id})

# def register(request):
#     form = UserForm()
#     return render(request, 'user/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.save()
        #     # return redirect('post_detail', pk=post.pk)
        #     return redirect('user_list')
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(name=name, username=username, password=password, email=email)
        return redirect("user_list")
    # else:
    #     form = UserForm()
    # return render(request, 'user/register.html', {'form': form})
    return render(request, 'user/register.html', {})

def login(request):
    if request.method == "POST":
        form = UserFormLogin(request.POST)
        if form.is_valid():
            # print(form.data)
            # print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password)
            print(user)
            user_id = user[0].pk
            if (len(user) == 1):
                # auth.login(request, user)
                # return render(request, 'user/success.html', {})
                # response = redirect('/user/all/')
                response = redirect('user_list')
                response.set_cookie('is_login', True)
                response.set_cookie('login_id', user_id)
                return response
                # users = User.objects.all()
                # return render(request, 'user/user_list.html', {'users': users})
            else:
                return render(request, 'user/fail.html', {})

    else:
        form = UserFormLogin()
        return render(request, 'user/login.html', {'form': form})

def login_test(request):
    if request.method == "GET":
        return render(request, "user/login_test.html")
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username=username, password=password)
    if (len(user) == 1):
        user_id = user[0].pk
        # auth.login(request, user)
        # return render(request, 'user/success.html', {})
        # response = redirect('/user/all/')
        response = redirect('user_list')
        response.set_cookie('is_login', True)
        response.set_cookie('login_id', user_id)
        return response
    # print(username)
    # print(password)
    return render(request, "user/login_test.html", {'rlt': username})

def index(request):
    login_id = 'False'
    try:
        login_id = int(request.COOKIES.get('login_id'))
        is_login = request.COOKIES.get('is_login')
    except:
        return render(request, 'user/index.html')
    if is_login == 'True':
        user = User.objects.filter(pk=login_id).first()
    return render(request, 'user/index.html', {'is_login': is_login, 'user': user})

def s(request):
    return render(request, 'user/test.html')

def test(request):
    if request.method == "GET":
        return HttpResponse("GET 方法")
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法1")