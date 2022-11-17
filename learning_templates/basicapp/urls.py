from django.urls import path, re_path
from basicapp import views

# template taggihg

app_name ='basicapp'

urlpatterns = [
    re_path(r'^relative/$',views.relative, name='relative'),
    re_path(r'^other/$', views.other, name='other')
]
