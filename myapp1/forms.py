from django.forms import ModelForm
from myapp1.models import Mybooks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Books(ModelForm):
	class Meta:#returns fields
		model=Mybooks
		fields='__all__'
#from django.contrib.auth.models import User

class Myform(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','password1','password2','email']



