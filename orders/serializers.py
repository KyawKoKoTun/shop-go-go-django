from rest_framework import serializers
from .models import Order, Item
from userdata.models import ShippingAddress

class ItemSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)

    class Meta:
        model = Item
        fields = ['product', 'quantity', 'total']

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
        
class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    address = serializers.SerializerMethodField()
    address_input = serializers.CharField(write_only=True)  # For accepting address input

    class Meta:
        model = Order
        fields = ['user', 'screenshot', 'items', 'status', 'address', 'address_input']

    def get_address(self, obj):
        if obj.address:
            return obj.address.address
        return None

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        address_data = validated_data.pop('address_input', None)  # Get address data from validated data

        user = self.context['request'].user
        if address_data:
            address_instance, _ = ShippingAddress.objects.get_or_create(user=user, address=address_data)
        else:
            address_instance = None

        order = Order.objects.create(user=user, address=address_instance, **validated_data)

        for item_data in items_data:
            Item.objects.create(order=order, **item_data)

        return order
