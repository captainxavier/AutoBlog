from django.shortcuts import render

#Blog Page.
def blog_screen_view(request):
    context = {}
    return render(request, 'blog/blog.html', context)