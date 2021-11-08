from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view
from django.db.models import Q
from functools import reduce

from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryView(APIView):
    def get(self, request, category_id=None):
        if category_id:
            try:
                queryset = Category.objects.get(category_id=category_id)
            except Category.DoesNotExist:
                return Response({"errors": "This category does not exist."}, status=400)
            read_serializer = CategorySerializer(queryset)
        else:
            queryset = Category.objects.all()
            read_serializer = CategorySerializer(queryset, many=True)

        return Response(read_serializer.data)


class SubCategoryView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                queryset = SubCategory.objects.get(subcategory_id=id)
            except SubCategory.DoesNotExist:
                return Response({"errors": "This category does not exist."}, status=400)
            read_serializer = SubCategorySerializer(queryset)
        else:
            queryset = SubCategory.objects.all()
            read_serializer = SubCategorySerializer(queryset, many=True)

        return Response(read_serializer.data)


class ProductView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                queryset = Product.objects.get(product_id=id)
            except Product.DoesNotExist:
                return Response({"errors": "This category does not exist."}, status=400)
            read_serializer = ProductSerializer(queryset)
        else:
            queryset = Product.objects.all()[:50]
            read_serializer = ProductSerializer(queryset, many=True)

        return Response(read_serializer.data)


# Search query function
@api_view(["GET"])
def search(request):
    name = request.GET.get("name")
    cat = request.GET.get("category")
    subcat = request.GET.get("subcategory")
    gender = request.GET.get("gender")
    color = request.GET.get("color")
    # Q is object wrapper for condition, set to none if not existing
    filter_name = ~Q(product_name=None)
    filter_gender = (
        ~Q(product_gender=None) if gender is None else Q(product_gender__iexact=gender)
    )
    filter_color = (
        ~Q(product_color=None) if color is None else Q(product_color__icontains=color)
    )
    filter_cat = ~Q(category=None)
    filter_subcat = ~Q(subcategory=None)

    if name:
        name_lst = name.split(" ")
        filter_name = reduce(
            lambda x, y: x & y, [Q(product_name__icontains=word) for word in name_lst]
        )

    # Take the id of category and subcategory
    if cat:
        cat_id = Category.objects.filter(name__iexact=cat).values_list(
            "category_id", flat=True
        )[0]
        filter_cat = Q(category=cat_id)
    if subcat:
        subcat_id = SubCategory.objects.filter(name__iexact=subcat).values_list(
            "subcategory_id", flat=True
        )[0]
        filter_subcat = Q(subcategory=subcat_id)

    try:
        products = Product.objects.filter(
            filter_name, filter_color, filter_gender, filter_cat, filter_subcat
        )[:25]
        print(type(products))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except:
        return Response({"errors": "This product does not exist."}, status=400)
