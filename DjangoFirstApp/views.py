from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member

def DjangoFirstApp(request):
  return HttpResponse("Hello world!")

def index2(request):
  template = loader.get_template('index2.html')
  return HttpResponse(template.render())

def home(request):
  return HttpResponse("Hello world!")

def main(request):
  template = loader.get_template('main.html') # main.html ou index.html
  return HttpResponse(template.render())

def home_view(request,*args, **kwargs):
  return HttpResponse("<h1>Hello World</h1>")

def index(request):
    members = Member.objects.all()
    member_list_html = [f"<li>{member.name}</li>" for member in members]
    return HttpResponse(f"<ul>{''.join(member_list_html)}</ul>")

def add_member(request, member_name):
    Member.objects.create(name=member_name)
    return redirect('index')