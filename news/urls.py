from django.urls import path
from .views import news, news_detail, news_new, news_edit, news_delete, tag_detail_view

urlpatterns = [
    path('', news, name='all_news'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('new/', news_new, name='news_new'),
    path('<int:pk>/edit/', news_edit, name='news_edit'),
    path('<int:pk>/delete/', news_delete, name='news_delete'),
    path('tag/<int:pk>/', tag_detail_view, name='news_by_tag'),
]
