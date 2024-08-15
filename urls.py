from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [  
    path('',views.index,name="login"),
    path('login',views.index,name="login"),
    path('home',views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    path('signup',views.signup,name="signup"),
    path('logout',views.Logout,name="logout"),
]

if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)