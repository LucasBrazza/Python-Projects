from django.urls import path
from BloodType import views as bloodtype_views

urlpatterns = [
    path('', bloodtype_views.BloodTypesList.as_view(), name='bloodtypes-list'),
    path('create', bloodtype_views.BloodTypeFormView.as_view(), name='bloodtype-create'),
    path('update/<int:pk>', bloodtype_views.BloodTypeUpdateView.as_view(), name='bloodtype-detail'),
    path('<int:pk>/delete', bloodtype_views.BloodTypeDeleteView.as_view(), name='bloodtype-delete'),
]

