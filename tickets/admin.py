from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportActionModelAdmin

from tickets.filter import SoldOutFilter, ConcertFilter, VenueFilter
from tickets.forms import TicketAdminForm
from tickets.inline import ConcertInline
from tickets.models import Concert, ConcertCategory, Ticket, Venue


class VenueAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ["name", "address", "capacity"]
    search_fields = ["name", "address"]
    inlines = [ConcertInline]


class ConcertCategoryAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class ConcertAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [
        "name",
        "venue",
        "starts_at",
        "tickets_left",
        "display_sold_out",
        "display_price",
        "display_venue",
    ]
    list_select_related = ["venue"]

    list_filter = ["venue", SoldOutFilter]

    search_fields = ["name", "venue__name", "venue__address"]

    def display_sold_out(self, obj):
        return obj.tickets_left == 0

    def display_price(self, obj):
        return f"${obj.price}"

    def display_venue(self, obj):
        link = reverse("admin:tickets_venue_change", args=[obj.venue.id])
        return format_html('<a href="{}">{}</a>', link, obj.venue)

    display_sold_out.short_description = "Sold out"
    display_sold_out.boolean = True

    display_price.short_description = "Price"
    display_price.admin_order_field = "price"

    display_venue.short_description = "Venue"


@admin.action(description="Activate selected tickets")
def activate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate selected tickets")
def deactivate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=False)


class TicketAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = [
        "customer_full_name",
        "concert",
        "payment_method",
        "paid_at",
        "is_active",
    ]
    list_select_related = ["concert", "concert__venue"]

    list_filter = [ConcertFilter, VenueFilter]
    search_fields = ["customer_full_name", "concert__name", "concert__venue__name"]
    actions = [activate_tickets, deactivate_tickets]

    form = TicketAdminForm


admin.site.register(Venue, VenueAdmin)
admin.site.register(ConcertCategory, ConcertCategoryAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Ticket, TicketAdmin)
