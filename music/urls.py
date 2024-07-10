from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    MusicianCreateView, MusicianUpdateView, MusicianDeleteView,
    AlbumCreateView, AlbumUpdateView, AlbumDeleteView, SignUpView, CustomLoginView
)

urlpatterns = [
    path('musicians/create/', MusicianCreateView.as_view(), name='musician_create'),
    path('musicians/<int:pk>/edit/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('musicians/<int:pk>/delete/', MusicianDeleteView.as_view(), name='musician_delete'),
    path('albums/create/', AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name ='log_out'),
]