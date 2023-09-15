from django.urls import path
from .views import index_view, kategori_view


app_name = "category"


urlpatterns = [
    path('', index_view, name="index"),
    path('<str:slug>', kategori_view),
]
