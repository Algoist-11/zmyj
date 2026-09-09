

"""
URL configuration for zmyj_arg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')



# 仅用于演示，视图函数一般写在views.py里

urlpatterns = [
    # path('admin/'.admin.site.urls),
    path('', index)  # 空字符串代表访问域名首页时运行，path(路径,视图函数)
]