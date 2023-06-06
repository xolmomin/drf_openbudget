from django_filters import FilterSet, CharFilter, NumberFilter

from apps.models import Product


class ProductFilterSet(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')
    category = CharFilter(field_name='category__description', lookup_expr='exact')
    # created_date = DateFilter(field_name='created_date__date', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', )
        # fields = {
        #     'price': ['lte'],
        #     'name': ['exact']
        # }

    # def customfileter(self, queryset, name, value):
    #     return queryset.filter(price=value)
