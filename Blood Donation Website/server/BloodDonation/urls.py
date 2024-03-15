from django.urls import path
from BloodDonation import views as blooddonation_views

urlpatterns = [
    path('', blooddonation_views.BloodDonationsList.as_view(), name='blooddonations-list'),
    path('create', blooddonation_views.BloodDonationFormView.as_view(), name='blooddonation-create'),
    path('update/<int:pk>', blooddonation_views.BloodDonationUpdateView.as_view(), name='blooddonation-detail'),
    path('<int:pk>/delete', blooddonation_views.BloodDonationDeleteView.as_view(), name='blooddonation-delete'),
]

