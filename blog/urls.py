from django.urls import path
from . import views
from . views import (
	PostListView,
	PostCreateView,
	PostUpdateView,
	PostDetailView,
	PostDeleteView,
    UserPostListView
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='detail'),
    path('posts/<str:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<str:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('note/<int:note>/', views.note_details, name='note'),
]
