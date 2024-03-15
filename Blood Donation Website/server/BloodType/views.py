from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import BloodType
from .forms import BloodTypeForm


class BloodTypesList(ListView):
    model = BloodType
    template_name = 'BloodType/bloodtypes_list.html'
    context_object_name = 'bloodtypes'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('type')
    
# fix csrf ond BloodTypeFormView
class BloodTypeFormView(FormView):
    template_name = 'BloodType/bloodtype_create.html'
    form_class = BloodTypeForm
    success_url = reverse_lazy('bloodtypes-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class BloodTypeUpdateView(UpdateView):
    model = BloodType
    template_name = 'BloodType/bloodtype_details.html'
    form_class = BloodTypeForm
    success_url = reverse_lazy('bloodtypes-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class BloodTypeDeleteView(DeleteView):
    model = BloodType
    success_url = reverse_lazy('bloodtypes-list')

    def form_valid(self, form):
        bloodtype_id = self.kwargs['pk']
        bloodtype = BloodType.objects.get(pk=bloodtype_id) 
        bloodtype.delete() 
        return super().form_valid(form)
    