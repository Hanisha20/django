from django.urls import path
from . import views
app_name = 'accountApp'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view() , name = 'User_register'),
    # path('register2/', views.UserRegisterView2.as_view() , name = 'User_register2'),
    path('login/', views.UserLoginView.as_view() , name = 'User_login'),
    path('logout/', views.UserLogoutView.as_view() , name = 'User_logout'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view() , name = 'User_profile'),
    path('reset/', views.UserResetPasswordView.as_view() , name = 'Reset_password'),
    path('reset/done', views.UserResetPasswordDoneView.as_view() , name = 'passwordResetDone'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view() , name = 'password_reset_confirm'),
    path('confirm/complete', views.UserPasswordResetConfirmView.as_view() , name = 'password_reset_complete'),
    path('follow/<int:user_id>/', views.UserFollowView.as_view() , name = 'User_follow'),
    path('unfollow/<int:user_id>/', views.UserUnfollowView.as_view() , name = 'User_unfollow'),
]