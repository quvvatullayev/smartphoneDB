from itertools import product
from django.shortcuts import render
from django.views import View
from .models import Company, Product
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
        product = Product()
        product.name = request.POST.get('name')
        product.color = request.POST.get('color')
        product.ram = request.POST.get('ram')
        product.memory = request.POST.get('memory')
        product.price = request.POST.get('price')
        product.image = request.POST.get('image')
        product.release_date = request.POST.get('release_date')
        product.company = Company.objects.get(id=request.POST.get('company'))
        product.save()
        

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

 