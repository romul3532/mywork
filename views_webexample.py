from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render 
# Create your views here.

def basic_one(request):
    view="basic_one"
    html="<html><body>ПРИВЕТ МИР! </html></body>"
    return HttpResponse(html)

def template_two(request):
    ##@import url('D:\my_pasport\programmi\anaconda\Artemii\siteAPP\mysite\webexample\mycss');
    view="template_two"
    t=get_template('myview.html')
    html=t.render({'name':view})
    return HttpResponse(None)


def template_three(request):
    view="template_THREE"
    t=get_template('myview.html')
        #html=t.render(Context({'name':view}))
    html=t.render({'name':view})
    return HttpResponse(html)
