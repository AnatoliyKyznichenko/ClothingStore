from django.urls import path
from .views import RegistrationView, GoogleLoginView, GithubLoginView, Authorized_User_Page, LogoutView, LoginUserView

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration_user'),
    path('google-login/', GoogleLoginView.as_view(), name='google_login'),
    path('github-login/', GithubLoginView.as_view(), name='github_login'),
    path('profile/', Authorized_User_Page.as_view(), name='profile_user'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('login/', LoginUserView.as_view(), name='login'),

]