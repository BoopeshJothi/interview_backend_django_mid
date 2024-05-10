
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, DeactivateOrderView, OrdersByDateRangeView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/deactivate/', DeactivateOrderView.as_view(), name='deactivate-order'),
    path('orders/by-date-range/', OrdersByDateRangeView.as_view(), name='orders-by-date-range'),

]