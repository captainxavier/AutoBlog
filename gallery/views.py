from django.shortcuts import render

# gallery
def gallery_screen_view(request):
    context = {}
    return render(request, 'gallery/gallery.html', context)


# Full page slide show
def full_screen_view(request):
    context = {}
    return render(request, 'gallery/gallery_full_screen.html', context)

