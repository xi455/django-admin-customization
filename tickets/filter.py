from typing import Any

from django.contrib.admin import SimpleListFilter
from django.db.models.query import QuerySet

from tickets.models import Venue, Concert


class SoldOutFilter(SimpleListFilter):
    title = "Sold out"
    parameter_name = "sold_out"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "yes":
            return queryset.filter(tickets_left=0)
        else:
            return queryset.exclude(tickets_left=0)


class ConcertFilter(SimpleListFilter):
    title = "Concert"
    parameter_name = "concert"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        concerts_queryset = Concert.objects.all().distinct()
        return [(concert.id, concert.name) for concert in concerts_queryset]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value():
            return queryset.filter(concert_id=self.value())


class VenueFilter(SimpleListFilter):
    title = "Venue"
    parameter_name = "venue"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        venue_queryset = Venue.objects.all().distinct()
        return [(venue.id, venue.name) for venue in venue_queryset]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value():
            return queryset.filter(concert__venue_id=self.value())