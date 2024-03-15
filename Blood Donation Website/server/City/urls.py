from django.urls import path
from City import views as city_views

urlpatterns = [
    path('', city_views.CitiesList.as_view(), name='cities-list'),
    path('create', city_views.CityFormView.as_view(), name='city-create'),
    path('update/<int:pk>', city_views.CityUpdateView.as_view(), name='city-detail'),
    path('<int:pk>/delete', city_views.CityDeleteView.as_view(), name='city-delete'),
]

