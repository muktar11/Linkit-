'''
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]

'''

from django.urls import path
from .consumers import CoinConsumer

websocket_urlpatterns = [
    path('ws/coin/', CoinConsumer.as_asgi()),
]
