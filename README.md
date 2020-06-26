# NextBnb - API

This application allows users to view properties and manage bookings on those
properties as they plan their next travel adventure!

## Important Links

- [NextBnb Client](https://gambinos14.github.io/nextbnb-client/#/)
- [NextBnb Django API](https://nextbnb-api.herokuapp.com/)

## Homepage View

![Homepage](nextbnb2.jpg)

## Planning Story

To build the api I first had to outline the relationships between my resources so
that I could make sure I'd have the necessary information to build out the front
end. I decided to build complete CRUD routes on the bookings resource, while only
building out GET routes for my house model.

Between the house model and booking model, I was able to obtain all the information
I would need on the client side to accurately display the details of a users'
booking reservation. The api can easily be built out to handle full CRUD actions
on the house model as well as the image model.

I thought one of the most challenging aspects of building out the Djano API was
choosing the right data model fields for my booking model. Initially, I tried using
a DateRange field which wasn't correctly handling the data I was sending it, so
eventually I settled on a DateField model with two keys on my model for a start
date and end date for each booking.

There were a few other challenges associated with having to override the queryset
attribute on a few rest-framework class-based views, but in the end I was able
to overcome those by giving queryset the value of an empty string.

### User Stories

* As an unregistered user, I would like to sign up with email and password.
* As a registered user, I would like to sign in with email and password.
* As a signed in user, I would like to change password.
* As a signed in user, I would like to sign out.
* As a signed in user, I would like to make a reservation at my favorite property.
* As a signed in user, I would like to be able to update my reservation.
* As a signed in user, I would like to cancel a reservation.
* As a signed in user, I would like to see all my reservations.
* As a signed in user, I would like to view individual reservation details

### Technologies Used

- Python
- Django
- SQL
- Postgres
- Heroku

### Unsolved Problems/Future Updates

- Would like to continue building out the views for houses so that I can create
and update houses from the client site.
- Would like to eventually add a comment model so that users can add comments
on the houses.
- Would like to move some of the booking dates filtering logic to the backend, so
that I can return less data to the client.

#### Wireframe and ERD

- [Wireframe and ERDs ](https://docs.google.com/document/d/1Pk_ML21nfQIxZaxbK4QNUWwwAYiqOJhJ7Ier5KqV4WY/edit?usp=sharing)
