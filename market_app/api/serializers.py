from rest_framework import serializers
from market_app.models import Market, Product, Seller

class MarketSerializer(serializers.HyperlinkedModelSerializer):  

    sellers = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='seller_single',
        read_only=True
    )

    class Meta:
        model = Market
        fields = '__all__'
    
class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = '__all__'

    def get_market_count(self, obj):
        return obj.markets.count()
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'