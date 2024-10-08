from rest_framework import serializers
from myapp.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields: list[str] = ["id", "name", "desc"]
