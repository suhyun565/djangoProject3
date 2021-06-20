import django_filters

from speedracer.models import Product


class productFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['contains', ],
            'category': ['contains', ],
            'price': ['lt', 'range'],
        }

