from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import *
from django.conf import settings
import uuid
import datetime
from app.models import *
from app.mailutil import *
# Create your views here.
def index(request):
	return render(request,'index.html',{})
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
	return render(request,'dashboard.html',{})

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

def changepassword(request):
	return render(request,'changepassword.html',{})
