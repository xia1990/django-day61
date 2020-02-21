#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from django.shortcuts import HttpResponse,render,redirect
from app01 import models

def yimi(request):
    return HttpResponse("hello yimi!")

def xiaohei(request):
    return HttpResponse("hello xiaohei!")

def login(request):
    error_message=""
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email == "admin@163.com" and password == "123456":
            return redirect("http://luffycity.com")
        else:
            # return HttpResponse("登录失败！")
            error_message="邮箱或密码错误！"
    return render(request, "login.html",{"error":error_message})

def baobao(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    if email=="admin@163.com" and password=="1223456":
        return HttpResponse("登录成功!")
    else:
        return HttpResponse("登录失败！")

#显示所有用户
def user_list(request):
    #得到所有用户的信息
    ret=models.UserInfo.objects.all()
    # print(ret[0].id,ret[0].name)
    #返回用户信息
    return render(request,"user_list.html",{"user_list":ret})

def add_user(request):
    if request.method=="POST":
        #得到用户输入的用户名
        new_name=request.POST.get("name")
        #向数据库中添加新用户
        models.UserInfo.objects.create(name=new_name)
        #返回用户列表
        return redirect("/user_list/")
    #返回用户添加界面
    return render(request,"add_user.html")
