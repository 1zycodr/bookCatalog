from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Review, Featured, Book
from .serializers import (
    ReviewBaseSerializer,
    FeaturedSerializer,
    FeaturedCreateSerializer,
    BookSerializer,
    BookDetailsSerializer,
)


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewBaseSerializer
    permission_classes = [IsAuthenticated]


class BookListView(ListAPIView):
    queryset = Book.objects.prefetch_related(
        'author', 'genre', 'reviews').all()
    serializer_class = BookSerializer
    filterset_fields = {
        'genre': ['exact'],
        'author': ['exact'],
        'publish_date': ['gte', 'lte'],
    }


class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.prefetch_related('author', 'genre',
                                             'reviews', 'reviews__user').all()
    serializer_class = BookDetailsSerializer


class FeaturedListCreateView(ListCreateAPIView):
    queryset = Featured.objects.prefetch_related('book', 'book__reviews').all()
    permission_classes = [IsAuthenticated]
    filterset_fields = ['user__id']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FeaturedCreateSerializer
        return FeaturedSerializer
