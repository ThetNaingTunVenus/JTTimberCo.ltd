from django import forms

class InquiryForm(forms.Form):
	name = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
	business = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Business Name'}))
	email = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
	phone = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}))
	address = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}))
	
	veneers = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Teak Veneer'}))
	decking = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Teak Decking'}))
	boards = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Teak Board or Lumber'}))
	flooring = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Moulding'}))
	skirtings = forms.CharField(max_length=200,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Aged Wood'}))