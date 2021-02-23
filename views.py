from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render ###render_to_response
# Create your views here.

def basic_one(request):
    view="basic_one"
    #view="template_two"
    #t=get_template('myview.html')
    #html=t.render(Context({'name':'view'}))
    html="<html><body>ПРИВЕТ МИР! </html></body>"
    return HttpResponse(html)

def template_two(request):
    @import url('D:\my_pasport\programmi\anaconda\Artemii\siteAPP\mysite\webexample\mycss');
    ##view="template_two"
    ##t=get_template('myview.html')### .css
    ##html=t.render({'name':view})
    return HttpResponse(None)###(html)


def template_three(request):
    view="template_THREE"
    t=get_template('myview.html')
        #html=t.render(Context({'name':view}))
    html=t.render({'name':view})
    return HttpResponse(html)
    ####t=get_template('myview.html')
    ####tml=t.render(Context({'name':view}))
    ####"<html><body> МЫ ЗДЕСЬ ??! </html></body>"
    ####return HttpResponse(html)
    #return render(request,'myview.html',{'name':view})
