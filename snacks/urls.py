from django.urls import path
from .views import SnackListView, SnackDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snacklist/', SnackListView.as_view(), name='snack_list'),
    path('snacklist/<int:pk>', SnackDetailView.as_view(), name='snack_detail')
]
