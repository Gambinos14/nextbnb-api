from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import get_object_or_404

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

class HouseFeatured(generics.ListAPIView):
  permission_classes = ()
  authentication_classes = ()
  serializer_class = HouseSerializer
  queryset = ''
  def get(self, request, slug):
    houses = House.objects.filter(featured=slug).order_by("?")[:4]
    data = HouseSerializer(houses, many=True).data
    return Response(data)

class HouseDetail(generics.RetrieveAPIView):
  permission_classes = ()
  authentication_classes = ()
  queryset = ''
  serializer_class = HouseSerializer
  def get(self, request, pk):
    house = get_object_or_404(House, pk=pk)
    data = HouseSerializer(house).data
    return Response(data)
