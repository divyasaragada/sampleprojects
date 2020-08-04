from django.shortcuts import render,redirect
from myapp1.forms import Myform,Books

from django.http import HttpResponse
from django.core.mail import send_mail
from BookBoom.settings import EMAIL_HOST_USER

from myapp1.models import Mybooks
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method=="POST":
		data=Myform(request.POST)
		if data.is_valid():
			data.save()
			return redirect('login')
	form=Myform()
	return render(request,'myapp1/register.html',{'form':form})


	
		#return HttpResponse("check your email")
		#data=UserForm(request.POST)
		#if data.is_valid():
		#	data.save()
		#	return HttpResponse("Registered Successfully..!!!")


#pp1/login.html',{'form':form})



def home(req):
	return render(req,'myapp1/home.html')
# Create your views here.
@login_required
def addbook(req):
	if  req.POST:
		data=Books(req.POST,req.FILES)
		if data.is_valid():
			data.save()
			return redirect("showbooks")
	form=Books()
	return render(req,'myapp1/addbook.html',{'form':form})

@login_required	
def showbooks(req):
	data=Mybooks.objects.all()
	
	return render(req,'myapp1/showbook.html',{'data':data})

def edit(req,id):
	data=Mybooks.objects.get(id=id)
	if req.method=="POST":
		form=Books(req.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/home')

	form=Books(instance=data)
	return render(req,'myapp1/edit.html',{'data':data,'info':form})
def delete(req,id):
	data=Mybooks.objects.get(id=id)
	if req.method=="POST":
		data.delete()
		return redirect("showbooks")
	return render(req,"myapp1/msg.html",{'info':data})


