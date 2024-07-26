from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
]