from django.shortcuts import render
from .models import Post

# for handling the home page requests
def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

# for handling the about page requests
def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})
