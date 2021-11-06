from django.shortcuts import render
from rest_framework.views import APIView
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteView(APIView):
    def get(self, request, customer_id=None):
        if customer_id:
            try:
                queryset = Favorite.objects.get(customer_id=customer_id)
            except Favorite.DoesNotExist:
                return Response({"errors": "This user does not exist."}, status=400)
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
            item = FavoriteSerializer.objects.get(customer_id=id)
            return item
        except FavoriteSerializer.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({"errors": "This user does not exist."}, status=400)

