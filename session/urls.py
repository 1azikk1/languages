from django.urls import path
from .views import create_session, get_session_value, delete_session_value, update_session_value, home

urlpatterns = [
    path('', home),
    path('create/session/', create_session),
    path('session/get/', get_session_value),
    path('session/delete/', delete_session_value),
    path('session/update/', update_session_value),
]
