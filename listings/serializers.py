from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    '''для преобразования экземпляров модели Listing в формат, подходящий для передачи по API'''
    class Meta:
        model = Listing
        fields = '__all__'