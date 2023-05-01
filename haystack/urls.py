#from django.conf.urls import url
from haystack import views
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    re_path(r'^$', views.githubproject, name='haystack/index'),
    #path('user/', views.user, name='user'),
    path('github/', views.githubproject, name='haystack/GitHub'),
    path('pullclick/', views.pull_table, name='haystack/pullclick'),
    path('labelsort/', views.labelsort, name='haystack/labelsort'),
    path('commentcat/', views.commentcat, name='haystack/commentcat'),
    path('userinfo/', views.graphAPI, name='haystack/userinfo/'),
    path('userinfo/<str:name>', views.graphAPI, name='haystack/userinfo/'),
    path('normalize/', views.normalize_API, name='haystack/normalize')


]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)