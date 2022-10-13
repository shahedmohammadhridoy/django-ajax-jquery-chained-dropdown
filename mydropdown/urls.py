from django.contrib import admin
from django.urls import path
from dropdown.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('load-courses/', load_courses, name='ajax_load_courses'),
]
