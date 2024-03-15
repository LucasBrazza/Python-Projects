from django.urls import path
from Person import views as person_views

urlpatterns = [
    path('', person_views.PersonsList.as_view(), name='persons-list'),
    path('create', person_views.PersonFormView.as_view(), name='person-create'),
    path('update/<int:pk>', person_views.PersonUpdateView.as_view(), name='person-detail'),
    path('<int:pk>/delete', person_views.PersonDeleteView.as_view(), name='person-delete'),
]

