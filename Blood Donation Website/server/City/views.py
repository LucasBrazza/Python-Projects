from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import City
from .forms import CityForm


class CitiesList(ListView):
    model = City
    template_name = 'City/cities_list.html'
    context_object_name = 'cities'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    
class CityFormView(FormView):
    template_name = 'City/city_create.html'
    form_class = CityForm
    success_url = reverse_lazy('cities-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class CityUpdateView(UpdateView):
    model = City
    template_name = 'City/city_details.html'
    form_class = CityForm
    success_url = reverse_lazy('cities-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('cities-list')

    def form_valid(self, form):
        city_id = self.kwargs['pk']
        city = City.objects.get(pk=city_id) 
        city.delete() 
        return super().form_valid(form)
    