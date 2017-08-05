from django.shortcuts import render, render_to_response
from apiManager import flyApi


def index(request):

    return render(request, "Home.html")


def resultFly(request):
    origin= request.form.get('')
    desttination = request.form.get('')
    numbAdult = request.form.get('')
    numbChild = request.form.get('')
    deparDate = request.form.get('')
    arivDate = request.form.get('')