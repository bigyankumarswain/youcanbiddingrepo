from django.db import models

class UserModel(models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="userImage/")
    status=models.CharField(max_length=10)


class ProductModel(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    minprice=models.FloatField()
    discription=models.CharField(max_length=300)
    status=models.CharField(max_length=10)
    image=models.ImageField(upload_to="productImage/")
    userinfo=models.ForeignKey(UserModel,on_delete=models.CASCADE)


class BiddingModel(models.Model):
    bidid=models.AutoField(primary_key=True)
    pid=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    uid=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)


class MaxAmountModel(models.Model):
    maid=models.AutoField(primary_key=True)
    pid=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    uid=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    maxamount=models.FloatField()
