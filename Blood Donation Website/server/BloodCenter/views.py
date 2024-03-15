from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import BloodCenter
from .forms import BloodCenterForm


class BloodCentersList(ListView):
    model = BloodCenter
    template_name = 'BloodCenter/bloodcenters_list.html'
    context_object_name = 'bloodcenters'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    
# fix csrf ond BloodCenterFormView
class BloodCenterFormView(FormView):
    template_name = 'BloodCenter/bloodcenter_create.html'
    form_class = BloodCenterForm
    success_url = reverse_lazy('bloodcenters-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class BloodCenterUpdateView(UpdateView):
    model = BloodCenter
    template_name = 'BloodCenter/bloodcenter_details.html'
    form_class = BloodCenterForm
    success_url = reverse_lazy('bloodcenters-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class BloodCenterDeleteView(DeleteView):
    model = BloodCenter
    success_url = reverse_lazy('bloodcenters-list')

    def form_valid(self, form):
        bloodcenter_id = self.kwargs['pk']
        bloodcenter = BloodCenter.objects.get(pk=bloodcenter_id) 
        bloodcenter.delete() 
        return super().form_valid(form)
    