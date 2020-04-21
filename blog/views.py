from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.db.models import Count, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.contenttypes.models import ContentType


from taggit.models import Tag

from accounts.models import Account
from blog.models import BlogPost, Category, BlogPicture
from comments.forms import CommentForm
from comments.models import Comments
from category.models import Category


BLOG_POST_PER_PAGE = 3
RESULT_POST_PER_PAGE = 17

#Category Count
def get_category_count():
    questSet = BlogPost \
            .objects \
            .values('categories__title','categories__id') \
            .annotate(Count('categories__title'))

    return questSet

#Blog Page.
def blog_screen_view(request):
    category_count = get_category_count()
    super_featured = BlogPost.objects.filter(super_featured=True).order_by('-date_published')[:3]
    blogPosts = BlogPost.objects.order_by('-date_published')
    recentPosts = BlogPost.objects.order_by('-date_published')[:4]
    # Pagination
    page = request.GET.get('page',1)
    blog_posts_paginator = Paginator(blogPosts, BLOG_POST_PER_PAGE)
    try:
	    blogPosts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
	    blogPosts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    except EmptyPage:
	    blogPosts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context = {
        'super_featured_posts':super_featured,
        'posts': blogPosts,
        'recent_posts': recentPosts,
        'categories': category_count,
    }
    return render(request, 'blog/blog.html', context)

# Single Post
def post_screen_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post_related = post.tags.similar_objects()[:3]
    app_url = request.get_full_path
    category_count = get_category_count()
    recentPosts = BlogPost.objects.order_by('-date_published')[:4]
    comments = post.comments
    initial_data = {
        'content_type': post.get_content_type,
        'object_id' : post.id,
    }
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.content_type = post.get_content_type
            com.object_id = post.id
            parent_obj = None
            try:
                parent_id = int(request.POST.get("parent_id"))
            except:
                parent_id = None
                
            if parent_id:
                parent_qs = Comments.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() ==1:
                    parent_obj = parent_qs.first()

            com.parent = parent_obj
            com.save()
            return HttpResponseRedirect(com.content_object.get_absolute_url())
        else:
            print('error')
    else:
        form = CommentForm()
   

    
    context = {
        'post': post,      
        'recent_posts': recentPosts,
        'categories': category_count,
        'post_url': app_url,
        'comments': comments,
        'comment_form': form,
        'related_posts':post_related,
    }
    return render(request, 'blog/post.html', context)


# Search Page
def search_screen_view(request):    
    query_set = BlogPost.objects.all()
    category_count = get_category_count()
    query = request.GET.get('q')
    if query:
        query_set = query_set.filter(
            Q(title__icontains=query) |
            Q(description_one__icontains=query) |
            Q(description_two__icontains=query)
        ).distinct()

    paginator = Paginator(query_set, RESULT_POST_PER_PAGE) # 6 posts per page
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'query_sets': posts,
        'categories':category_count,
    }  
    return render(request, 'blog/result_search.html', context)