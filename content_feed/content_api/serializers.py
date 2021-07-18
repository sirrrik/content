from rest_framework import fields, serializers
from content_api.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = 'id', 'title', 'description','image'
