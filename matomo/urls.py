#from django.conf.urls import url
from matomo import views
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    re_path(r'^$', views.githubproject, name='matomo/index'),
    #path('user/', views.user, name='user'),
    path('github/', views.githubproject, name='matomo/GitHub'),
    path('pullclick/', views.pull_table, name='matomo/pullclick'),
    path('labelsort/', views.labelsort, name='matomo/labelsort'),
    path('commentcat/', views.commentcat, name='matomo/commentcat'),
    path('userinfo/', views.graphAPI, name='matomo/userinfo/'),
    path('userinfo/<str:name>', views.graphAPI, name='matomo/userinfo/'),
    path('normalize/', views.normalize_API, name='matomo/normalize')


]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)