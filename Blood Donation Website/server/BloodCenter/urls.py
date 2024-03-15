from django.urls import path
from BloodCenter import views as bloodcenter_views

urlpatterns = [
    path('', bloodcenter_views.BloodCentersList.as_view(), name='bloodcenters-list'),
    path('create', bloodcenter_views.BloodCenterFormView.as_view(), name='bloodcenter-create'),
    path('update/<int:pk>', bloodcenter_views.BloodCenterUpdateView.as_view(), name='bloodcenter-detail'),
    path('<int:pk>/delete', bloodcenter_views.BloodCenterDeleteView.as_view(), name='bloodcenter-delete'),
]

