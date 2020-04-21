from django.contrib import admin
from blog.models import BlogPost, BlogPicture



class PostPictureInline(admin.TabularInline):
    model = BlogPicture
    fields = ['picture',]


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPictureInline,]    
    list_display = ('title', 'date_published', 'date_updated', 'author', 'super_featured', 'featured',)
    search_fields = ('title', 'author', 'date_updated', 'super_featured', 'featured')
    readonly_fields = ('date_published', 'date_updated',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(BlogPost, PostAdmin)
