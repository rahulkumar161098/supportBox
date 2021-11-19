from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib import messages
# from django.db.models import Q

# Create your views here.
def index(request):
    all_articles= Article.objects.all().order_by('-date')
    return render(request,'index.html',{'article':all_articles})


    #     all_articles = Article.objects.all().order_by('-date')
    # return render(request,'blog.html',{'article':all_articles})

def details(request,art_id):
    return render (request,'details.html', {'art':Article.objects.get(id = art_id)})


def search(request):
    search = request.GET['search']
    all_articles_title= Article.objects.filter(title__icontains=search)
    all_articles_body= Article.objects.filter(body__icontains=search)
    all_articles = all_articles_title.union(all_articles_body)
    if all_articles.count() == 0:
        messages.error(request,"no result fount")
    return render(request, 'search.html', {'article': all_articles,'query':search})