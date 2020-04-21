from django.shortcuts import render

from accounts.models import Account
from blog.models import BlogPost



def home_screen_view(request):

    super_featured = BlogPost.objects.filter(super_featured=True).order_by('-date_published')[:3]    
    featured = BlogPost.objects.filter(featured=True).order_by('-date_published')[:3]  
    latest = BlogPost.objects.order_by('-date_published')[:3]
    accounts = Account.objects.all()
    context = {
         'super_featured_posts':super_featured,        
        'featured_blog_posts': featured,
        'latest_posts': latest,
        'accounts': accounts,
    }

    return render(request, 'home/index.html', context)