from django.urls import path
from .views import sites_list, sites_detail, like_dislike, comment_like_dislike

urlpatterns = [
    path('', sites_list, name='home'),
    path('<int:site_id>/', sites_detail, name='detail'),
    path('site/<int:site_id>/<str:action>/', like_dislike, name='like_dislike'),
    path('comment/<int:comment_id>/<str:action>/', comment_like_dislike, name='comment_like_dislike'),
]
