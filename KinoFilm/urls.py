from django.urls import path
from .views import *

urlpatterns = [
    path('', ContentList.as_view(), name='main'),
    path('category/<int:category_id>/', category_view, name='category'),
    path('content/<int:pk>/', ContentDetail.as_view(), name='content'),
    path('random/', random_movie, name='random_movie'),
    path('login/', user_login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration', registration_view, name='register'),
    path('search/', SearchContent.as_view(), name='search'),
    path('comment_save/<int:pk>/', comment_save_view, name='comment_save'),
    path('comment_delete/<int:pk>/', comment_delete, name='comment_delete'),
    path('profile/', profile_view, name='profile'),
    path('edit/profile/', edit_profile_view, name='edit_profile'),
    path('edit/account/', edit_account_view, name='edit_account')
]