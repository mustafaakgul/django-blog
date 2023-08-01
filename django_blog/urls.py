"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
]





from django.contrib import admin
from django.urls import path, include

#from article.views import index
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    #path('detail/<int:id>', views.detail, name = "detail"),
    path('articles/', include("article.urls")),   #article grnce article icinde url bak article/create gelirse git article icine bak http://127.0.0.1:8000/articles/create
    path('user/', include("user.urls")),
    path('contact/', include("contact.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#yukarısı var
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from article.views import index
from article import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #redirect icin name kllnlmali
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('detail/<int:id>', views.detail, name = "detail"),
    #path('articles/deneme1', views.detail, name = "detail"),
    #eger bana article diye url gelirse farkli bir url yi dahil et articles/create gelirse ilk buraya gelr snra create olana
    path('articles/', include("article.url")),
    #user/login geldgnde digerine git
    path('user/', include("user.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    #redirect icin name kllnlmali
    path('main/', views.index, name = "index"),
    path('main/about/', views.about, name = "about"),
    path('detail/<int:id>', views.detail, name = "detail"),
    #path('articles/deneme1', views.detail, name = "detail"),
    #eger bana article diye url gelirse farkli bir url yi dahil et articles/create gelirse ilk buraya gelr snra create olana
    path('articles/', include("article.url")),
    #user/login geldgnde digerine git
    path('user/', include("user.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""