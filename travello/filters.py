import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Myorder
        fields = '__all__'
        exclude = ['name', 'date_created']

class CustomerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    address = CharFilter(field_name='address', lookup_expr='icontains')
    class Meta:
        model = Newcustomer
        fields = ('mobileno',)
        exclude = ['date_created' ]


class ComplainFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    mobile = CharFilter(field_name='mobile', lookup_expr='icontains')
    status = CharFilter(field_name='status', lookup_expr='icontains')
    class Meta:
        model = Newcomplain
        fields = '__all__'
        exclude = ['date_created' ,'user1', 'email','date_solved','comments', 'note','subject' ]