from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account has been created. You can able to Login Now!')
			return redirect('login')
	else: 
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')	
	# note: for only displaying the user name, we don't need a context

# Create your views here.
