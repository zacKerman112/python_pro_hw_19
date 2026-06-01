from django_filters import rest_framework as django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    """filtering all the books by name, author, publication year and genre"""
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    
    publication_year = django_filters.NumberFilter(field_name='publication_year')
    genre = django_filters.CharFilter(field_name='genre')    
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre']