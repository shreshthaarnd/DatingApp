from django.shortcuts import render

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