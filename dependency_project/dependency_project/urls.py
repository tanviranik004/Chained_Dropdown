
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from myapp.views import dependantfield
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', dependantfield,name='dependantfield'),
    
]

