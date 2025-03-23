from django.urls import path
from .views import sites_list, sites_detail

urlpatterns = [
    path('', sites_list, name='home'),
    path('<int:site_id>/', sites_detail, name='detail'),
]
