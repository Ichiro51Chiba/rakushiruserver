"""
URLs for django_occupations.
"""
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="django_occupations/base.html")),
]
