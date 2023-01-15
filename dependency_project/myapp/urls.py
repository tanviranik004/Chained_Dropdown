from django.conf.urls import url
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns 


urlpatterns = [
    
    path('get_card/', views.get_card, name='get_card'),

    
]