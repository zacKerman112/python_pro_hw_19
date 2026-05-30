from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Book


class BookAPITests(APITestCase):
    
    def setUp(self):
        """setting up"""
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        
        self.book = Book.objects.create(
            title="Test book",
            author="Test author",
            genre="Fantasy",
            publication_year=2026
        )
        
        self.url_list = reverse('book-list')

    def test_get_all_books(self):
        """checking if user can see all the books"""
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """checking the creatin of book made by an authorised user"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        data = {
            "title": "New book",
            "author": "A famous author",
            "genre": "Detective",
            "publication_year": "2025"
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """checking if a non-authorised user is able to upload books"""
        data = {"title": "Forbidden book!"}
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)