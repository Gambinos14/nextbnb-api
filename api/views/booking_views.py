from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from operator import itemgetter


from ..models.booking import Booking
from ..serializers import BookingSerializer
from ..serializers import BookingReadSerializer


class Bookings(generics.ListCreateAPIView):
  queryset = ''
  serializer_class = BookingSerializer

  def get(self, request):
    bookings = Booking.objects.filter(guest=request.user.id)
    data = BookingReadSerializer(bookings, many=True).data
    ordered_dates = sorted(data, key=itemgetter('start'))
    return Response(ordered_dates)

  def post(self, request):
    request.data['booking']['guest'] = request.user.id
    booking = BookingSerializer(data=request.data['booking'])
    if booking.is_valid():
      booking.save()
      return Response(booking.data, status=status.HTTP_201_CREATED)
    else:
      return Response(booking.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = ''
  serializer_class = BookingSerializer

  def get(self, request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    data = BookingReadSerializer(booking).data

    if not request.user.id == data['guest']:
      raise PermissionDenied('Unauthorized. You do not own this reservation.')
    return Response(data)

  def delete(self, request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    data = BookingSerializer(booking).data
    if not request.user.id == data['guest']:
      raise PermissionDenied('Unauthorized. You do not own this reservation.')
    booking.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
    if request.data['booking'].get('guest', False):
      del request.data['booking']['guest']

    booking = get_object_or_404(Booking, pk=pk)
    data = BookingReadSerializer(booking).data

    if not request.user.id == data['guest']:
      raise PermissionDenied('Unauthorized. You do not own this reservation.')

    request.data['booking']['guest'] = request.user.id

    updatedBooking = BookingSerializer(booking, data=request.data['booking'], partial=True)
    if updatedBooking.is_valid():
      updatedBooking.save()
      return Response(updatedBooking.data)
    else:
      return Response(updatedBooking.errors, status=status.HTTP_400_BAD_REQUEST)
