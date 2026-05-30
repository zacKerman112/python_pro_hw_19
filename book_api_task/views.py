from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['genre', 'author', 'publication_year']
    search_fields = ['title', 'author']
    
    def get_permissions(self):
        """getting permissions and checking if user has any privilages"""
        if self.action == 'destroy':
            return [IsAdminUser()]
        elif self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticated()]
        return [AllowAny()]