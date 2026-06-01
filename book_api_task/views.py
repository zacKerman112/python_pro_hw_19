from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """
    here we made all the CRUD operations
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['genre', 'author', 'publication_year']
    search_fields = ['title', 'author']

    def get_permissions(self):
        """setting up the rights of users"""
        if self.action == 'destroy':
            return [IsAdminUser()]
        elif self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticated()]
        return [AllowAny()]