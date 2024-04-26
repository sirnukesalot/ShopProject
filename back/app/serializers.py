from rest_framework import serializers


from .models import Product, Brand, ProductCategory, Order, CustomUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'




class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    id = serializers.IntegerField()
    class Meta:
        model = Brand
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')