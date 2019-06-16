from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DetailView,
	DeleteView
)
from .models import Post, Note
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# old function based view
# def post_list(request):
# 	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	highlights = Post.objects.filter(highlight = True).order_by('published_date')
# 	note = Note.objects.all()
# 	context = {
# 		'posts':posts,
# 		'highlights':highlights,
# 		'note':note,
# 	}
# 	return render(request, 'blog/post_list.html', context)


class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/post_list.html'
	ordering = ['-published_date']
	#<app>/<model>_<viewtype.html>
	paginate_by = 5

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		# context['posts'] = Post.objects.filter(published_date__lte=timezone.now())
		context['highlights'] = Post.objects.filter(highlight = True)
		context['note'] = Note.objects.all()
		return context

class UserPostListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/user_posts.html'
	#<app>/<model>_<viewtype.html>
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-published_date')


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content', 'slug']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content', 'slug']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/blog_article.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['article'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		context['highlights'] = Post.objects.filter(highlight = True).order_by('-published_date')
		# context['postlink'] = Post.objects.get(slug=slug)
		context['note'] = Note.objects.all()
		context['posts'] = Post.objects.all()
		return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/blog'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


# Function Based View for details, changed above to a class based view
#
# def post_details(request, slug):
# 	# return HttpResponse(f'post_details for {slug}')
# 	article = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	highlights = Post.objects.filter(highlight = True).order_by('-published_date')
# 	postlink = Post.objects.get(slug=slug)
# 	note = Note.objects.all()
# 	posts = Post.objects.all()
# 	context = {
# 		'postlink':postlink,
# 		'posts':posts,
# 		'article':article,
# 		'highlights':highlights,
# 		'note':note,
# 		}
# 	return render(request, 'blog/blog_article.html', context)

def note_details(request, note):
	return HttpResponse(f'This is the notes for {note}')

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})