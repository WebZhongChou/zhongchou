from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.template import loader
from datetime import *
# Create your views here.
def zhuce(request):
    if request.method == 'GET':
        Username = request.GET.get('usernamesignup')
        Password = request.GET.get('passwordsignup')
        user = Users.objects.filter(Username = Username)

        if user:
            return render(request, 'yonghu/index.html')
        else:
            user = Users(Username = Username, Password = Password)
            user.save()
            return render(request, 'yonghu/index.html')
        #TouXiang = request.POST.get('',null)
        
        #return render(request, 'yonghu/index.html#toregister')
def index(request):
    chanpins = Chanpin.objects.order_by('-hasSale')[:10]
    context = {'chanpins':chanpins,'nowTime':date.today()}
    return render(request, 'yonghu/index.html',context)
def denglu(request):
    if request.method == 'GET':
        Username = request.GET.get('username')
        Password = request.GET.get('password')
        users = Users.objects.filter(Username = Username)
        if users[0].Password == Password:
            return render(request, 'yonghu/index.html')
    return render(request, 'yonghu/index.html')
def raisePublic(request):
    return render(request, 'yonghu/raisePublic.html')
def raisePublicForm(request):
    if request.method == 'GET':
        Name = request.GET.get('usernamesignup')
        jieshao = request.GET.get('jieshao')
        TaocanName_1 = request.GET.get('taocanName_1')
        TaocanPrice_1 = request.GET.get('taocanPrice_1')
        Taocanjianjie_1 = request.GET.get('taocanContent_1')
        TaocanName_2 = request.GET.get('taocanName_2')
        TaocanPrice_2 = request.GET.get('taocanPrice_2')
        Taocanjianjie_2 = request.GET.get('taocanContent_2')
        TaocanName_3 = request.GET.get('taocanName_3')
        TaocanPrice_3 = request.GET.get('taocanPrice_3')
        Taocanjianjie_3 = request.GET.get('taocanContent_3')
        Price = request.GET.get('price')
        CreateTime = date.today()
        delta = timedelta(days=100)
        DueTime = CreateTime + delta
        chanpin = Chanpin(DueTime = DueTime,CreateTime = CreateTime,Name = Name,jieshao = jieshao,TaocanName_1 = TaocanName_1,TaocanPrice_1 = TaocanPrice_1,Taocanjianjie_1 = Taocanjianjie_1,TaocanName_2 = TaocanName_2,TaocanPrice_2 = TaocanPrice_2,Taocanjianjie_2 = Taocanjianjie_2,TaocanName_3 = TaocanName_3,TaocanPrice_3 = TaocanPrice_3,Taocanjianjie_3 = Taocanjianjie_3,Price= Price)
        chanpin.save()
        return render(request, 'yonghu/index.html')