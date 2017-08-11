from . import views
from django.conf.urls import  include, url, RegexURLPattern
from chart import views

urlpatterns = [
    url(r'^',views.CategoryView.as_view()),
]