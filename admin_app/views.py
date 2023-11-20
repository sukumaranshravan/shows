from django.shortcuts import render,redirect
from .models import *
from show_app.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
def log_inaction(request):
    u_name=request.POST['user_name']
    p_word=request.POST['password']
    admin_in=admin_tb.objects.filter(user_name=u_name,password=p_word)
    user_check=register_tb.objects.filter(user_name=u_name,password=p_word)
    usr_name_chk=register_tb.objects.filter(user_name=u_name)
    pass_chk=register_tb.objects.filter(password=p_word)
    if admin_in.count()>0:
        # request.session['admin']=admin_in[0].id
        users=register_tb.objects.filter(status='pending')
        show=category_tb.objects.all()
        return render(request,'admin_profile.html',{'key':users,'cat':show})
    elif user_check.count()>0:
        if user_check[0].status=='Approved':
            request.session['yourself']=user_check[0].id
            yourself=register_tb.objects.filter(id=request.session['yourself'])
            shows=show_tb.objects.filter(user_id_id=request.session['yourself'])
            my_id=request.session['yourself']
            mylist=watchlist_tb.objects.filter(user_id_id=my_id)
            return render(request,'user_profile.html',{'key':yourself,'cat':shows,'watch':mylist})
        elif user_check[0].status=='pending':
            messages.add_message(request,messages.INFO,"Your request is under process, thank you for your patience. ")
            return redirect('home')
        else:
            messages.add_message(request,messages.INFO,"Sorry your request is rejected by the admin")
            return redirect('home')
    elif usr_name_chk.count()>0 and pass_chk.count()<1:
        messages.add_message(request,messages.INFO,"Wrong password, try again or reset password.")
        return redirect('home')
    else:
        messages.add_message(request,messages.INFO,"You are not registered with us, please Register")
        return redirect('home') 
    
def admin_profile(request):
    admin=admin_tb.objects.all()
    return render(request,'admin_profile.html',{'key':admin})

def registeraction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    mail=request.POST['email']
    mob=request.POST['mobile']
    picture=request.FILES['picture']
    u_name=request.POST['user_name']
    p_word=request.POST['password']
    register=register_tb(name=name,gender=gender,dob=dob,email=mail,mobile=mob,picture=picture,user_name=u_name,password=p_word)
    register.save()
    messages.add_message(request,messages.INFO,"Registered Successfully!!")
    return redirect('home')

def categoryaction(request):
    category=request.POST['category']
    add=category_tb(category_name=category)
    add.save()
    messages.add_message(request,messages.INFO,'Added to Category list.')
    return render(request,'admin_profile.html')

def log_out(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"Signed Out Successfully..")
    return redirect('home')

def approve(request,id):
    approval=register_tb.objects.filter(id=id).update(status="Approved")
    messages.add_message(request,messages.INFO,"User Added Successfully!")
    return render(request,'admin_profile.html')
def reject(request,id):
    rejection=register_tb.objects.filter(id=id).update(status='Rejected')
    return render(request,'admin_profile.html') 
def edit_shows_admin(request):
    all=show_tb.objects.filter()
    return render(request,'admin_shows.html',{'key':all})

