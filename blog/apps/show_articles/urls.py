from django.urls import path, re_path
from .views import ArticlesView

app_name = 'show_articles'

urlpatterns = [
    re_path('articles/(?P<article_id>.*)/$', ArticlesView.as_view(), name='articles'),
]
