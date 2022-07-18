from django.shortcuts import render
from .forms import JournalForm
from .models import User, Journal
from django.shortcuts import redirect
from django.utils import timezone
from datetime import date


# Create your views here.

# def journal_list(request):


def journal_create(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            login_id = int(request.COOKIES.get('login_id'))
            user = User.objects.filter(pk=login_id).first()
            journal = form.save(commit=False)
            journal.author = user
            journal_create_date = date.isoformat(timezone.now())
            print(type(journal_create_date)) # string
            print(journal_create_date) # 2022-07-15
            journal.created_date = journal_create_date
            journal.save()
            return redirect('test')
    else:
        form = JournalForm()
    return render(request, 'journal/create.html', {'form': form})

def journal_list(request):
    print('request:', request)

def journal_date(request):
    user_id = request.COOKIES.get('login_id')
    user = User.objects.filter(pk=user_id).first()
    journals = user.journal_set.all()
    # print(type(journals))
    # print(len(journals))
    # date_list = []
    # for journal in journals:
    #     date_list.append((journal.pk, journal.created_date))
    # print(type(date_list[0])) # string
    # return render(request, 'journal/list_date.html', {'date_list' :    date_list})
    return render(request, 'journal/list_date.html', {'journals' : journals})

def other_journal_date(request, user_pk):
    # print('pk:', pk)
    user = User.objects.filter(pk=user_pk).first()
    journals = user.journal_set.all()
    # date_list = []
    # for journal in journals:
    #     # date_list.append(journal.created_date)
    #     date_list.append((journal.pk, journal.created_date))
    return render(request, 'journal/list_date.html', {'journals' : journals})

def journal_detail(request, journal_pk):
    journal = Journal.objects.filter(pk=journal_pk).first()
    return render(request, 'journal/detail.html', {'journal' : journal})