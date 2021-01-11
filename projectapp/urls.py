from django.urls import path
from articleapp.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView, ArticleListView
from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),

]