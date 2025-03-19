from django.urls import path
from .views import HomeView, RoomView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:room_name>/<str:username>/', RoomView.as_view(), name='room')
]