from django.urls import path, include
from .views import MarketsView, MarketSingleView, SellerOfMarketList, market_single_view, sellers_view, sellers_single_view, ProductViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', MarketsView.as_view()),
    path('<int:pk>/', MarketSingleView.as_view(), name='market-detail'),
    path('<int:pk>/sellers/', SellerOfMarketList.as_view(), name='market-sellers'),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single'),
]
