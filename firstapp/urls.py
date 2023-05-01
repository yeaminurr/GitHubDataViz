#from django.conf.urls import url
from firstapp import views
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    re_path(r'^$', views.githubproject, name='index'),
    #path('user/', views.user, name='user'),
    path('github/', views.githubproject, name='GitHub'),
    path('pullclick/', views.pull_table, name='pullclick'),
    path('labelsort/', views.labelsort, name='labelsort'),
    path('commentcat/', views.commentcat, name='commentcat'),
    path('userinfo/', views.graphAPI, name='firstapp/userinfo/'),
    path('userinfo/<str:name>', views.graphAPI, name='firstapp/userinfo/'),
    path('normalize/', views.normalize_API, name='firstapp/normalize')


]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)