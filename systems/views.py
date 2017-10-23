from django.shortcuts import redirect


def login_redirect():
    return redirect('/ordering/login')
