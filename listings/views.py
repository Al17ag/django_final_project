from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ListingSerializer
from .models import Listing
from django_filters.rest_framework import DjangoFilterBackend
def index(request):
    return HttpResponse('Home page')

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'location', 'rooms', 'housing_type']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['price']
