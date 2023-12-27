from django.urls import path
from .views import RegisterView, LoginView
urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name="sign-up"),
    path('login/', LoginView.as_view(), name="login"),
]
