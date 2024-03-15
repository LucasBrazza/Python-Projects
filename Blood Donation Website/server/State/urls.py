from django.urls import path
from State import views as state_views

urlpatterns = [
    path('', state_views.StatesList.as_view(), name='states-list'),
    path('create', state_views.StateFormView.as_view(), name='state-create'),
    path('update/<int:pk>', state_views.StateUpdateView.as_view(), name='state-detail'),
    path('<int:pk>/delete', state_views.StateDeleteView.as_view(), name='state-delete'),
]

