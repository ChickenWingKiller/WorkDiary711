from django.shortcuts import render
from .models import User

# Create your views here.

def user_list(request):
    user = User.objects.order_by('name')
    return render(request, 'user/user_list.html', {user})