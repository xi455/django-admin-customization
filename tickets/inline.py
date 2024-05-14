from django.contrib import admin

from tickets.models import Concert


class ConcertInline(admin.TabularInline):
    model = Concert
    fields = ["name", "starts_at", "price", "tickets_left"]
    readonly_fields = ["name", "starts_at", "price", "tickets_left"]
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True
