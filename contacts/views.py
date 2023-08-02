from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            messages.success(request, "We have received your messages.")
            return redirect("contact")
    else:
        form = ContactForm()
        context = {
            'form': form
        }
    return render(request, "contact.html", context)