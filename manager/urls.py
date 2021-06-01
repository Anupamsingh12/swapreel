from django.urls import path
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home, name="home"),
    path('index',views.index, name="index"),
    path('home',views.home, name="home"),
    path('login',views.login, name="login"),
    path('forget_password',views.forget_password, name="forget_password"),
    path('logout',views.logout,name='logout'),
    path('find_friends',views.find_friends,name='find friends'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='profile'),
    path('post',views.post,name='profile'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
