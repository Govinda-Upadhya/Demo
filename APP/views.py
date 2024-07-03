from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    homepage = Homepage.objects.all()
    context ={
        'home': homepage,
    }
    return render(request,'index.html',context)

def about(request):
    raw_material = Raw_material.objects.all()
    homepage = Homepage.objects.all()
    product = Production_capcity.objects.all()
    team = Team_Member.objects.all()
    context = {
        'raw': raw_material,
        'home': homepage,
        'product': product,
        'team': team,
    }
    return render(request,'about.html',context)

def products(request):
    return render(request,'product.html')

def environmental(request):
    certificates = Certificates.objects.all()
    context = {
        'certificates': certificates,
    }
    return render(request,'environmental.html',context)

def announcements(request):
    career = Career.objects.all()
    announcement = Announcement.objects.all()
    context = {
        'career': career,
        'announcement': announcement,
    }
    return render(request,'announcements.html',context)

def announcement_detail(request,pk):
    announcements = get_object_or_404(Announcement, pk=pk)
    context ={
        'announcement': announcements,
    }
    return render (request,'announcement_details.html',context)

def contact(request):
    team = Team_Member.objects.all()
    context = {
        'team': team,
    }
    return render(request,'contact.html',context)