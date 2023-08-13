from django.shortcuts import render
from .models import Entry
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "content"]

    def get_success_url(self) -> str:
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
