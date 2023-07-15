from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>ВСЕМ ПРИВЕТ!</h1>
        <a class="navbar-brand" href="lesson_4/">
            ДОМАШКА ДЛЯ ЗАДАНИЯ №4
        </a> 
    """)

def lesson(request):
    return HttpResponse("""
        <h1> СОДЕРЖИМОЕ </h1>
    """)