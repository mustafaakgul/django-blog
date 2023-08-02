from django.urls import path
from . import views


app_name = "articles"


urlpatterns = [
    path('', views.list_articles, name="list_articles"),
    path('create/', views.create_article, name = "create_article"),
    path('detail/<int:id>', views.get_article, name="get_article"),
    path('update/<int:id>', views.update_article, name="update_article"),
    path('delete/<int:id>', views.delete_article, name="delete_article"),
]
