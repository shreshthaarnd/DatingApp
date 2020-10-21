from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('about/', about),
    path('blog/', blog),
    path('contact/', contact),
    path('room/', room),
    path('single-blog/', single_blog),
    path('single-room/', single_rooms),
    path('saveuser/', saveuser),
    path('verify/', verify),

    path('dashboard/',dashboard),
    path('adminindex/',adminindex),
    path('adminlogin/',adminlogin),
    path('admincustomerlist/',admincustomerlist),
    path('adminaddmenuitem/',adminaddmenuitem),
    path('changepassword/',changepassword),
    path('login/',login),
    path('wall/',wall),

    path('verify_account/', verify_account),

]