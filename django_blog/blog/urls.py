from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register_view, profile_view, profile_edit_view, CustomLogoutView
from .models import Post
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts
)
from taggit.views import TaggedObjectList

urlpatterns = [
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
    path("search/", search_posts, name="search-posts"),
    path("tags/<str:tag>/", TaggedObjectList.as_view(model=Post), name="posts-by-tag"),
]

