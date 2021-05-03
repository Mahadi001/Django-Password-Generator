from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generatorapp/index.html')

def password(request):
    
    length = int(request.GET.get('length', 12))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*_()'))

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generatorapp/password.html', {'password': password})