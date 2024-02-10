from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('blog/', views.post_list, name='post-list'),
    path('blog/<int:post_id>', views.post_detail, name='post-detail'),
    path('blog/add', views.PostCreate.as_view(), name='post-create'),
    path('blog/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('blog/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
]