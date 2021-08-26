from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.db.models import Count
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView,View
from django.conf import settings

from .models import Project,ProjectImage,Blog,Comment,Categories
from .forms import CommentForm

from taggit.models import Tag

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio.html'
    context_object_name = 'projects'

class PortfolioDetailView(DetailView):
    model = Project
    template_name = 'portfolio-detail.html'
    context_object_name = 'project'


class BlogView(ListView):
    model = Blog
    paginate_by = 8
    template_name = 'blogs.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Blog.published.all()
        if self.kwargs.get('tag_slug'):
            tag = get_object_or_404(Tag,slug=self.kwargs.get('tag_slug'))
            queryset = queryset.filter(tags__in=[tag])
            context['tag'] = tag.name
        
        if self.kwargs.get('categories'):
            categories = get_object_or_404(Categories,slug=self.kwargs.get('categories'))
            queryset = queryset.filter(categories__in=[categories])
            context['categories'] = categories.title

        context['blogs'] = queryset
        
        return context



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-detail.html'

    def get_object(self):
        obj = get_object_or_404(Blog,slug=self.kwargs.get('slug'),status='published')
        return obj

    def comment_posted(self,boolean=False):
        return boolean

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        tags_list = blog.tags.values_list('id',flat=True)
        similar_blogs = Blog.published.filter(tags__in=tags_list).exclude(id=blog.id)
        similar_blogs = similar_blogs.annotate(tags_num=Count('tags')).order_by('-tags','-publish')[:2]

        comments = blog.comments.filter(active=True).order_by('-created')

        context['blog'] = blog
        context['similars'] = similar_blogs
        context['form'] = CommentForm()
        context['comments'] = comments
        return context

    def post(self,request,**kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            blog = self.get_object()
            form.instance.blog = blog
            form.save() 
            messages.success(request, 'Your comment has been added')
            return redirect(reverse("home:blog_detail", kwargs={'slug': blog.slug}))


class SearchView(View):
    
    def get(self,request):
        query = None
        results = []
        if 'q' in request.GET:
            query = request.GET.get('q')
            results = Blog.published.annotate(search=SearchVector('title','body')).filter(search=query)
        return render(request,'search.html',{'query':query,'results':results})

class ContactView(TemplateView):
    template_name = "contact.html"
    def post(self,request,**kwargs):
            email = self.request.POST['email']
            name = self.request.POST['name']
            message = self.request.POST['message']
            send_mail(f'{name} sent mail through lamdiv',
                      f'{message}\n\nname: {name} \nemail: {email}',
                      settings.EMAIL_HOST_USER,
                      ['your email'],fail_silently=False)
            messages.success(request, 'Your message has been sent')
            return redirect(reverse("home:contact"))