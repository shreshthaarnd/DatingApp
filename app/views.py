from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import *
from django.conf import settings
import uuid
import datetime
from app.models import *
from app.mailutil import *
from app.myutil import *
# Create your views here.
def index(request):
	dic = {'checksession':checksession(request),
			'data':UserData.objects.filter(Status='Active'),
			'pictures':UserPictureData.objects.all()}
	return render(request,'index.html',dic)
def about(request):
	return render(request,'about.html',{})
def blog(request):
	return render(request,'blog.html',{})
def contact(request):
	return render(request,'contact.html',{})
def room(request):
	return render(request,'room.html',{})
def single_blog(request):
	return render(request,'single-blog.html',{})
def single_rooms(request):
	return render(request,'single-room.html',{})
def verify(request):
	return render(request,'verify.html',{})
def dashboard(request):
	dic = {'data':UserData.objects.filter(User_ID=request.session['user_id'])[0],
			'picture':UserPictureData.objects.filter(User_ID=request.session['user_id'])[0]}
	return render(request,'dashboard.html',dic)

@csrf_exempt
def saveuser(request):
	if request.method == 'POST':
		if not UserData.objects.filter(User_Email=request.POST.get('email')).exists():
			name = request.POST.get('name')
			email = request.POST.get('email')
			mobile = request.POST.get('mobile')
			gender = request.POST.get('gender')
			age = request.POST.get('age')
			city = request.POST.get('city')
			u="U00"
			x=1
			uid = u+str(x)
			while UserData.objects.filter(User_ID=uid).exists():
				x=x+1
				uid=u+str(x)
			x=int(x)
			password=uuid.uuid5(uuid.NAMESPACE_DNS, uid+name+email+mobile+gender+age+city)
			password=str(password)
			password=password.upper()[0:8]
			UserData(
				User_ID = uid,
				User_Name = name,
				User_Email = email,
				User_Mobile = mobile,
				User_Gender = gender,
				User_Age = age,
				User_City = city,
				User_Password=password,
				).save()
			UserPictureData(
				User_ID = uid
				).save()
			sendconfirmation(email)
			dic = {'msg':'<h4 style="color:green;"><i class="fa fa-check"></i> We will contact you soon!</h4>'}
			return render(request,'index.html',dic)
		else:
			dic = {'msg':'<h4 style="color:red;"><i class="fa fa-exclamation-triangle"></i> Account Already Exists!</h4>'}
			return render(request,'index.html',dic)
	else:
		return HttpResponse('Error')

def adminindex(request):
	return render(request,'adminpannel/index.html',{})
def adminlogin(request):
	return render(request,'adminpannel/login.html',{})
def admincustomerlist(request):
	return render(request,'adminpannel/customerlist.html',{})
def adminaddmenuitem(request):
	return render(request,'adminpannel/addmenuitem.html',{})

@csrf_exempt
def adminlogincheck(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		if email == 'admin@dating.com' and password == '1234':
			request.session['admin'] = email
			return redirect('/adminindex/')
		else:
			dic = {'msg':'Incorrect Credentials'}
			return render(request,'adminpannel/login.html',dic)

def adminuserlist(request):
	try:
		aid = request.session['admin']
		dic = {'data':UserData.objects.all()}
		return render(request,'adminpannel/userlist.html',dic)
	except:
		return HttpResponse('404 Not Found')

def adminapproveuser(request):
	try:
		uid = request.GET.get('uid')
		obj = UserData.objects.filter(User_ID=uid)
		obj.update(Status='Active')
		sendpassword(obj[0].User_Email,obj[0].User_Password)
		return redirect('/adminuserlist/')
	except:
		return HttpResponse('404 Not Found')

@csrf_exempt
def checklogin(request):
	if request.method=='POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		if UserData.objects.filter(User_Email=email, User_Password=password).exists():
			request.session['user_id'] = UserData.objects.filter(User_Email=email)[0].User_ID
			return redirect('/index/')
		else:
			dic = {'msg':'<h4 style="color:red;"><i class="fa fa-exclamation-triangle"></i> Incorrect Account Credentials</h4>'}
			return render(request,'login.html',dic)
	else:
		return HttpResponse('404 Not Found')

def changepassword(request):
	dic = {'flag':False}
	return render(request,'changepassword.html',dic)
@csrf_exempt
def savepassword(request):
	if request.method=='POST':
		old=request.POST.get('old')
		new=request.POST.get('new')
		uid=request.session['user_id']
		if UserData.objects.filter(User_ID=uid,User_Password=old).exists():
			UserData.objects.filter(User_ID=uid).update(User_Password=new)
			dic={'flag':True,
			'msg':'<h4 style="color:green;"><i class="fa fa-check"></i> Password Changed Successfully!</h4>'}
			return render(request,'changepassword.html',dic)
		else:
			dic = {'flag':False,'msg':'<h4 style="color:red;"><i class="fa fa-exclamation-triangle"></i> Incorrect Old Password</h4>'}
			return render(request,'changepassword.html',dic)
	else:
		return HttpResponse('404 Not Found')

@csrf_exempt
def saveprofilepicture(request):
	if request.method=='POST':
		pic=request.FILES['picture']
		uid=request.session['user_id']
		UserPictureData.objects.filter(User_ID=uid).delete()
		UserPictureData(
			User_ID=uid,
			User_Pic=pic,
			).save()
		return redirect('/dashboard/')
	else:
		return HttpResponse('404 Not Found')
def logout(request):
	del request.session['user_id']
	return redirect('/index/')

def login(request):
	return render(request,'login.html',{})
def wall(request):
	try:
		users = UserData.objects.filter(Status='Active')
		picture = UserPictureData.objects.all()
		dic = {'userid':request.session['user_id'],'checksession':checksession(request),'users':users,'picture':picture}
		return render(request,'wall.html',dic)
	except:
		users = UserData.objects.filter(Status='Active')
		picture = UserPictureData.objects.all()
		dic = {'userid':'none','checksession':checksession(request),'users':users,'picture':picture}
		return render(request,'wall.html',dic)
	
def changeprofilepic(request):
	dic = {'checksession':checksession(request)}
	return render(request,'changeprofilepic.html',dic)

@csrf_exempt
def saveedit(request):
	if request.method=='POST':
		name=request.POST.get('name')
		mobile=request.POST.get('mobile')
		age=request.POST.get('age')
		city=request.POST.get('city')
		obj=UserData.objects.filter(User_ID=request.session['user_id'])
		obj.update(
				User_Name=name,
				User_Mobile=mobile,
				User_Age=age,
				User_City=city
				)
		return redirect('/dashboard/')
	else:
		return HttpResponse('404 Not Found')
def editinfo(request):
	dic = {'checksession':checksession(request),
			'data':UserData.objects.filter(User_ID=request.session['user_id'])[0]}
	return render(request,'editinfo.html',dic)
def adminchangesitemap(request):
	return render(request,'adminpannel/changesitemap.html',{})
def adminchangekeywords(request):
	return render(request,'adminpannel/changekeywords.html',{})
def adminchangediscription(request):
	return render(request,'adminpannel/changediscription.html',{})