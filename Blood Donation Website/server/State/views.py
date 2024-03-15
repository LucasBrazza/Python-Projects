from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import State
from .forms import StateForm


class StatesList(ListView):
    model = State
    template_name = 'State/states_list.html'
    context_object_name = 'states'
    paginate_by = 6
    
    # @api_view(['GET'])
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    
# fix csrf ond StateFormView
class StateFormView(FormView):
    template_name = 'State/state_create.html'
    form_class = StateForm
    success_url = reverse_lazy('states-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid")
        return super().form_invalid(form)

class StateUpdateView(UpdateView):
    model = State
    template_name = 'State/state_details.html'
    form_class = StateForm
    success_url = reverse_lazy('states-list')
    
    # @api_view(['POST'])
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form_invalid: ", form)
        return super().form_invalid(form)
    

class StateDeleteView(DeleteView):
    model = State
    success_url = reverse_lazy('states-list')

    def form_valid(self, form):
        state_id = self.kwargs['pk']
        state = State.objects.get(pk=state_id) 
        state.delete() 
        return super().form_valid(form)
    