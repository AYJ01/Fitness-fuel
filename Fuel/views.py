from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def contact(request):
    return render(request,"commonhome.html")



def index(request):
    return render(request, "index.html")

def Register(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        address = request.POST["address"]
        skill = request.POST['skills']
        image = request.FILES['image']
        if Login.objects.filter(username=email).exists():
            messages.error(request, "Email Already Exists")
        else:
            logQry = Login.objects.create_user(
                username=email,
                email = email,
                password=password,
                userType="Shop",
                viewPass=password,
                is_active=1,
            )
            logQry.save()
            if logQry:
                artistReg = Shops.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    rnumber=skill,
                    image=image,
                    loginid=logQry,
                    status = "Approved",
                )
                artistReg.save()
                messages.success(request, "Registration Successfull")
                return redirect("/signin")
    return render(request, "shopregister.html")


def userRegister(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        address = request.POST["address"]
        image = request.FILES["image"]
        if Login.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exists")
        else:
            logQry = Login.objects.create_user(
                username=email,
                email=email,
                password=password,
                userType="User",
                viewPass=password,
                is_active=1,
            )
            logQry.save()
            if logQry:
                userReg = User.objects.create(
                    name=name, email=email, phone=phone, address=address, loginid=logQry,image=image
                )
                userReg.save()
                messages.success(request, "Registration Successfull")
                return redirect("/signin")
    return render(request, "userregister.html")


from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Login, Shops

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user_data = Login.objects.get(username=email)
        except Login.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, "login.html")
        
        print(f"User type: {user_data.userType}")
        print(f"Email: {email}, Password: {password}")

        artist = authenticate(username=email, password=password)
        if artist is None:
            messages.error(request, "Incorrect Email/Password..😥")
            return render(request, "login.html")
        
        if user_data.userType == "Shop":
            try:
                vendor = Shops.objects.get(email=email)
            except Shops.DoesNotExist:
                messages.error(request, "Shop does not exist.")
                return render(request, "login.html")

            if vendor.status == "Not Approved":
                request.session["payMail"] = email
                messages.error(request, "You are not approved yet... Please wait 🙂")
                return render(request, "login.html")

            request.session["uid"] = user_data.id
            messages.info(request, "Login Success")
            return redirect("/shophome")

        elif user_data.userType == "User":
            request.session["uid"] = user_data.id
            request.session["type"] = "User"
            messages.info(request, "Login Success")
            return redirect("/userhome")

        elif user_data.userType == "Trainer":
            request.session["uid"] = user_data.id
            request.session["type"] = "Trainer"
            messages.info(request, "Login Success")
            return redirect("/trainerhome")

        elif user_data.userType == "Admin":
            request.session["uid"] = user_data.id
            request.session["type"] = "Admin"
            messages.info(request, "Login Success")
            return redirect("/adminhome")

        else:
            messages.error(request, "Unknown user type.")
            return render(request, "login.html")

    return render(request, "login.html")


def trainerRegister(request):
    data=Trainer.objects.all()
    if request.POST:
        print("register")
        name = request.POST["name"]
        age = request.POST["age"]
        qualification = request.POST["qualification"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        address = request.POST["address"]
        image = request.FILES['image']
        image2=request.FILES['image2']
        
        if Login.objects.filter(username=email).exists():
            messages.error(request, "Email Already Exists")
        else:
            logQry = Login.objects.create_user(
                username=email,
                password=password,
                userType="Trainer",
                viewPass=password,
                is_active=1,
            )
            logQry.save()
            if logQry:
                artistReg = Trainer.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    image=image,
                    certificate=image2,
                    loginid=logQry,
                    qualification=qualification,
                    age=age,
                    status = "Approved"
                )
                artistReg.save()
                messages.success(request, "Registration Successfull")
                return redirect("/adminhome")
    return render(request, "trainerregister.html",{"data":data})

    



def adminhome(request):
    return render(request,"adminhome.html")

def userhome(request):
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    return render(request,"userhome.html",{"user":user.name})

def shophome(request):
    uid = request.session["uid"]
    user = Shops.objects.get(loginid = uid)
    return render(request,"shophome.html",{"user":user.name})


def trainerhome(request):
    uid = request.session["uid"]
    user = Trainer.objects.get(loginid = uid)
    return render(request,"trainerhome.html",{"user":user.name})



def shopproducts(request):
    uid = request.session["uid"]
    user = Shops.objects.get(loginid = uid)
    product=Products.objects.filter(sid = user)
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        age = request.POST['age']
        price = request.POST['price']
        exptime = request.POST['exptime']
        company = request.POST['company']
        image = request.FILES['image']

        products=Products.objects.create(name=name,desc=desc,age=age,price=price,exptime=exptime,company=company,image=image,sid=user)
        products.save()
    




    return render(request,"shopproducts.html",{'product':product})



def userproducts(request):
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    product=Products.objects.all()
    return render(request,"userproducts.html",{"user":user.name,'product':product})


def usercart(request):
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    pid=request.GET['pid']
    products = Products.objects.get(id = pid)
    cart=Cart.objects.create(uid=user,pid=products)
    cart.save()
    return redirect('/userproducts')


def cart(request):
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    product = Cart.objects.filter(uid=user)
    total = Cart.objects.filter(uid=user).aggregate(total_price=Sum('pid__price'))
    total_price = total['total_price']
    booked=ChildBooking.objects.filter(bid__uid=user )
    if request.method == "POST":
        bid = Booking.objects.create(uid=user,status="Booked",tot=total_price)
        bid.save()
        newbid = Booking.objects.order_by('-id').first()
        for i in product:
            cbid=ChildBooking.objects.create(bid=newbid,pid=i.pid,count=1,tot=i.pid.price)
            cbid.save()
            i.delete()
            
        return redirect(f'/payment?bid={newbid.id}')
    return render(request,"usercart.html",{"user":user.name,'product':product,'booked':booked})


def payment(request):
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    users=User.objects.filter(loginid = uid)
    product = Cart.objects.filter(uid=user)
    booked=ChildBooking.objects.filter(bid__uid=user )
    bid = request.GET['bid']
    book=Booking.objects.get(id=bid)
    total=Booking.objects.get(id=book.id)
    if request.method == 'POST':
        book.status="Paid"
        book.save()
        return redirect("/cart")
    
    return render(request,"payment.html",{"user":users,'product':product,'booked':booked,'total':total.tot})

def adminproducts(request):
    products=Products.objects.all()
    return render(request,"adminproducts.html",{'products':products})

def adminusers(request):
    products=User.objects.all()
    return render(request,"adminusers.html",{'products':products})

def adminshops(request):
    products=Shops.objects.all()
    return render(request,"adminshops.html",{'products':products})

def admintrainers(request):
    products=Trainer.objects.all()
    return render(request,"admintrainers.html",{'products':products})

def adminarticles(request):
    products=Articles.objects.all()
    if request.method == "POST":
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']
        image= request.FILES['image']
        article=Articles.objects.create(heading=heading,paragraph=paragraph,image=image)
        article.save()
    return render(request,"adminarticles.html",{'products':products})



def admindeletearticle(request):
    id=request.GET["aid"]
    aid=Articles.objects.get(id=id)
    aid.delete()
    
    return redirect('/adminarticles')

def admindeleteuser(request):
    id=request.GET["aid"]
    aid=User.objects.get(id=id)
    aid.delete()
    
    return redirect('/adminusers')

def admindeletetrainer(request):
    id=request.GET["aid"]
    aid=Trainer.objects.get(id=id)
    aid.delete()
    
    return redirect('/admintrainer')

def admindeleteshops(request):
    id=request.GET["aid"]
    aid=Shops.objects.get(id=id)
    aid.delete()
    
    return redirect('/adminshops')




def usertrainers(request):
    uid = request.session["uid"]
    user = User.objects.get( loginid=uid)
    product = Trainer.objects.all()
    return render(request, "usertrainers.html", {"user": user.name, 'product': product})
def userchat(request):
    tid = request.GET['tid']
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    trainer = Trainer.objects.get( id=tid)
    chats = Chat.objects.filter((Q(uid=user)) &  Q(tid=trainer))
    if request.method == 'POST':
        message_content = request.POST.get('message')
        
        chat = Chat.objects.create(uid=user, tid=trainer, message=message_content,sender=user.email)
        chat.save()
    return render(request, "userchat.html", {'chats': chats, 'trainer': trainer})

def send_message(request, trainer_id):
    return redirect(f'/userchat?tid={trainer_id}')


def userarticles(request):
    uid = request.session["uid"]
    user = User.objects.get(loginid = uid)
    product = Articles.objects.all()
    return render(request,'articles.html', {"user": user.name, 'product': product})


def traineruser(request):
    uid = request.session["uid"]
    user = Trainer.objects.get( loginid=uid)
    product = User.objects.all()
    return render(request, "traineruser.html", {"user": user.name, 'product': product})
def trainerchat(request):
    tid = request.GET['tid']
    uid = request.session["uid"]
    user = User.objects.get(id = tid)
    trainer = Trainer.objects.get( loginid=uid)
    chats = Chat.objects.filter((Q(uid=user)) & Q(tid=trainer))
    if request.method == 'POST':
        message_content = request.POST.get('message')
        chat = Chat.objects.create(uid=user, tid=trainer, message=message_content,sender=trainer.email)
        chat.save()
    return render(request, "trainerchat.html", {'chats': chats, 'trainer': trainer})



def shoporder(request):
    uid = request.session["uid"]
    user = Shops.objects.get(loginid = uid)
   
    booked=ChildBooking.objects.filter(pid__sid=user )
    return render(request, "shoporder.html", {"user":user.name,'booked':booked})


def shopdelivery(request):
    bid=request.GET['bid']
    booked = Booking.objects.get(id=bid)
    booked.status='Delivered'
    booked.save()
    return redirect('/shoporder')