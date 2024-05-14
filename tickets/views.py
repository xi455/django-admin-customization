from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from tickets.models import Concert, Ticket
from tickets.forms import TicketCreateForm
# Create your views here.

class ConcertListView(ListView):
    model = Concert
    paginate_by = 5
    template_name = "concert_list.html"
    queryset = Concert.objects.filter(tickets_left__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "音樂會場次"
        return context


class TicketBuyCreateView(CreateView):
    model = Ticket
    form_class = TicketCreateForm
    success_url = reverse_lazy("ticket:ticket-list")
    template_name = "concert_detail.html"

    def form_valid(self, form: TicketCreateForm) -> HttpResponse:
        query = get_object_or_404(Concert, id=self.kwargs["pk"])

        if query.tickets_left > 0:
            messages.success(self.request, "購票成功！！")

            form.instance.concert = query
            form.instance.customer_full_name = form.cleaned_data["first_name"] + " " + form.cleaned_data["last_name"]

            query.tickets_left -= 1
            query.save()

            return super().form_valid(form)
        else:
            messages.error(self.request, "購買失敗！！ 門票已盡數售出！！")
            return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        concert = get_object_or_404(Concert, id=self.kwargs["pk"])

        context = super().get_context_data(**kwargs)
        context["title"] = "購票資訊"
        context["concert"] = concert
        return context


class TicketListView(ListView):
    model = Ticket
    paginate_by = 10
    template_name = "ticket_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "購票目錄"
        return context