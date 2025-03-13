from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Asosiy sahifa
    path('news_detail/<int:new_id>/', new_detail, name='news_detail'),
    path('search_news/', search_view, name='search_news'),
    path('categories/<int:category_id>/', categories, name='categories'),
    path('update_new/<int:new_id>/', new_update, name='update_new'),
    path('new_about/<int:new_id>/', new_about, name='new_about'),
    path('add_news/', news_add, name='news_add'),
]
