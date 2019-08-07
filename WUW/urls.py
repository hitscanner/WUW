"""WUW URL Configuration

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
import main.views
import accounts.views
import fullcalendar.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='index'),
    path('', main.views.ajax_index, name='ajax_index'),
    path('search/', main.views.search, name='search'),
    path('detail/<int:movie_id>', main.views.detail, name='detail'),
    path('ranking/', main.views.ranking, name='ranking'),
    path('tag/', main.views.tag, name='tag'),
    path('fullcalendar/', fullcalendar.views.fullcalendar, name='fullcalendar'),
    path('cart/<int:user_id>', main.views.cart, name='cart'),

    path('like/', main.views.like, name='like'),

    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
]
