from rest_framework import serializers
from chart.models import Category
class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('area', 'category', 'lat', 'lan', 'price')
    
     