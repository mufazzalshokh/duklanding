from django.views.generic import TemplateView, CreateView

from page.forms import ContactModelForm


class HomeTemplateView(TemplateView):
    template_name = 'index-sport.html'


class ContactCreateView(CreateView):
    # template_name = 'contact.html'
    form_class = ContactModelForm
