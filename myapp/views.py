from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models import Item
from myapp.serializers import ItemSerializer


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SomeShit(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        content = {"message": "for sure"}
        return Response(content)
