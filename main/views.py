from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()

    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''

    context = {'contacts':contacts,'search_input':search_input}
    return render(request, 'index.html', context)

def addContact(request):
    if request.method == 'POST':
        contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            adress = request.POST['address'],
            phone_number = request.POST['phone-number'],
            email = request.POST['email'],
        )
        contact.save()
        return redirect('/')

    return render(request, 'new.html')

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact = Contact.objects.get(id=pk)
        contact.delete()
        return redirect('/')

    context = {'contact':contact}
    return render(request, 'delete.html', context)

def profile(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact':contact}
    return render(request, 'contact-profile.html',context)

def edit(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.adress = request.POST['address']
        contact.phone_number = request.POST['phone-number']
        contact.email = request.POST['email']
        contact.save()
        return redirect('/')


    context = {'contact':contact}
    return render(request, 'edit.html', context)