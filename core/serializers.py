from django.db.models import Avg
from rest_framework import serializers

from authentication.models import User
from .models import Review, Featured, Book, Author, Genre


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'full_name']


class ReviewBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['book', 'user', 'rating', 'text']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ['user', 'rating', 'text']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    author = AuthorSerializer()
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'average_rating', 'publish_date']

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(average, 2) if average is not None else None


class BookDetailsSerializer(BookSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'publish_date',
                  'author', 'genre', 'average_rating', 'reviews']


class FeaturedCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Featured
        fields = ['id', 'book', 'user']
        read_only_fields = ['id']


class FeaturedSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Featured
        fields = ['id', 'book', 'user']
        read_only_fields = ['id']
