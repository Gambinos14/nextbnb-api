from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from decimal import *
import os
from dotenv import load_dotenv, find_dotenv
import stripe

load_dotenv(find_dotenv())

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def generate_response(intent):
  if intent.status == 'succeeded':
    # Handle post-payment fulfillment
    return Response(intent, status=status.HTTP_200_OK)
  else:
    # Any other status would be unexpected, so error
    return Response(intent, status=status.HTTP_200_OK)

class Pay(APIView):
  authentication_classes = ()
  permission_classes = ()
  def post(self, request):
    date_format = '%Y-%m-%d'
    data = request.data
    house_price = request.data['house']['price']
    check_in = datetime.strptime((request.data['reservation']['startDate'].split('T')[0]), date_format)
    check_out = datetime.strptime((request.data['reservation']['endDate'].split('T')[0]), date_format)
    length = check_out - check_in
    twoplaces = Decimal('0.01')
    total_cost = Decimal(float(length.days) * float(house_price)).quantize(twoplaces)
    reservation_amount = round(total_cost * 100)

    try:
      # Create the PaymentIntent
      intent = stripe.PaymentIntent.create(
        amount=reservation_amount,
        currency='usd',
        payment_method=data['payment_method_id'],
        # A PaymentIntent can be confirmed some time after creation,
        # but here we want to confirm (collect payment) immediately.
        confirm=True,
        # If the payment requires any follow-up actions from the
        # customer, like two-factor authentication, Stripe will error
        # and you will need to prompt them for a new payment method.
        error_on_requires_action=True,
      )
      return generate_response(intent)
    except stripe.error.CardError as e:
      # Display error on client
      return Response({'error': e.user_message}, status=status.HTTP_200_OK)
