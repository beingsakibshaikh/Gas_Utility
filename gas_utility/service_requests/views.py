from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.urls import reverse


def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            print(service_request)
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})


def request_status(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'request_status.html', {'requests': requests})

def some_view(request):
    return redirect(reverse('submit_request'))