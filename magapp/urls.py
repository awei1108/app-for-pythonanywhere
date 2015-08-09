
from django.cong.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
