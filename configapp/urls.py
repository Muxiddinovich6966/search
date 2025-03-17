from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('news_detail/<int:new_id>/', new_detail, name='news_detail'),
    path('search_news/', search_view, name='search_news'),
    path('categories/<int:category_id>/', categories, name='categories'),
    path('update_new/<int:new_id>/', new_update, name='update_new'),
    path('new_about/<int:new_id>/', new_about, name='new_about'),
    path('add_news/', news_add, name='news_add'),
    path('login', loginPage, name='login'),
    path('logout',logoutPage, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
