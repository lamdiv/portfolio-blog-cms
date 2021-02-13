from django.contrib import admin
from home.models import Project,ProjectImage,TaggedTechnologies,Blog,Categories,Comment

admin.site.register(TaggedTechnologies)

class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','preview','created','tag')
    list_filter = ('tag', 'created','technologies')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('created','tag')

    inlines = [ProjectImageAdmin]

    class Meta:
       model = Project

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created', 'publish', 'status')
    list_filter = ('status', 'publish', 'tags')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'created')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','blog', 'created', 'active',)
    list_editable = ('active',)
    list_filter = ('active', 'created',)
    search_fields = ('name', 'body',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('created',)

