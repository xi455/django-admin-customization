from django.urls import path
from tickets.views import ConcertListView, TicketBuyCreateView

app_name = "ticket"
urlpatterns = [
    path("/concert/", ConcertListView.as_view(), name="ticket-list"),
    path("/concert/detail/<pk>/", TicketBuyCreateView.as_view(), name="concert-detail"),
    # path("/concert/<pk>/buy/", TicketBuyCreateView.as_view(), name="ticket-buy"),
]
