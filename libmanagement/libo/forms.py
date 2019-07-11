from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils.html import strip_tags
from .models import User, Book, LendPeriods, Publisher, Author, review, UserProfile
from .validators import email_vailidator
from django.utils import timezone
from django.forms import ModelForm