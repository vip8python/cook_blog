from django.urls import path
from . import views
from .views import HomeListView

urlpatterns = [
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', HomeListView.as_view(), name='home'),
]
