from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import InquiryModel,VeneerModel,DeckingModel,LumberModel,MoldingModel,AgedModel
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import InquiryForm

# from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.



def index(request):
	return render(request,'index.html')

def veneer(request):
	# veneerlist = VeneerModel.objects.all()
	return render(request,'veneer.html')

def decking(request):
	return render(request,'decking.html')

def agedwood(request):
	return render(request,'agedwood.html')

def moulding(request):
	return render(request,'moulding.html',)

def lumber(request):
	# lumberlist =
	return render(request,'lumber.html',)


def contact(request):
	context = {
		"form":InquiryForm
	}
	return render(request,'contact.html',context)

def sendinjuiry(request):
	name= request.POST.get('name','')
	business = request.POST.get('business', '')
	email_id = request.POST.get('email', '')
	phone = request.POST.get('phone', '')
	address = request.POST.get('address', '')
	subject = request.POST.get('subject', '')
	message = request.POST.get('message', '')
	message_form = (f'Name = {name}<br> Business : {business}<br> Phone : {phone}<br> Address : {address} <br> {message}')
	host_mai = settings.EMAIL_HOST_USER
	email = EmailMessage(subject, message_form,email_id,[host_mai])
	email.content_subtype = 'html'

	file = request.FILES['file']
	email.attach(file.name, file.read(), file.content_type)

	email.send()
	# return HttpResponse("OK, Success")
	return redirect('index')
	#mail form
	# subject = 'hello, thank you message your advice'
	# message = 'successful send message to email'
	# email = settings.EMAIL_HOST_USER
	#
	# if request.method == 'POST':
	#
	# 	email = settings.EMAIL_HOST_USER
	# 	send_mail(
	# 		subject,
	# 		message,
	# 		email,
	# 		['kokothet1994.2@gmail.com.com'],
	# 		fail_silently=False
	# 		)
	# 	return redirect('index')




	# return redirect('index')

def report(request):
	pass