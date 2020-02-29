from django.contrib import messages
from django.shortcuts import render, redirect
from .models import AdminModel
from userApp.models import UserModel
from adminApp.sms import sendSMS


def adminlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pswd = request.POST.get("pswd")
        try:
            data = AdminModel.objects.get(email=email,password=pswd)
            request.session["email"] = email
            return render(request,"admintemp/welcom.html",{"data":data})
        except:
            messages.success(request,"Invalid Email And Password")
            return redirect('admin_login')
    else:
        try:
            if request.session["email"]:
                email = request.session["email"]
                data = AdminModel.objects.get(email=email)
                return render(request, "admintemp/welcom.html", {"data": data})
            else:
                return render(request,"admintemp/login.html")
        except:
            return render(request, "admintemp/login.html")


def adminlogout(request):
    try:
        del request.session["email"]
        messages.success(request, "You Successfully Logged Out")
        return redirect('home')
    except:
        return redirect('admin_login')


def pending_reqst(request):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        try:
            qs = UserModel.objects.filter(status="pending")
            if qs:
                return render(request, "admintemp/welcom.html", {"pdata": qs, "data": data})
            else:
                messages = "There are no Pending Request"
                return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
        except:
            messages = "There are no Pending Request"
            return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
    except:
        return redirect('admin_login')


def approved_list(request):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        try:
            qs = UserModel.objects.filter(status="approved")
            if qs:
                return render(request, "admintemp/welcom.html", {"adata": qs, "data": data})
            else:
                messages = "There are no Approved List"
                return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
        except:
            messages = "There are no Approved List"
            return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
    except:
        return redirect('admin_login')


def approvePendingUser(request,uid):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        xxx = UserModel.objects.filter(uid=uid)
        name = ""
        cno = ""
        pswd = ""
        for x in xxx:
            name = x.name
            cno = x.contact
            email = x.email
            pswd = x.password
        xxx.update(status="approved")

        mess = "Hello Mr/Miss : " + name + ". Your Registration is Approved. You can login with your email :" + email + " and password :" + pswd
        # sendSMS(str(cno), mess)
        qs = UserModel.objects.filter(status="pending")
        if qs:
            return render(request, "admintemp/welcom.html", {"pdata": qs, "data": data})
        else:
            messages = "There are no Pending Request"
            return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
    except:
        return redirect('admin_login')


def declineUser(request,uid):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        xxx = UserModel.objects.filter(uid=uid)
        name = ""
        cno = ""
        for x in xxx:
            name = x.name
            cno = x.contact
        xxx.update(status="blocked")

        mess = "Hello Mr/Miss : " + name + ". Your acount is temporary blocked by Admin "
        # sendSMS(str(cno), mess)
        qs = UserModel.objects.filter(status="approved")
        if qs:
            return render(request, "admintemp/welcom.html", {"adata": qs, "data": data})
        else:
            messages = "There are no Approved List"
            return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
    except:
        return redirect('admin_login')


def decline_list(request):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        try:
            qs = UserModel.objects.filter(status="blocked")
            if qs:
                return render(request, "admintemp/welcom.html", {"ddata": qs, "data": data})
            else:
                messages = "There are no decline List"
                return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
        except:
            messages = "There are no decline List"
            return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
    except:
        return redirect('admin_login')


def approveDeclineUser(request,uid):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        xxx = UserModel.objects.filter(uid=uid)
        name = ""
        cno = ""
        pswd = ""
        for x in xxx:
            name = x.name
            cno = x.contact
            email = x.email
            pswd = x.password
        xxx.update(status="approved")

        mess = "Hello Mr/Miss : " + name + ". Your blocked account is Approved now . You can login with your email :" + email + " and password :" + pswd
        # sendSMS(str(cno), mess)
        qs = UserModel.objects.filter(status="blocked")
        if qs:
            return render(request, "admintemp/welcom.html", {"ddata": qs, "data": data})
        else:
            messages = "There are no Decline Request"
            return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})
    except:
        return redirect('admin_login')


def admmin_welcom(request):
    try:
        email = request.session["email"]
        data = AdminModel.objects.get(email=email)
        return render(request, "admintemp/welcom.html", {"data": data})
    except:
        return redirect('admin_login')


def delete_decline(request,uid):
    email = request.session["email"]
    data = AdminModel.objects.get(email=email)
    UserModel.objects.filter(uid=uid).delete()
    qs = UserModel.objects.filter(status="blocked")
    if qs:
        return render(request, "admintemp/welcom.html", {"ddata": qs, "data": data})
    else:
        messages = "There are no Decline Request"
        return render(request, "admintemp/welcom.html", {"msg": messages, "data": data})