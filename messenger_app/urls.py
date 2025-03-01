from django.urls import path
from . views import HomeView, ChatView, MessagesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chat/<str:username>', ChatView.as_view(), name='chat'),
    path('messages/<str:username>', MessagesView.as_view(), name='messages'),  # This is where you'll add the API endpoint for sending messages.  # For example, /messages/user1
]