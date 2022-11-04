from django.shortcuts import render
from django.views import View
from .models import Company, Product
from django.http import JsonResponse
from datetime import datetime,date

from django.contrib.auth.models import User
class MainView(View):
    def get(self,request):
        company = Company.objects.get(name='Artel')

        product = Product()
        product.color = 'Black'
        product.name = 'Artel PRO MAX'
        product.ram = 6
        product.memory = 128
        product.price = 1100
        product.release_date = date(2019,1,13)
        product.image = 'img'
        product.company = company
        product.save()

        return JsonResponse({'Result':company.name})
     

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
        return JsonResponse({'message': 'Product added successfully'})
        

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
    def get(self, request, name):
        """
        Get a product by company name 
        args:
            request: HTTP request
            id: product id
        returns:
            HTTP response
        """
        products = Product.objects.filter(company__name=name)
        result = {
            'result':[]
        }
        for p in products:
            product_data = {
                   'name': p.name,
                   'color': p.color,
                   'ram': p.ram,
                   'memory': p.memory,
                   'price': p.price,
                   'image': p.image,
                   'release_date': p.release_date,
                   'company': p.company.name
               }
            result['result'].append(product_data)

        return JsonResponse(result)


class GetUserView(View):
    def get(self,request):
        user = User.objects.get(username='admin')
        return JsonResponse({
            'username':user.username,
            'email':user.email,
            'super':user.is_superuser,
            'password':user.password
        })
            
            



       
            
            


class getCompany(View):
    def get(self, request, name):
        """
        Get a company by id
        args:
            request: HTTP request
            id: company id
        returns:
            HTTP response
        """
        company = Company.objects.filter(product__name__contains=name)
        return JsonResponse({'Result':company[0].name,'total':company.count()})

  
 