## chat > views.py

from rest_framework import viewsets, permissions
from .models import Notice, ChatPost
from .serializers import NoticeSerializer, ChatPostSerializer
from .permissions import IsAuthorOrReadOnly

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ChatPostViewSet(viewsets.ModelViewSet):
    queryset = ChatPost.objects.all()
    serializer_class = ChatPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)