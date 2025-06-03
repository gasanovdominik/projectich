from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['patch'], url_path='confirm')
    def confirm_booking(self, request, pk=None):
        booking = self.get_object()
        if request.user != booking.listing.owner:
            return Response({'detail': 'Недостаточно прав.'}, status=403)
        booking.status = 'confirmed'
        booking.save()
        return Response({'status': 'confirmed'})

    @action(detail=True, methods=['patch'], url_path='cancel')
    def cancel_booking(self, request, pk=None):
        booking = self.get_object()
        if request.user != booking.user and request.user != booking.listing.owner:
            return Response({'detail': 'Недостаточно прав.'}, status=403)
        booking.status = 'cancelled'
        booking.save()
        return Response({'status': 'cancelled'})

