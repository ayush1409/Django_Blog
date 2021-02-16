from django.shortcuts import render

# dummy posts
posts = [
	{
		'author': 'ayush',
		'title': 'Blog Post1',
		'content': 'Awesome',
		'date_posted' : '15-02-2021'
	},
	{
		'author': 'Tony',
		'title': 'Blog Post2',
		'content': 'Geek',
		'date_posted' : '15-02-2021'
	}
]
# for handling the home page requests
def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

# for handling the about page requests
def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})
