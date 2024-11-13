from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse
from .models import contactus
def home(request):
    return HttpResponse("This is klu project with CSE app")
def base(request):
    return render(request,'base.html')
def login(request):
    return render(request,'login1.html')
# Create your views here.
def logout(request):
    return render(request,'logout.html')


from .forms import LocationForm
from datetime import datetime
import pytz
def timezonepagecall(request):
    return render(request,'timezonepage.html')

def timezonepagelogic(request):
    current_time = None
    selected_location = None
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            selected_location = form.cleaned_data['timezone']
            timezone = pytz.timezone(selected_location)
            current_time = datetime.now(timezone)
            print(f"Selected Location: {selected_location}")
            print(f"Current Time: {current_time}")
    else:
        form = LocationForm()

    context = {
        'form': form,
        'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S') if current_time else None,
        'selected_location': selected_location,
    }
    print("Context Data:", context)
    return render(request, 'timezonepage.html', context)

def contactlogic(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        subject = 'Thank You for ur valuable Feedback'
        send_mail(
            subject,
            comment,
            'thummagantijayanthraj@gmail.com',  # Update with your sender email
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Thank you for giving Feedback </center></h1>")
    else:
        HttpResponse("<h1>error</h1>")

def contactpagecall(request):
            # Your logic here
            return render(request   , 'contact.html')

# contacts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    query = request.GET.get('q', '')
    contacts = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(email__icontains=query)
    return render(request, 'contact_list.html', {'contacts': contacts, 'query': query})

def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()


            send_mail(
                'New Contact Added',
                f'Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nAddress: {contact.address}',
                'saiganeshmurala@gmail.com',
                ['gkarthik8467@gmail.com'],
                fail_silently=False,
            )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')


# contacts/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact


def send_all_contacts(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')  # Get the user-defined email

        # Get all contacts
        contacts = Contact.objects.all()
        contact_details = "\n".join([
            f'Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}, Address: {contact.address}'
            for contact in contacts
        ])

        # Send email
        send_mail(
            'All Contacts',
            contact_details or 'No contacts available.',
            'saiganeshmurala@gmail.com',
            [recipient_email],
            fail_silently=False,
        )

        return redirect('contact_list')  # Redirect after sending

    return render(request, 'send_all_contacts.html')  # Render a template to send contacts

