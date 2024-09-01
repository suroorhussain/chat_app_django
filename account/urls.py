from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import account.views as account_views

urlpatterns = [
    path('signup/', account_views.SignupAPIView.as_view(), name='account_signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/<username>', account_views.ProfileUpdateView.as_view(), name='profile_update'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]