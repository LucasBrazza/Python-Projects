from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import Person
from .forms import PersonForm


class PersonsList(ListView):
    model = Person
    template_name = 'Person/persons_list.html'
    context_object_name = 'persons'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    
# fix csrf ond PersonFormView
class PersonFormView(FormView):
    template_name = 'Person/person_create.html'
    form_class = PersonForm
    success_url = reverse_lazy('persons-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'Person/person_details.html'
    form_class = PersonForm
    success_url = reverse_lazy('persons-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('persons-list')

    def form_valid(self, form):
        person_id = self.kwargs['pk']
        person = Person.objects.get(pk=person_id) 
        person.delete() 
        return super().form_valid(form)
    