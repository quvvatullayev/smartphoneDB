from django.shortcuts import render
from django.views import View
# Create your views here.
class AddProductView(View):
 
    def post(self, request):
        """
        Add a new product
        args:
            request: HTTP request
        returns:
            HTTP response
        """
        pass

    def get(self, request):
        """
        Get all products
        args:
            request: HTTP request
        returns:
            HTTP response
        """
        pass


class GetProduct(View):
    def get(self, request, id):
        """
        Get a product by id
        args:
            request: HTTP request
            id: product id
        returns:
            HTTP response
        """
        pass

 