from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class DeactivateOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def patch(self, request, *args, **kwargs):
        order = self.get_object()
        if not order.is_active:
            return Response({'status': 'fail', 'message': 'Order already deactivated'}, status=status.HTTP_400_BAD_REQUEST)
        
        order.is_active = False
        order.save()
        return Response({'status': 'success', 'message': 'Order deactivated'}, status=status.HTTP_200_OK)
    

class OrdersByDateRangeView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Fetch query parameters
        start_date = self.request.query_params.get('start_date')
        embargo_date = self.request.query_params.get('embargo_date')
        
        if start_date and embargo_date:
            # Filter orders within the date range
            return self.queryset.filter(
                Q(start_date__gte=start_date) & Q(embargo_date__lte=embargo_date)
            )
        return self.queryset.none()  # Return an empty queryset if no valid date range is provided
