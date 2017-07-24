from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import *
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