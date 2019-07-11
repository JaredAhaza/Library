from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# from .forms import AuthenticateForm, UserCreateForm, UserEditForm, AuthorForm, PublisherForm, LendPeriodForm, BookForm
from .models import Book, LendPeriods, Publisher, Author, review, UserProfile
# from .tables import BookTable, FriendTable, BookTableUser, AuthorTable, PublisherTable, PeriodsTable
from django_tables2 import RequestConfig
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .decorators.group_required import group_required
from django.db.models.base import ObjectDoesNotExist



def index(request):
    return HttpResponse("Hello, we welcome you to our services that allows you to have better library management services.")


def sign_in(request, auth_form=None):
    """
    View responsible for sign in using username and password

    :param auth_form: form that validates whether user can be authorized
    :type auth_form: `AuthenticationForm()`
    """
    if request.user.is_authenticated():
        redirect('/')
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        else:
            auth_form = auth_form or AuthenticateForm()
            return render(request, 'sign_in.html', {'auth_form': auth_form})
    auth_form = AuthenticateForm()
    return render(request, 'sign_in.html', {'auth_form': auth_form})