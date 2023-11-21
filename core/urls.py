from django.urls import path

from .views import (
    ReviewCreateView,
    FeaturedListCreateView,
    BookRetrieveView,
    BookListView,
)

urlpatterns = [
    path('review/', ReviewCreateView.as_view()),
    path('featured/', FeaturedListCreateView.as_view()),
    path('book/<int:pk>/', BookRetrieveView.as_view()),
    path('book/', BookListView.as_view()),
]
