"""NewsITT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from NewsV1.views import index
from NewsV1.views import registration
from NewsV1.views import homePage
from NewsV1.views import search
from NewsV1.views import cards
from NewsV1.views import newshome
from NewsV1.views import User
from NewsV1.views import subscription
from NewsV1.views import payment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('registrationPage.html/',registration),
    path('registrationPage.html/homePage.html',homePage),
    path('registrationPage.html/Subscription.html',subscription),
    path('registrationPage.html/User.html',User),
    path('homePage.html/',homePage),
    path('homePage.html/',search),
    path('index.html/',newshome),
    path('cards.html/',cards),
    path('cards.html/homePage.html',homePage),
    path('cards.html/User.html',User),
    path('cards.html/Subscription.html',subscription),
    path('cards.html/homePage.html/User.html',User),
    path('cards.html/payments.html',payment),
    path('registrationPage.html/payments.html',payment),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
