from rest_framework import generics
from sweetCocoWeb.models import Product
from sweetCocoWeb.serializer import ProductSerializer

'''
This class inherited from generics.ListCreateAPIView
1) This view is designed for operations related to a COLLECTION of resources.
2) Handles GET (list) and POST (create) requests.
3) Provides a list of resources (GET) or allows the creation of a new resource (POST).
'''
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        # Customize the queryset based on your needs
        return Product.objects.all()

'''
This class inherited from generics.RetrieveUpdateDestroyAPIView
1) This view is designed for operations related to a SINGLE resource.
2) Handles GET (retrieve), PUT (update), PATCH (partial update), and DELETE (destroy) requests.
3) Retrieves details of a single resource (GET), allows updating of a resource (PUT), updates part of a resource (PATCH), or deletes a resource (DELETE).
'''
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        # Customize the queryset based on your needs
        return Product.objects.all()