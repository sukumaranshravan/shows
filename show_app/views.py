from django.shortcuts import render,redirect
from .models import *
from admin_app.models import *
from django.contrib import messages

# Create your views here.
def user_profile(request):
    yourself=register_tb.objects.filter(id=request.session['yourself'])
    show=category_tb.objects.all()
    shows=show_tb.objects.filter(user_id_id=request.session['yourself'])
    my_id=request.session['yourself']
    mylist=watchlist_tb.objects.filter(user_id_id=my_id)
    return render(request,'user_profile.html',{'key':yourself,'cat':shows,'watch':mylist})

def add_show(request):
    show=category_tb.objects.all()
    return render(request,'add_show.html',{'key':show})
    
def add_showaction(request):
    show_name=request.POST['title']
    poster=request.FILES['poster']
    genre=request.POST['genre']
    year=request.POST['year']
    language=request.POST['language']
    rating=request.POST['rating']
    director=request.POST['director']
    story=request.POST['story']
    category=request.POST['category']
    your_id=request.session['yourself']
    user_id=register_tb.objects.filter(id=your_id)
    uid=user_id[0].id
    create=show_tb(title=show_name,poster=poster,genre=genre,year=year,language=language,rating=rating,director=director,story=story,category_id=category,user_id_id=uid)
    create.save()
    messages.add_message(request,messages.INFO,"Show added Successfully.")
    show=category_tb.objects.all()
    return render(request,'add_show.html',{'key':show})

def edit_profile(request):
    view=register_tb.objects.filter(id=request.session['yourself'])
    return render(request,'edit_profile.html',{'key':view})
def edit_profileaction(request):
    your_id=request.session['yourself']
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    mail=request.POST['mail']
    mobile=request.POST['mobile']
    picture=request.FILES['picture']
    u_name=request.POST['user_name']
    p_word=request.POST['password']
    register_tb.objects.filter(id=your_id).update(name=name,gender=gender,dob=dob,email=mail,mobile=mobile,user_name=u_name,password=p_word,picture=picture)
    messages.add_message(request,messages.INFO,"Changes made in your profile successfully")
    return redirect('user_profile')

def find_show(request):
    view=show_tb.objects.all()
    return render(request,'find_show.html',{'key':view})
def searchaction(request):
    item=request.POST['search']
    view=show_tb.objects.filter(title__istartswith=item)|show_tb.objects.filter(year=item)|show_tb.objects.filter(genre__istartswith=item)
    return render(request,'find_show.html',{'key':view})

def see_details(request,id):
    show=show_tb.objects.filter(id=id) # this gives the id of show
    categories=show[0].category_id # we need category id from show id
    cat_id=category_tb.objects.filter(id=categories) # this will give category id from its category_tb
    catname=cat_id[0].category_name # this will give us category name from category_tb as we got id of category in the above step
    return render(request,'see_details.html',{'key':show,'cat':catname})

def gallery(request):   #this function is only a model for me to check how to add this to user profile without creating a table
    shows=show_tb.objects.all()
    return render(request,'gallery.html',{'cat':shows})

def add_to_watchlist(request):
    your_id=request.session['yourself']
    title=request.GET['title']
    rating=request.GET['rating']
    watchlist=watchlist_tb(title=title,user_id_id=your_id,rating=rating)
    watchlist.save()
    messages.add_message(request,messages.INFO,'Show added to watchlist successfully!')
    return redirect('gallery')

def my_watchlist(request):
    my_id=request.session['yourself']
    mylist=watchlist_tb.objects.filter(user_id_id=my_id)
    return render(request,'user_profile.html',{'watch':mylist})

def my_shows(request):
    my_id=request.session['yourself']
    shows=show_tb.objects.filter(user_id_id=my_id)
    return render(request,'my_shows.html',{'key':shows})

def edit_shows_user(request,id):
    show=show_tb.objects.filter(id=id)
    categories=category_tb.objects.all()
    return render(request,'edit_shows.html',{'key':show,'cat':categories})

def edit_showaction(request):
    show_name=request.POST['title']
    poster=request.FILES['poster']
    genre=request.POST['genre']
    year=request.POST['year']
    language=request.POST['language']
    rating=request.POST['rating']
    director=request.POST['director']
    story=request.POST['story']
    category=request.POST['category']
    your_id=request.session['yourself']
    show_id=request.POST['id']
    show_tb.objects.filter(id=show_id).update(title=show_name,poster=poster,genre=genre,year=year,language=language,rating=rating,director=director,story=story,category_id=category,user_id_id=your_id)
    messages.add_message(request,messages.INFO,'Changes made successfully.')
    return redirect('gallery')

def find_my_show(request):
    item=request.POST['search']
    view=show_tb.objects.filter(title__istartswith=item)|show_tb.objects.filter(year=item)|show_tb.objects.filter(genre__istartswith=item)
    return render(request,'my_shows.html',{'key':view})