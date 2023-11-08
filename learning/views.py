from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .models import category,photo,urlClass,snippet_class


def gallery(request):
    category1 = request.GET.get('category')
    # print('category:',category1)

    if category1 == None:
        total_objects = photo.objects.all
    else:
        total_objects = photo.objects.filter(category__name=category1)
    
    categories = category.objects.all()

    # total_objects=photo.objects.all()

    context={'categories': categories,'total_objects': total_objects}
    res=render(request,'learn/gallery.html',context)
    return res


def add_context(request):
    
    categories = category.objects.all()

    if request.method =='POST':
        category1=''
        data =request.POST
        ques_image=request.FILES.get('ques_image')
        ans_image=request.FILES.get('ans_image')
        ans_second_image=request.FILES.get('ans_second_image')

        if data['category'] !='none':
            category1=category.objects.get(id=data['category'])
        elif data['category_new'] !='':
            category1,created = category.objects.get_or_create(name=data['category_new'])
        else:
            category1=None

        photo_object=photo.objects.create(
            category=category1,
            description=data['description'],
            ques_image=ques_image,
            ans_image=ans_image,
            ans_second_image=ans_second_image,
            ques_no=data['ques_no'],
            ques_url=data['ques_url'],
            ans_url=data['ans_url'],
            ques_heading=data['ques_heading'],

        )

        return HttpResponseRedirect('gallery')


       
    
    context={'categories': categories}
    res=render(request,'learn/add.html',context)
    return res

def urls(request):
    url_objects=urlClass.objects.all()
    context={'url_objects': url_objects}
    res=render(request,'learn/url.html',context)
    return res

def snippets(request):
    snippet_objects=snippet_class.objects.all()
    context={'url_objects': snippet_objects}
    res=render(request,'learn/snippets.html',context)
    return res