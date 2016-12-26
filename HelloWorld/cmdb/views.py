from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"}
]
def index(request):
    #request.POST
    #request.GET
    #return HttpResponse("HELLO WORLD ! ")
    if request.method=="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password", None)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
        #print(username, password)
        temp = {"user":username,"pwd":password}
        user_list.append(temp)
    return render(request, "index.html",{"data":user_list})