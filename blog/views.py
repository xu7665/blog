from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import *
from .forms import RegisterForm
# Create your views here.
# class Person(object):
def base(request):
    # t = loader.get_template("indexaaaaa.html")
    # user = {"name":"kkk","age":"12"}
    # c = Context({"title":"ooo","user":user})
    article_list = Article.objects.all()
    caragory_list = Catagory.objects.all()

    return render(request, 'base.html', locals())

def detail(request,id):
    article = get_object_or_404(Article,id)
    return render(request,'detail.html',context={'article':article})


def shenghuo(request):
    # t = loader.get_template("indexaaaaa.html")
    # user = {"name":"kkk","age":"12"}
    # c = Context({"title":"ooo","user":user})
    return render(request,'shenghuo.html',locals())

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            if redirect_to:
                return \
                    redirect(redirect_to)
            else:
                return redirect('/index')

    else:
        form = RegisterForm()

    return render(request,'register.html',locals())

def index(request):
    return render(request,'index.html',context={'form':form,'next':redirect_to})