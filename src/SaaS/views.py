from django.http import HttpResponse
from django.shortcuts import render
from visits.models import Pagevisit

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = Pagevisit.objects.all()
    page_qs = Pagevisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title" : my_title,
        "page_visit_count" : page_qs.count(),
        "total_page_visit_count":qs.count()
    }
    path = request.path
    Pagevisit.objects.create(path=path)
    return render(request,"home.html",my_context)