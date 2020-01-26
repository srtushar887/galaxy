from django.shortcuts import render

# Create your views here.

from category.models import Category,Subcategory
from pagecontent.models import generalSetting,icon,homeSlider,homeSectionOne,Homeservices,Homemiddlestatic,patner

def index(request):
    maincategory = Category.objects.filter(is_publish=True)
    subcategory = Subcategory.objects.filter(is_publish=True)
    general_setting = generalSetting.objects.all()[:1].get()
    icons = icon.objects.all()
    slider = homeSlider.objects.all()
    sectoonone = homeSectionOne.objects.all()
    homeservice = Homeservices.objects.all()
    homemiddlestatic = Homemiddlestatic.objects.all()[:1].get()
    patners = patner.objects.all()
    context = {
        'maincategory' : maincategory,
        'subcategory' : subcategory,
        'general_setting':general_setting,
        'icons' : icons,
        'slider': slider,
        'sectoonone':sectoonone,
        'homeservice':homeservice,
        'homemiddlestatic':homemiddlestatic,
        'patners':patners
    }
    return render(request,'pages/index.html',context)