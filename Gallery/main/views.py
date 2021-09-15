from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import post
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import CreateBlogPostForm, UpdateBlogPostForm

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=post.objects.filter(ImgName__icontains=q).order_by('-id')
    else:
        posts=post.objects.all().order_by('-id')
    paginator=Paginator(posts,1)
    page_num = request.GET.get('page',1)
    posts=paginator.page(page_num)
    return render(request,'main/home.html',{'posts':posts})

def search(request):
	query = request.GET['query']
	posts = post.objects.filter(ImgName__icontains=query).order_by('-id')
	return render(request,'main/home.html',{'posts':posts})


class PostListView(ListView):
	model = post
	template_name = "main/home.html"
	context_object_name = "posts"
	paginate_by = 9


class PostDetailView(DetailView):
	model = post


class PostCreateView(CreateView):
	model = post
	fields = ['ImgName','ImgURL','ImgDetails']

	def form_valid(self, form):
		return super().form_valid(form)

def create_blog_view(request):

	context = {}

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		form = CreateBlogPostForm()
	context['form'] = form
	return render(request, "main/create_blog.html", context)



class PostUpdateView(UpdateView):
	model = post
	fields = ['ImgURL','ImgDetails']

	def form_valid(self, form):
		return super().form_valid(form)



def edit_blog_view(request, *args, **kwargs):
	context = {}
	blog_post = get_object_or_404(post, pk=kwargs['pk'])

	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj

	form = UpdateBlogPostForm(
			initial = {
					"ImgName": blog_post.ImgName,
					"ImgURL": blog_post.ImgURL,
					"ImgDetails": blog_post.ImgDetails,
			}
		)

	context['form'] = form
	return render(request, 'main/edit_blog.html', context)

class PostDeleteView(DeleteView):
	model = post
	success_url = '/'
	
