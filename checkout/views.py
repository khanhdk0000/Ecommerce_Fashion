from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from checkout.models import Order, OrderDetail, RegisteredCustomer
from checkout.serializers import (
    OrderDetailSerializer,
    OrderSerializer,
    RegisteredCustomerSerializer,
)
from product.models import Product

# Create your views here.


class OrderView(APIView):
    def get(self, request, order_id=None, customer_id=None):
        if order_id:
            # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                queryset = Order.objects.get(order_id=order_id)
                read_serializer = OrderSerializer(queryset)
            except Order.DoesNotExist:
                return Response({"errors": "This order does not exist."}, status=400)
        elif customer_id and not order_id:
            try:
                queryset = Order.objects.filter(
                    customer_id=customer_id)
                read_serializer = OrderSerializer(queryset, many=True)
            except Order.DoesNotExist:
                return Response({"warnings": "This customer's order does not exist."}, status=303)
        else:
            queryset = Order.objects.all()
            # print("-" * 50, end="\n\n")
            # print(queryset, end="\n\n")
            # print("-" * 50, end="\n\n")
            read_serializer = OrderSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = OrderSerializer(
            data=request.data,
        )

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # Create new item
            order_item_obj = create_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = OrderSerializer(order_item_obj)

            # Return a HTTP response with the newly created item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, order_id=None):
        item = self._check_item(order_id)

        # If the item does exists, use the serializer to validate the updated data
        update_serializer = OrderSerializer(item, data=request.data)

        # If the data to update the item is valid, proceed to saving data to the database
        if update_serializer.is_valid():
            # Update item in db
            item_obj = update_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = OrderSerializer(item_obj)

            # Return a HTTP response with the newly updated item data
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, order_id=None):
        item = self._check_item(order_id)

        # Delete the chosen item from db
        item.delete()

        # Return a HTTP response notifying that the item was successfully deleted
        return Response(status=204)

    def _check_item(self, id):
        try:
            # Check if the todo item the user wants to update exists
            item = Order.objects.get(order_id=id)
            return item
        except Order.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({"errors": "This order item does not exist."}, status=400)


class OrderDetailView(APIView):
    def get(self, request, order_id=None, product_id=None):
        if order_id and product_id:
            try:
                queryset = OrderDetail.objects.get(
                    order_id=order_id, product_id=product_id)

                read_serializer = OrderDetailSerializer(queryset)
            except OrderDetail.DoesNotExist:
                return Response(
                    {"warnings": "This order detail does not exist."}, status=303
                )
        elif order_id and not product_id:
            # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                queryset = OrderDetail.objects.filter(
                    order_id=order_id
                )
                read_serializer = OrderDetailSerializer(queryset, many=True)
            except OrderDetail.DoesNotExist:
                return Response(
                    {"errors": "No order details exist when search by order_id"}, status=400
                )
        elif product_id and not order_id:
            try:
                queryset = OrderDetail.objects.filter(product_id=product_id)
                read_serializer = OrderDetailSerializer(queryset, many=True)
            except OrderDetail.DoesNotExist:
                return Response(
                    {"errors": "No order details exist when search by product_id"},
                    status=400,
                )
        else:
            queryset = OrderDetail.objects.all()
            read_serializer = OrderDetailSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        # print("-" * 50, end="\n\n")
        # print(request.data, end="\n\n")
        # print("-" * 50, end="\n\n")
        create_serializer = OrderDetailSerializer(
            data=request.data,
        )

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # Create new item
            detail_item_obj = create_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = OrderDetailSerializer(detail_item_obj)

            # Return a HTTP response with the newly created item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, order_id=None, product_id=None):
        item = self._check_item(order_id=order_id, product_id=product_id)

        # If the item does exists, use the serializer to validate the updated data
        update_serializer = OrderDetailSerializer(item, data=request.data)

        # If the data to update the item is valid, proceed to saving data to the database
        if update_serializer.is_valid():
            # Update item in db
            item_obj = update_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = OrderDetailSerializer(item_obj)

            # Return a HTTP response with the newly updated item data
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, order_id=None, product_id=None):
        item = self._check_item(order_id=order_id, product_id=product_id)

        # Delete the chosen item from db
        item.delete()

        # Return a HTTP response notifying that the item was successfully deleted
        return Response(status=204)

    def _check_item(self, order_id, product_id):
        try:
            # Check if the todo item the user wants to update exists
            item = OrderDetail.objects.filter(order_id=order_id, product_id=product_id)[
                0
            ]
            return item
        except OrderDetail.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({"errors": "This order item does not exist."}, status=400)


class RegisteredCustomerView(APIView):
    def get(self, request, customer_id=None):
        if customer_id:
            # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                queryset = RegisteredCustomer.objects.get(
                    customer_id=customer_id)
            except RegisteredCustomer.DoesNotExist:
                return Response({"errors": "This user does not exist."}, status=400)
            read_serializer = RegisteredCustomerSerializer(queryset)
        else:
            queryset = RegisteredCustomer.objects.all()
            read_serializer = RegisteredCustomerSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request, customer_id=None):
        create_serializer = RegisteredCustomerSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # Create new item
            order_item_obj = create_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = RegisteredCustomerSerializer(order_item_obj)

            # Return a HTTP response with the newly created item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, customer_id=None):
        item = self._check_item(customer_id)

        # If the item does exists, use the serializer to validate the updated data
        update_serializer = RegisteredCustomerSerializer(
            item, data=request.data)

        # If the data to update the item is valid, proceed to saving data to the database
        if update_serializer.is_valid():
            # Update item in db
            item_obj = update_serializer.save()

            # Serialize the new item from a Python object to JSON format
            read_serializer = RegisteredCustomerSerializer(item_obj)

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
            item = RegisteredCustomer.objects.get(customer_id=id)
            return item
        except RegisteredCustomer.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({"errors": "This user does not exist."}, status=400)
