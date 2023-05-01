#from django.conf.urls import url
from react import views
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    re_path(r'^$', views.githubproject, name='react/index'),
    #path('user/', views.user, name='user'),
    path('github/', views.githubproject, name='react/GitHub'),
    path('pullclick/', views.pull_table, name='react/pullclick'),
    path('labelsort/', views.labelsort, name='react/labelsort'),
    path('commentcat/', views.commentcat, name='react/commentcat'),
    path('userinfo/', views.graphAPI, name='react/userinfo/'),
    path('userinfo/<str:name>', views.graphAPI, name='react/userinfo/'),
    path('normalize/', views.normalize_API, name='react/normalize')


]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)