from django.views.generic import ListView
from .models import UserProfile, Chat, Message
from datetime import datetime

class HomeView(ListView):
    model = UserProfile
    template_name = 'home.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class ChatView(ListView):
    model = Chat
    template_name = 'messenger_app/chat.html'
    context_object_name = 'chats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class MessagesView(ListView):
    model = Message
    template_name = 'messenger_app/messages.html'
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


