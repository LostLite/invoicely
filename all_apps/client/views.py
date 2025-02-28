from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm

# Create your views here.
@login_required
def index(request):
    clients = Client.objects.all().filter(created_by=request.user)
    return render(request, 'client/index.html', {'clients': clients})


@login_required
def add_client(request):
    
    form = ClientForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            
            form.instance.created_by = request.user
            form.save()
            
            messages.success(request, 'New client added successfully.')
            return redirect('all-clients')
    
    return render(request, 'client/client_form.html', {'form': form, 'form_title': 'New Client'})


@login_required
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Client updated successfully.')
            return redirect('all-clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/client_form.html', {'form': form})


@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk, created_by=request.user)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully.')
        return redirect('all-clients')
    return render(request, 'client/client_confirm_delete.html', {'client': client})

