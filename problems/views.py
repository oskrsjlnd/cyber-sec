from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from .models import Account, Diary#, UserLogs
# FIX FOR LOGGING
# from datetime import datetime

# FIX FOR BROKEN AUTHENTICATION
# from werkzeug.security import generate_password_hash, check_password_hash

@csrf_protect
def index_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pw = request.POST.get('password')
        account = Account.objects.get(user=username)

        if account.password == pw:
        # FIX TO BROKEN ACCESS CONTROL
        # if check_password_hash(account.password, pw):
        
        # FIX FOR MISSING LOGGING
        #   UserLogs.objects.create(user=request.session['username'], time=datetime.now(), event="USER LOGGED IN")
            request.session['authenticated'] = True
            request.session['username'] = username
            return render(request, 'create_entry.html')
        # FIX FOR MISSING LOGGING
        # else:
            # UserLogs.objects.create(user=username ,time=datetime.now(), event="FAILED LOGIN")

    return render(request, 'index.html')

def logout_view(request):
    # FIX TO BROKEN ACCESS CONTROL
    # if request.session['authenticated']:

    # FIX FOR LOGGING
    # UserLogs.objects.create(user=request.session['username'], time=datetime.now(), event="USER LOGGED OUT")
    del request.session['authenticated']
    del request.session['username']
    return render(request, 'index.html')

@csrf_protect
def write_view(request):
    # FIX TO BROKEN ACCESS CONTROL
    if request.method == "POST": # and request.session['authenticated']:
        entry = request.POST.get('entry')
        account = request.session['username']
        cursor = connections['default'].cursor()
        cursor.execute(f"""INSERT INTO 'problems_diary' (user, entry) VALUES ("{account}","{entry}")""")
        # No parameterized query

        # FIX FOR SQL INJECTION BELOW
        # diary = Diary(user=user, entry=entry)
        # diary.save()
        cursor.close()
        return render(request, 'create_entry.html')

    return render(request, 'create_entry.html')

def show_entries_view(request):
    # FIX FOR BROKEN ACCESS CONTROL
    # if request.session['authenticated']:
    account = request.session['username']
    results = Diary.objects.filter(user=account)
    return render(request, 'show_entries.html', {"entries": results})


def account_view(request):
    if request.method == "POST": # and request.session['authenticated']:
        current_pw = request.POST.get("current pw")
        new_pw = request.POST.get('new password')
        user = request.session['username']
        account = Account.objects.get(user=user)

    #   CHECK USER KNOWS CURRENT PW BEFORE CHANGING TO NEW ONE
    #   if account.password == current_pw:
    # FIX TO BROKEN AUTHENTICATION
    # if check_password_hash(account.password, current_pw)
    #   account.password = generate_password_hash(new_pw, method="pbkdf2:sha256", salt_length=16)
        account.password = new_pw
        account.save(update_fields=['password'])
            # FIX MISSING LOGGING
            # UserLogs.objects.create(user=user, time=datetime.now(), event="USER PASSWORD CHANGED")
        return render(request, "create_entry.html")
        # FIX MISSING LOGGING
        # else:
            # UserLogs.objects.create(user=user, time=datetime.now(), event="FAILED PASSWORD CHANGE")
    return render(request, 'account.html')


@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        pw = form.get('password')

        # Passwords are not stored with secure hashing and functions
        # account = Account(user=username, password=generate_password_hash(pw, method="pbkdf2:sha256", salt_length=16)
        account = Account(user=username, password=pw)
        account.save()
        request.session['authenticated'] = True
        request.session['username'] = username
        return render(request, 'create_entry.html')

    return render(request, 'register.html')