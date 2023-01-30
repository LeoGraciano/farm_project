from django_filters import rest_framework as filters
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from farm_base.models.farm import Farm

class FarmFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    municipality = django_filters.CharFilter(field_name='municipality', lookup_expr='icontains')
    state = django_filters.CharFilter(field_name='state', lookup_expr='icontains')
    owner = django_filters.CharFilter(field_name='owner__name', label="Owner", lookup_expr='icontains')
    document = django_filters.CharFilter(field_name='owner__document', label="Document")

    class Meta:
            model = Farm
            fields = ['id','name']