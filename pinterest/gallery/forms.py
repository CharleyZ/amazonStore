from django import forms

#from .models import User


class UserForm(forms.Form):
	name = forms.CharField(label='User Name', max_length = 100)
	email = forms.EmailField(label='Email Address', max_length = 100)
	isSeller = forms.BooleanField(label='Is Seller',initial = False,required=False)
	password = forms.CharField(label='Enter Password', max_length = 100)
	repassword = forms.CharField(label='Re enter password',max_length = 100)	

class LoginForm(forms.Form):
	name = forms.CharField(label='User Name', max_length = 100)
	password = forms.CharField(label='Password', max_length = 100)



# class UserForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ('name', 'email','password','user_id','isSeller',)