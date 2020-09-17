from django.conf.urls import url
from blogapp import views
urlpatterns = [
    url('login', views.userLogin),
]