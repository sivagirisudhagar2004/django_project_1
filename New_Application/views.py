from django.shortcuts import render
from django.http import HttpResponse
"""""
def home(request):
    return render(request,"home.html")

def register(resquest):
    name = resquest.POST['name']
    password = resquest.POST['password']
    address = resquest.POST['address']
    mail = resquest.POST['mail']
    return render(resquest,"output.html",{'Name':name,'Password':password,"Address":address, 'Mail':mail})
"""""
def home(request):
    return render(request,"home_1.html")
