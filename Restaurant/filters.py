from .models import Restaurant 
import django_filters

class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model=Restaurant
        fields = ['cuisine','ville','meals','price']

