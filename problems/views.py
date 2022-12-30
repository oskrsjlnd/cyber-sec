from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from .models import Account, Diary

@csrf_protect
def index_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pw = request.POST.get('password')
        account = Account.objects.get(user=username)

        if account.password == pw:
            request.session['authenticated'] = True
            request.session['username'] = username
            return render(request, 'create_entry.html')

    return render(request, 'index.html')

def logout_view(request):
    del request.session['authenticated']
    del request.session['username']
    return render(request, 'index.html')

@csrf_protect
def write_view(request):
    if request.method == "POST":
        entry = request.POST.get('entry')
        account = request.session['username']
        cursor = connections['default'].cursor()
        cursor.execute(f"""INSERT INTO 'problems_diary' (user, entry) VALUES ("{account}","{entry}")""")
        # No parameterized query
        cursor.close()
        return render(request, 'create_entry.html')

    return render(request, 'create_entry.html')

def show_entries_view(request):
    account = request.session['username']
    results = Diary.objects.filter(user=account)
    return render(request, 'show_entries.html', {"entries": results})


def account_view(request):
    if request.method == "POST":
        new_pw = request.POST.get('password')
        user = request.session['username']
        account = Account.objects.get(user=user)
        account.password = new_pw
        account.save(update_fields=['password'])
        
    return render(request, 'account.html')

@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        pw = form.get('password')
        account = Account(user=username, password=pw)
        account.save()
        request.session['authenticated'] = True
        request.session['username'] = username
        return render(request, 'create_entry.html')

    return render(request, 'register.html')