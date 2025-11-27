from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView, BlogPostCreateView, \
    BlogPostListView, BlogPostDetailView, BlogPostUpdateView, ProductCreateView, VersionCreateView, VersionListView, \
    ProductUpdateView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_details/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_details'),
    path('create/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('posts/', BlogPostListView.as_view(), name='list_blogpost'),
    path('posts_details/<int:pk>', BlogPostDetailView.as_view(), name='posts_details'),
    path('update_post/<int:pk>', BlogPostUpdateView.as_view(), name='update_post'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_details/<int:pk>/version_create', VersionCreateView.as_view(), name='version_create'),
    path('product_details/<int:pk>/version_list', VersionListView.as_view(), name='version_list'),
    path('product_details/<int:pk>/product_update', ProductUpdateView.as_view(), name='product_update'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail')
]
