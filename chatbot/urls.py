from django.urls import path
from . import views

urlpatterns = [
    path('', views.furia_chatbot, name='chat'),
    path('chat/ajax/', views.furia_chatbot_ajax, name='chat_ajax'),
]
