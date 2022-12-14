from django.urls import path
from .views import News, New, PostCreate, PostUpdate, PostDelete, Search, Articles

urlpatterns = [
    path('', News.as_view(), name='news'),
    path('<int:pk>', New.as_view(), name='new'),
    # path('create/', create_post),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', Search.as_view(), name='search'),
]
