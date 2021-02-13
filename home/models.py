from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase

from ckeditor_uploader.fields import RichTextUploadingField


############## Project ##################

class ProjectTechnology(TagBase):
    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")


class TaggedTechnologies(GenericTaggedItemBase):
    tag = models.ForeignKey(ProjectTechnology,on_delete=models.CASCADE,
                            related_name="%(app_label)s_%(class)s_items")


class Project(models.Model):

    Project_Type_CHOICES = [
    ('Personal','Personal'),
    ('Client','Client')
    ]

    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=300,unique=True)
    thumbnail = models.ImageField(upload_to="project/thumbnail")
    github = models.URLField(null=True,blank=True)
    tag = models.CharField(max_length=10,choices=Project_Type_CHOICES)
    preview = models.URLField(null=True,blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    technologies = TaggableManager(through=TaggedTechnologies,verbose_name='Technologies')

    def get_absolute_url(self):
        return reverse("home:project_detail",kwargs={'slug':self.slug})

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, related_name="images", on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'project/images/')
 
    def __str__(self):
        return self.project.title


############## Blogs ##################


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Categories(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=250,unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = RichTextUploadingField(external_plugin_resources=[(
        'youtube',
        '/static/js/ckeditor/youtube/',
        'plugin.js',
    )],)
    thumbnail = models.ImageField(upload_to="blogs/thumbnail")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    categories = models.ManyToManyField(Categories)
    tags = TaggableManager()
    objects = models.Manager() 
    published = PublishedManager()

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
     return self.title

    def get_absolute_url(self):
        return reverse("home:blog_detail",kwargs={'slug':self.slug})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
   
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog}'