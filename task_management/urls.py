
from django.contrib import admin
from django.urls import path
from tasks.views import home
from tasks.views import contact
from tasks.views import support

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home),
    path("Contact/", contact),
    path("support/", support)
]
