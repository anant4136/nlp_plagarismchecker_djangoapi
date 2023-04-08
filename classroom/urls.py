from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views
from classroom import views

urlpatterns = [
    path('register/', views.registerUser.as_view(), name='register'),
    path('users/<int:pk>', views.UsersView.as_view(), name='user'),
    path('users/change-password',
         views.ChangePasswordView.as_view(), name='change-password'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('submit_paper/', views.Submit_paper.as_view()),
    #     path('store/<int:pk>/', views.BookDetail.as_view()),
    path('check_result/', views.Check_result.as_view()),
    path('token/', auth_views.obtain_auth_token)
]
