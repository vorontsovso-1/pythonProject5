from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#     return HttpResponse("""
#         <h1>Все супер</h1>
#         <a class="navbar-brand" href="lesson_4/">
#             Домашняя работа 4 занятия
#         </a>
#     """)
#
# def lesson(request):
#     return HttpResponse("""
#         <h1> Вот и домашка </h1>
#     """)
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, "top-sellers.html")
