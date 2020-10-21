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
			otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+uid+name+email+mobile+age+gender+city).int
			otp=str(otp)
			otp=otp.upper()[0:6]
			request.session['otp'] = otp
			UserData(
				User_ID = uid,
				User_Name = name,
				User_Email = email,
				User_Mobile = mobile,
				User_Gender = gender,
				User_Age = age,
				User_City = city
				).save()
			sendotp(otp, email)
			return redirect('/index/')
		else:
			dic = {'msg':'<h4 style="color:red;"><i class="fa fa-exclamation-triangle"></i> Account Already Exists!</h4>'}
			return redirect('/index/')
	else:
		return HttpResponse('Error')

@csrf_exempt
def verify_account(request):
	if request.method=='POST':
		id_ = request.POST.get('id')
		otp = request.POST.get('otp')
		session_otp = request.session['otp']
		if otp == session_otp:
			UserData.objects.filter(User_ID=id_).update(Status='Active')
			request.session['userid'] = id_
			return redirect('/index/')
		else:
			dic = {'id':id_}
			return render(request,'verify.html',dic)
def adminindex(request):
	return render(request,'adminpannel/index.html',{})
def adminlogin(request):
	return render(request,'adminpannel/login.html',{})
def admincustomerlist(request):
	return render(request,'adminpannel/customerlist.html',{})
def adminaddmenuitem(request):
	return render(request,'adminpannel/addmenuitem.html',{})
def changepassword(request):
	return render(request,'changepassword.html',{})
def login(request):
	return render(request,'login.html',{})
def wall(request):
	return render(request,'wall.html',{})
def changeprofilepic(request):
	return render(request,'changeprofilepic.html',{})