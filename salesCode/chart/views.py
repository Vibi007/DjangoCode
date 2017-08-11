from django.http import HttpRequest,HttpResponse, JsonResponse
from django_filters import rest_framework
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from chart.models import Category
from chart.serializers import ChartSerializer
from rest_framework import generics

# def chart_data(request):
#     if request.method == 'GET':
#         Categories = Category.objects.all()
#         serializer = ChartSerializer(Categories, many = True)
#         return JsonResponse(serializer.data,safe = False)

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ChartSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ('area','category',)