from django.urls import path
from .views import SignInView, SignUpView

urlpatterns = [
    path('',Test_bujoriView.as_view()),
    path('/in',SignInView.as_view()),
    path('/up',SignUpView.as_view()),
]