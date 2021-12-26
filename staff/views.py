from django.views.generic import TemplateView

from staff.models import StaffModel


class HomeTemplateView(TemplateView):
    template_name = 'index-sport.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['staffs'] = StaffModel.objects.order_by('-pk')[:3]

        return context
