from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import *

urlpatterns=[
    path('',index,name='home'),
    path('register/',register,name='register'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)