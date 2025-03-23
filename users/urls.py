from django.urls import path
from django.conf import settings
from users.views import UserCreateView, UserLoginView, LogoutView, ProfileView, ProfileEditView
from django.conf.urls.static import static
urlpatterns = [
    path('register/',UserCreateView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit/',ProfileEditView.as_view(),name='edit_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)