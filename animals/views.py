from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


# class InfoMixin(ContextMixin):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['info'] = get_info()
#         return context


class IndexView(TemplateView):
    template_name = 'animals/index.html'


class AboutView(TemplateView):
    template_name = 'animals/about.html'


def index_view(request):
    if request.is_get:
        return render(request, 'animals/index.html')
    raise Http404
