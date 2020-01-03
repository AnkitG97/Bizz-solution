from django.conf.urls import url

from . import views

app_name = 'wedding'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('products/', views.products, name='products')
]
