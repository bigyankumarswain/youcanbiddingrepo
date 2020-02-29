from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserModel,ProductModel,BiddingModel,MaxAmountModel

def user_register(request):
    if request.method == "POST":
        pswd = request.POST.get("pswd")
        pswd1 = request.POST.get("pswd1")
        if pswd == pswd1:
            name = request.POST.get("name")
            contact = request.POST.get("contact")
            img = request.FILES["img"]
            email = request.POST.get("email")
            status="pending"

            UserModel(name=name,email=email,password=pswd,contact=contact,image=img,status=status).save()
            messages.success(request, "Your Registration Request Sent Successfully")
            return render(request,"home.html")
        else:
            messages.success(request,"Enter Same Password  Two Times")
            return render(request, "usertemp/register.html")
    else:
        return render(request,"usertemp/register.html")

def userLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pswd = request.POST.get("pswd")
        try:
            data = UserModel.objects.get(email=email, password=pswd)
            if data.status == "approved":
                request.session["uemail"] = email
                return render(request, "usertemp/welcome.html", {"data": data})
            elif data.status == "blocked":
                messages.success(request, "Your acount is temporary blocked .")
                return redirect('login')
            else:
                messages.success(request, "Your acount registation is till  now pending .")
                return redirect('login')
        except:
            messages.success(request, "Invalid Email And Password")
            return redirect('login')
    else:
        try:
            if request.session["uemail"]:
                email = request.session["uemail"]
                data = UserModel.objects.get(email=email)
                return render(request, "usertemp/welcome.html", {"data": data})
            else:
                return render(request,"usertemp/login.html")
        except:
            return render(request,"usertemp/login.html")


def userLogout(request):
    try:
        del request.session["uemail"]
        messages.success(request, "You Successful Logged Out")
        return redirect('home')
    except:
        return redirect('login')


def user_welcome(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        return render(request, "usertemp/welcome.html", {"data": data})
    except:
        return redirect('login')


def selling(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def buying(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        all_bid = MaxAmountModel.objects.all()
        if all_bid:
            return render(request, "usertemp/welcome.html", {"data": data, "buy": "buy", "allbid": all_bid})
        else:
            messages.success(request, "Sorry we have no Product .")
            return render(request, "usertemp/welcome.html", {"data": data, "buy": "buy"})
    except:
        return redirect('login')


def add_product(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        if request.method == "POST":
            name = request.POST.get("name")
            image = request.FILES["img"]
            minbidprice = request.POST.get("minbidprice")
            details = request.POST.get("details")

            ProductModel(pname=name, minprice=minbidprice, discription=details, status="not_bid", image=image,
                         userinfo_id=data.uid).save()
            messages.success(request, "Your Product is Successfully Added .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
        else:
            addproduct = "Add Your Product"
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "add": addproduct})
    except:
        return redirect('login')


def view_all_product(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        allproduct = ProductModel.objects.filter(userinfo_id=data.uid)
        if allproduct:
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "allProduct": allproduct})
        else:
            messages.success(request, "You have no product  now .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def product_not_bid(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        try:
            ProductModel.objects.filter(userinfo_id=data.uid)
            try:
                qs = ProductModel.objects.filter(userinfo_id=data.uid, status="not_bid")
                if qs:
                    return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "notbid": qs})
                else:
                    messages.success(request, "There is no product like not-bidding .")
                    return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
            except ProductModel.DoesNotExist:
                messages.success(request, "There is no product like not-bidding .")
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
        except ProductModel.DoesNotExist:
            messages.success(request, "There is no product You added .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def product_bid(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        try:
            ProductModel.objects.filter(userinfo_id=data.uid)
            try:
                qs = ProductModel.objects.filter(userinfo_id=data.uid, status="bid")
                if qs:
                    return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "bid": qs})
                else:
                    messages.success(request, "There is no product like bidding .")
                    return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
            except ProductModel.DoesNotExist:
                messages.success(request, "There is no product like bidding .")
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
        except ProductModel.DoesNotExist:
            messages.success(request, "There is no product You added .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def product_sold(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        try:
            ProductModel.objects.filter(userinfo_id=data.uid)
            try:
                qs = ProductModel.objects.filter(userinfo_id=data.uid, status="sold")
                if qs:
                    return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "sold": qs})
                else:
                    messages.success(request, "There is no product like sold .")
                    return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
            except:
                messages.success(request, "There is no product like sold .")
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
        except:
            messages.success(request, "There is no product You added .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def add_to_bid(request,pid):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        ProductModel.objects.filter(pid=pid).update(status="bid")
        ps = ProductModel.objects.get(pid=pid)
        amt = ps.minprice
        MaxAmountModel(maxamount=amt, pid_id=pid, uid_id=data.uid).save()
        qs = ProductModel.objects.filter(userinfo_id=data.uid, status="not_bid")
        if qs:
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "notbid": qs})
        else:
            messages.success(request, "There is no product like not-bidding .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def bidding_product(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        pid = request.POST["pid"]
        price = int(request.POST["bid_price"])
        bidding = MaxAmountModel.objects.filter(pid_id=pid)
        for x in bidding:
            m_price = x.maxamount
        if price > m_price and price - m_price >= 100:
            bidding.update(maxamount=price)
            all_bid = MaxAmountModel.objects.all()
            BiddingModel(pid_id=pid, uid_id=data.uid, amount=price).save()
            return render(request, "usertemp/welcome.html", {"data": data, "buy": "buy", "allbid": all_bid})
        else:
            all_bid = MaxAmountModel.objects.all()
            messages.success(request, "You have to bid atleast more than 100 rupees from Product amount")
            return render(request, "usertemp/welcome.html", {"data": data, "buy": "buy", "allbid": all_bid})
    except:
        return redirect('login')


def bidding_info(request,pid):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        try:
            qs = BiddingModel.objects.filter(pid_id=pid)
            if qs:
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "bid_info": qs})
            else:
                messages.success(request, "No One Bid this Item till now .")
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
        except:
            messages.success(request, "No One Bid this Item till now .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def bid_Details(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        try:
            qs = BiddingModel.objects.filter(uid_id=data.uid)
            if qs:
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell", "bid_details": qs})
            else:
                messages.success(request, "You are not bidding any item till now .")
                return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
        except:
            messages.success(request, "You are not bidding any item till now .")
            return render(request, "usertemp/welcome.html", {"data": data, "sell": "sell"})
    except:
        return redirect('login')


def change_pswd(request):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        if request.method == "POST":
            old = request.POST.get("old")
            new = request.POST.get("new")
            confirm = request.POST.get("confirm")
            if data.password == old :
                if new == confirm:
                    UserModel.objects.filter(email=email).update(password=new)
                    messages.success(request, "Successfully changed your password")
                    return render(request,"usertemp/welcome.html", {"data": data,"change":"change"})
                else:
                    messages.success(request, "Enter same password for twice")
                    return redirect('change_pswd')
            else:
                messages.success(request,"You entered wrong password")
                return redirect('change_pswd')
        else:
            return render(request,"usertemp/welcome.html", {"data": data,"change":"change"})
    except:
        return redirect('login')


def bid_prices(request,pid):
    try:
        email = request.session["uemail"]
        data = UserModel.objects.get(email=email)
        qs = BiddingModel.objects.filter(pid_id=pid)
        if qs :
            return render(request, "usertemp/welcome.html", {"data": data, "buy": "buy","bid_prices":qs})
        else:
            all_bid = MaxAmountModel.objects.all()
            messages.error(request,"This Product is not Bid by anyone")
            return render(request, "usertemp/welcome.html", {"data": data, "buy": "buy","allbid": all_bid})
    except:
        return redirect('login')