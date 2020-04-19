"""Blog_Project URL Configuration

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
from django.urls import path,include
from App import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("news-event/",views.newsevent,name="newsevent"),
    path("contactus/",views.contactus,name="contactus"),
    path("video/",views.video,name="video"),
    path("blog/",views.blog,name="blog"),
    path("blog/<int:id>",views.blog_read,name="blog_read"),
    path("signup/",views.register,name="signup"),
    path("login/",views.user_login,name="login"),
    path("dashboard/",views.user_dashboard,name="dashboard"),
    path("logout/",views.user_logout,name="user_logout"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

