"""TodoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from todo import views as v

urlpatterns = [
    url(r'^$',v.home),
    url('success/',v.home),
    url('failure/', v.failure),
    url(r'^complete/', v.mark_complete),
    url(r'^incomplete/', v.mark_incomplete),
    url('delete/', v.delete),
    url('new/', v.add),
    url('admin/', admin.site.urls),
]
