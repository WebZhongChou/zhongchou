from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.template import loader
from datetime import *
from django.http import HttpResponseRedirect
import rsa
#from Crypto.Cipher import PKCS1_v1_5
#from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import re
from django.contrib.sessions.backends.db import SessionStore
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
        
        #return renderS(request, 'yonghu/index.html#toregister')
def index(request):
    chanpinList = []
    with open('public.pem') as publickfile:
            p = publickfile.read()
            pubkey = rsa.PublicKey.load_pkcs1(p)
            #request.session["pubkey"] = pubkey

    chanpins = Chanpin.objects.order_by("-hasSale")[:10]
    for chanpin in chanpins:

        data = {"ChanpinID":chanpin.ChanPinID,"hasSale":chanpin.hasSale,"Name":chanpin.Name,"picture":chanpin.picture,"hasComplete":(chanpin.hasSale/chanpin.Price)*100,"lastTime":(chanpin.DueTime.replace(tzinfo=None)-datetime.today().replace(tzinfo=None)).days}
        chanpinList.append(data)
    n = '%x' % pubkey.n
    e = '%x' % pubkey.e
    context = {"data":chanpinList,"pubkeye":e,"pubkeyn":n}
    return render(request, 'yonghu/index.html',context)
def denglu(request):
    if request.method == 'GET':
        Username = request.GET.get('username')
        Password = request.GET.get('password')



        try:
            users = Users.objects.filter(Username = Username)
            DataBasePass = users[0].Password
            mk = open('private.pem','r')
            privkey = RSA.importKey(mk.read())
            ciphertext = ''.join([chr(int(x, 16)) for x in re.findall(r'\w\w', DataBasePass)])
            plaintext = rsa.decrypt(ciphertext, privkey)
            Password = rsa.decrypt(Password, privkey)
            if plaintext == Password:
                userID = users[0].UserID
                request.session["userID"] = userID
                return HttpResponseRedirect('/index#')
        except Exception,e:
            return HttpResponseRedirect('/index#')
    return HttpResponseRedirect('/index#')
def raisePublic(request):
    if request.method == 'GET':
        UserID  = request.session.get("userID",None)
        if UserID == None:
            return HttpResponseRedirect('/index#tologin')
        return render(request, 'yonghu/raisePublic.html')
def raisePublicForm(request):
    if request.method == 'GET':
        context= {}
        try:
            Name = request.GET.get('usernamesignup')
            jieshao = request.GET.get('jieshao')
            UserID  = request.session.get("userID",None)
            if UserID == None:
                return HttpResponseRedirect('/index#tologin')
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
            picture = request.GET.get('picture')

            delta = timedelta(days=100)
            DueTime = CreateTime + delta
            chanpin = Chanpin(picture= picture,hasSale=0,UserID= UserID,DueTime = DueTime,CreateTime = CreateTime,Name = Name,jieshao = jieshao,TaocanName_1 = TaocanName_1,TaocanPrice_1 = TaocanPrice_1,Taocanjianjie_1 = Taocanjianjie_1,TaocanName_2 = TaocanName_2,TaocanPrice_2 = TaocanPrice_2,Taocanjianjie_2 = Taocanjianjie_2,TaocanName_3 = TaocanName_3,TaocanPrice_3 = TaocanPrice_3,Taocanjianjie_3 = Taocanjianjie_3,Price= Price)
            chanpin.save()
        except Exception,e:
            return HttpResponseRedirect('/index#')
        return HttpResponseRedirect('/index#')

def getPublic(request):
    if request.method == 'GET':
        ChanpinID = request.GET.get('chanpinID')
        commentNum = 0
        pinglunList = []
        try:
            pingluns = Pinglun.objects.filter(ChanPinID = ChanpinID)
            commentNum = len(pingluns)

            for pinglun in pingluns:
                data = {}
                userID = pinglun.UserID
                user = Users.objects.filter(UserID = userID)
                username = user[0].Username
                data['username'] = username
                data['content']=  pinglun.Content
                data['time']=  pinglun.Time.replace(tzinfo=None)
                pinglunList.append(data)
        except Exception,e:
            print e
        try:

            chanpin = Chanpin.objects.get(ChanPinID = ChanpinID)
            name = chanpin.Name
            picture = chanpin.picture
            jieshao = chanpin.jieshao
            taocanName_1 = chanpin.TaocanName_1
            taocanPrice_1 = chanpin.TaocanPrice_1
            taocanjianjie_1 = chanpin.Taocanjianjie_1
            taocanName_2 = chanpin.TaocanName_2
            taocanPrice_2 = chanpin.TaocanPrice_2
            taocanjianjie_2 = chanpin.Taocanjianjie_2
            taocanName_3 = chanpin.Taocanjianjie_3
            taocanPrice_3 = chanpin.TaocanPrice_3
            taocanjianjie_3 = chanpin.Taocanjianjie_3
            price = chanpin.Price
            hasSale = chanpin.hasSale
            createTime = chanpin.CreateTime
            dueTime = chanpin.DueTime
            context = {"pinglunList":pinglunList,"commentNum":commentNum,"chanpinID":ChanpinID,"name":name,"picture":picture,"jieshao":jieshao,"taocanName_1":taocanName_1,"taocanPrice_1":taocanPrice_1,"taocanjianjie_1":taocanjianjie_1,"taocanName_2":taocanName_2,"taocanPrice_2":taocanPrice_2,"taocanjianjie_2":taocanjianjie_2,"taocanName_3":taocanName_3,"taocanPrice_3":taocanPrice_3,"taocanjianjie_3":taocanjianjie_3,"price":price,"hasSale":hasSale,"createTime":createTime,"dueTime":dueTime}
        except Exception,e:
            return HttpResponseRedirect('/index#id')
        return render(request, 'yonghu/goods.html',context)
def buyPublic(request):
    if request.method == 'GET':
        ChanpinID = request.GET.get('chanpinID')
        taocan = request.GET.get('taocan')
        UserID  = request.session.get("userID",None)
        if UserID == None:
            return HttpResponseRedirect('/index#tologin')
        chanpin = Chanpin.objects.get(ChanPinID = ChanpinID)
        ChanpinName = chanpin.Name
        sale = 0
        if int(taocan)  ==1:
            sale = chanpin.TaocanPrice_1
        elif int(taocan) ==2:
            sale = chanpin.TaocanPrice_2
        else:
            sale = chanpin.TaocanPrice_3
        try:
            if chanpin.hasSale + sale < chanpin.Price:
                chanpin.hasSale = chanpin.hasSale+sale
                chanpin.save()
                newBuychanpin = buyChanpin(ChanpinName=ChanpinName,ChanpinID=ChanpinID,UserID=UserID,price=sale)
                newBuychanpin.save()

                return HttpResponseRedirect('/index#id456')
        except Exception,e:
            return HttpResponseRedirect('/index#id123')
    return HttpResponseRedirect('/index#id')

def comment(request):
    if request.method == 'GET':
        ChanpinID = request.GET.get('chanpinID')
        UserID  = request.session.get("userID",None)
        content = request.GET.get('content')
        if UserID == None:
            return HttpResponseRedirect('/index#tologin')
        try:
            newcomment = Pinglun(UserID=UserID,ChanPinID = ChanpinID,Content=content,Time=datetime.now())
            newcomment.save()
        except Exception,e:
            return HttpResponseRedirect('/index#id123')
    return HttpResponseRedirect('/getPublic?chanpinID='+str(ChanpinID))
