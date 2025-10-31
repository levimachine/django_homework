from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView2, ProductDetailView, ProductListView, BlogPostCreateView, \
    BlogPostListView, BlogPostDetailView, BlogPostUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView2.as_view(), name='products'),
    path('product_details/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('create/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('posts/', BlogPostListView.as_view(), name='list_blogpost'),
    path('posts_details/<int:pk>', BlogPostDetailView.as_view(), name='posts_details'),
    path('update_post/<int:pk>', BlogPostUpdateView.as_view(), name='update_post'),
]
