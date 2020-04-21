"""autoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Site View
from home.views import (home_screen_view)
from blog.views import (blog_screen_view,post_screen_view)
from gallery.views import (gallery_screen_view, full_screen_view)
from contacts.views import (contact_screen_view)
from portfolio.views import (portfolio_screen_view)
from accounts.views import(sign_up_view,sign_in_view,logout_view)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home_screen_view, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', blog_screen_view, name='blog'),   
    path('gallery/', gallery_screen_view, name='gallery'),
    path('full_screen', full_screen_view, name='full_screen'),
    path('portfolio/', portfolio_screen_view, name='portfolio'),
    path('contacts/', contact_screen_view, name='contacts'),
    path('signup/', sign_up_view, name='sign_up'),
    path('signin/', sign_in_view, name='sign_in'),
    path('logout/', logout_view, name='logout'),
    path('result_search/', blog_screen_view, name='result_search'),
    path('<slug>/', post_screen_view, name='single_post'),
    path('category/', blog_screen_view, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
