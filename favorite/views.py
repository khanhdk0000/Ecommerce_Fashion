from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Favorite, Contains
from rest_framework.decorators import api_view
from .serializers import FavoriteSerializer, ContainsSerializer
from product.serializers import ProductSerializer
from product.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict

class FavoriteView(APIView):
    def get(self, request, customer_id=None):
        if customer_id:
            try:
                queryset = Favorite.objects.get(customer_id=customer_id)
                # id = queryset.favorite_id
                # tem = Contains.objects.filter(favorite_id=id)
                # print(tem.query)
                # print(type(tem), type(queryset))
            except Favorite.DoesNotExist:
                return Response({"errors": "This user does not exist."}, status=400)
            # read_serializer = ContainsSerializer(tem, many=True)
            read_serializer = FavoriteSerializer(queryset)
        else:
            return Response({"errors": "No id provided."}, status=400)

        return Response(read_serializer.data)
    
    def post(self, request, customer_id=None):
        create_serializer = FavoriteSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # Create new item
            order_item_obj = create_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = FavoriteSerializer(order_item_obj)

            # Return a HTTP response with the newly created item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, customer_id=None):
        item = self._check_item(customer_id)

        # If the item does exists, use the serializer to validate the updated data
        update_serializer = FavoriteSerializer(item, data=request.data)

        # If the data to update the item is valid, proceed to saving data to the database
        if update_serializer.is_valid():
            # Update item in db
            item_obj = update_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = FavoriteSerializer(item_obj)

            # Return a HTTP response with the newly updated item data
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, customer_id=None):
        item = self._check_item(customer_id)
        print(type(item))

        # Delete the chosen item from db
        item.delete()

        # Return a HTTP response notifying that the item was successfully deleted
        return Response(status=204)

    def _check_item(self, id):
        try:
            # Check if the todo item the user wants to update exists
            print('get called')
            item = FavoriteSerializer.objects.get(customer=id)
            return item
        except:
            # If the todo item does not exist, return an error response
            return Response({"errors": "This user does not exist."}, status=400)



class ContainsView(APIView):
    def get(self, request, product_id=None, customer_id=None):
        print('contain get called')
        if favorite_id:
            try:
                queryset = Contains.objects.get(favorite_id=favorite_id)
            except Favorite.DoesNotExist:
                return Response({"errors": "This favorite does not exist."}, status=400)
            read_serializer = ContainsSerializer(queryset)
        else:
            return Response({"errors": "No id provided."}, status=400)

        return Response(read_serializer.data)
    
    def post(self, request, product_id=None, customer_id=None):
        favorite = Favorite.objects.get(customer_id=customer_id)
        ordinary_dict = {'favorite_id': favorite.favorite_id, 'product_id': product_id}
        query_dict = QueryDict('', mutable=True)
        query_dict.update(ordinary_dict)
        create_serializer = ContainsSerializer(data=query_dict)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # Create new item
            order_item_obj = create_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = ContainsSerializer(order_item_obj)

            # Return a HTTP response with the newly created item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, product_id=None, customer_id=None):
        item = self._check_item(customer_id)

        # If the item does exists, use the serializer to validate the updated data
        update_serializer = ContainsSerializer(item, data=request.data)

        # If the data to update the item is valid, proceed to saving data to the database
        if update_serializer.is_valid():
            # Update item in db
            item_obj = update_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = ContainsSerializer(item_obj)

            # Return a HTTP response with the newly updated item data
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, product_id=None, customer_id=None):
        item = self._check_item(product_id, customer_id)
        print(request.data)

        # Delete the chosen item from db
        item.delete()

        # Return a HTTP response notifying that the item was successfully deleted
        return Response(status=204)

    def _check_item(self, product_id, customer_id):
        try:
             # Get Favorite object by user id
            favorite = Favorite.objects.get(customer_id=customer_id)
            item = Contains.objects.filter(favorite_id=favorite.favorite_id, product_id=product_id)
            # print(item)
            return item
        except ObjectDoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({"errors": "This user does not exist."}, status=400)


# Search wishlist function
@api_view(["GET"])
def wishlist(request, customer_id=None):
    """
    Take customer_id and return all the favorite items in the database belongs to that user.

    """
    # Get Favorite object by user id
    favorite = Favorite.objects.get(customer_id=customer_id)

    # get contains object with id = favorite id of the user, returns a tuple
    queryContains = Contains.objects.values_list('favorite_id', 'product_id').filter(favorite_id=favorite.favorite_id)

    # Get list of products
    res = list(map(lambda x: Product.objects.get(product_id=x[1]), list(queryContains)))

    # map the list to json
    read_serializer = ProductSerializer(res, many=True)
    return Response(read_serializer.data, status=201)