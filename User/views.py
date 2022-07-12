from django.shortcuts import render
from .models import User
from .forms import UserForm, UserFormLogin
from django.shortcuts import redirect

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
            # print(form.data.get('username'))
            username = form.data.get('username')
            password = form.data.get('password')
            user =User.objects.filter(username=username, password=password)
            if (len(user) != 0):
                return render(request, 'user/success.html', {})
            else:
                return render(request, 'user/fail.html', {})

    else:
        form = UserFormLogin()
    return render(request, 'user/login.html', {'form': form})


def index(request):
    return render(request, 'user/index.html')