from django.urls import path
from webs.views import index

urlpatterns = [
    path("websocket/", index, name="index"),
]
