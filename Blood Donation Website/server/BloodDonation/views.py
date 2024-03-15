from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import BloodDonation
from .forms import BloodDonationForm


class BloodDonationsList(ListView):
    model = BloodDonation
    template_name = 'BloodDonation/blooddonations_list.html'
    context_object_name = 'blooddonations'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('date')
    
# fix csrf ond BloodDonationFormView
class BloodDonationFormView(FormView):
    template_name = 'BloodDonation/blooddonation_create.html'
    form_class = BloodDonationForm
    success_url = reverse_lazy('blooddonations-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class BloodDonationUpdateView(UpdateView):
    model = BloodDonation
    template_name = 'BloodDonation/blooddonation_details.html'
    form_class = BloodDonationForm
    success_url = reverse_lazy('blooddonations-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class BloodDonationDeleteView(DeleteView):
    model = BloodDonation
    success_url = reverse_lazy('blooddonations-list')

    def form_valid(self, form):
        blooddonation_id = self.kwargs['pk']
        blooddonation = BloodDonation.objects.get(pk=blooddonation_id) 
        blooddonation.delete() 
        return super().form_valid(form)
    