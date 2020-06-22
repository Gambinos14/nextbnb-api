from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q

from ..models.house import House
from ..serializers import HouseSerializer

class Houses(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = HouseSerializer
    queryset = ''
    def get(self, request):
      houses = House.objects.all()
      data = HouseSerializer(houses, many=True).data
      return Response(data)

class HouseSearch(generics.ListAPIView):
  permission_classes = ()
  authentication_classes = ()
  serializer_class = HouseSerializer
  queryset = ''
  def get(self, request, slug):
    print('slug:', slug)
    houses = House.objects.filter(Q(city=slug) | Q(country=slug))
    data = HouseSerializer(houses, many=True).data
    return Response(data)
