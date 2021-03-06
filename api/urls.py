from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.house_views import Houses, HouseSearch, HouseFeatured, HouseDetail
from .views.booking_views import Bookings, BookingDetail
from .views.payments import Pay

urlpatterns = [
	# Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('houses/', Houses.as_view(), name='houses-index'),
    path('houses/<slug:slug>/', HouseSearch.as_view(), name='house-search'),
    path('houses/featured/<slug:slug>/', HouseFeatured.as_view(), name='house-featured'),
    path('houses/id/<int:pk>/', HouseDetail.as_view(), name='houses-show'),
    path('bookings/', Bookings.as_view(), name='bookings-index'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='bookings-show'),
    path('pay/', Pay.as_view(), name='payment')
]
