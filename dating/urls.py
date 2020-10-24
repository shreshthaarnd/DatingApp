from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path('adminlogincheck/',adminlogincheck),
    path('adminuserlist/',adminuserlist),
    path('changepassword/',changepassword),
    path('adminapproveuser/',adminapproveuser),
    path('login/',login),
    path('wall/',wall),
    path('checklogin/',checklogin),
    path('savepassword/',savepassword),
    path('saveprofilepicture/',saveprofilepicture),
    path('logout/',logout),
    path('saveedit/',saveedit),
    path('editinfo/',editinfo),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
