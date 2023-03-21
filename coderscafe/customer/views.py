from django.shortcuts import render
from django.views import View



class Index(View):
     def get(self, request, *args, **kwargs):
         return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
     def get(self, request, *args, **kwargs):
        # get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='entre')
        desserts = MenuItem.objects.filter(category__name__contains='dessert')
        drinks = MenuItem.objects.filter(category__name__contains='drink')

        #pass into context

        #render the template
