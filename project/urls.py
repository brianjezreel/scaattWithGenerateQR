"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from project import settings
from django.conf.urls.static import static
from myapp import HodViews, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo', views.showDemoPage),
    path('', views.showLoginPage),
    path('doLogin', views.doLogin),
    path('register', views.register),
    path('logout_user', views.logout_user),
    path('admin_home', HodViews.admin_home, name="admin_home"),
    path('add_student', HodViews.add_student, name='add_student'),
    path('add_student_save', HodViews.add_student_save),
    path('add_course_save', HodViews.add_course_save),
    path('add_course', HodViews.add_course, name="add_course"),
    path('scanner', HodViews.scanner, name="scanner"),
    path('viewusers', HodViews.viewusers),
    path('viewcourses/', HodViews.viewcourses, name='viewcourses'),
    path('deleteprofile/<int:id>', HodViews.deleteprofile),
    path('deletecourse/<int:id>', HodViews.deletecourse),
    path('editprofile/<int:id>', HodViews.editprofile),
    path('updateprofile/<int:id>', HodViews.updateprofile),
    path('createqrcode/<int:course_id>/', HodViews.createqrcode),
    path('showqrcode/<int:qr_code_id>/', HodViews.showqrcode, name='showqrcode'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
