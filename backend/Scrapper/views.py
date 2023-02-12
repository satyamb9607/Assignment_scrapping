from rest_framework import viewsets
from .models import Crypto
from .serializers import CryptoSerializer
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
from django.http import HttpResponse

class ScrapViewset(viewsets.ModelViewSet):
    # Specifying the serializer class to be used
    serializer_class = CryptoSerializer
    # Queryset to be used for the ViewSet
    queryset = Crypto.objects.all()
    # Allowed methods for this ViewSet
    allowed_methods = ['GET', 'POST']

    def create(self, request, *args, **kwargs):
        # Getting the data from the request
        data = request.data
        
        # Looping through each record in the data
        for record in data:
            # Getting an instance of the serializer
            serializer = self.get_serializer(data=record)
            
            # Checking if the serialized data is valid
            if serializer.is_valid(raise_exception=True):
                # Updating or creating a new instance of Crypto
                obj, created = Crypto.objects.update_or_create(
                    name=record['name'],
                    defaults=serializer.data,
                )
        
        # Returning a success response with a status code of 201 (created)
        return Response({'success': "Records created successfully"}, status.HTTP_201_CREATED)