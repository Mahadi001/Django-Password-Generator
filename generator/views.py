from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generatorapp/index.html')

def password(request):
    
    length = int(request.GET.get('length', 9))

    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_()')
    password = ''

    if request.GET.get('radio_options') == "uppercase":
        characters = (list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('radio_options') == "lowercase":
        characters = (list('abcdefghijklmnopqrstuvwxyz'))
        
    if request.GET.get('radio_options') == "numbers":
        characters = (list('1234567890'))

    if request.GET.get('radio_options') == "special_characters":
        characters = (list('!@#$%^&*_()'))

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generatorapp/password.html', {'password': password})