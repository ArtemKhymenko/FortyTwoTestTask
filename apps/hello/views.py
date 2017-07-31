from django.views.generic.base import TemplateView

from hello.models import Person

class HomePageView(TemplateView):

    template_name = 'index.html'
    data = Person.objects.all()

    def get_context_data(self, **kwargs):
        context = ({
            'data': self.data,
        })

        return context
