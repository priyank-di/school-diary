from django.urls import path, include
from rest_framework.authtoken import views

app_name = "api"

urlpatterns = [
    path('news/', include('api.news.urls', namespace="news")),
    path('timetable/', include('api.timetable.urls', namespace="timetable")),
    path('auth/', views.obtain_auth_token),
    path('ajax/', include('api.ajax.urls', namespace='ajax')),
    path('', include('api.diary.urls', namespace='diary')),
]
