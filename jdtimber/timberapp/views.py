from django.shortcuts import render,redirect
from .models import InquiryModel,VeneerModel,DeckingModel,LumberModel,MoldingModel,AgedModel
from django.core.mail import send_mail
from django.conf import settings
from .forms import InquiryForm

# from django.core.mail import send_mail
# from django.conf import settings
from django.contrib import messages


# Create your views here.
def index(request):
	return render(request,'index.html')

def veneer(request):
	veneerlist = VeneerModel.objects.all()
	return render(request,'veneer.html',{"VeneerModel":veneerlist})

def decking(request):
	deckinglist = DeckingModel.objects.all()
	return render(request,'decking.html',{"DeckingModel":deckinglist})

def agedwood(request):
	agedlist = AgedModel.objects.all()
	return render(request,'agedwood.html',{"AgedModel":agedlist})

def moulding(request):
	mouldinglist = MoldingModel.objects.all()
	return render(request,'moulding.html',{"MoldingModel":mouldinglist})

def lumber(request):
	lumberlist = LumberModel.objects.all()
	return render(request,'lumber.html',{"LumberModel":lumberlist})


def contact(request):
	context = {
		"form":InquiryForm
	}
	return render(request,'contact.html',context)

def sendinjuiry(request):

	subject = 'hello, thank you message your advice'
	message = 'successful send message to email'
	email = settings.EMAIL_HOST_USER

	if request.method == 'POST':

		email = settings.EMAIL_HOST_USER
		# subject = request.POST['subject']
		# message = request.POST['message']

		send_mail(
			subject,
			message,
			email,
			['kokothet1994.2@gmail.com.com'],
			fail_silently=False
			)
		return redirect('index')




	# return redirect('index')

def report(request):
	inquirylist = InquiryModel.objects.all()
	return render(request,'reportdata.html',{"InquiryModel":inquirylist})