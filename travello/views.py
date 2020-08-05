from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from telusko import settings
from .forms import *
from .models import *
from .views import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    dests = Destination.objects.all()
    return render(request, "travello/home.html", {"dests": dests})


def friends(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone' ]
        friend_name = request.POST['friend_name']
        friend_phone = request.POST['friend_phone']
        friend_email = request.POST['friend_email' ]
        friend_address = request.POST['fiend_address']
        category = request.POST['category']
        contacttime=request.POST['your_time']
        subject = " Welcome to DSoft Communications."
        your_message = request.POST['your_message']
        message = "Dear "+ friend_name + ",\n\n" \
                  + "Reference :- " + your_name + "\n\n" \
                  + "We like to introduce as one of the leading internet servive providers." + "\n" \
                  + "We are providing services for the last 10 years to valuable customers."+ "\n" \
                  + "We assure you are best services at all times."+ "\n\n" \
                  + "Our representative will contact you soon to explain the benefits and clarrify your doubts if any." + "\n" \
                  + "Warm Regards \n\n From: DSoft Support Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [ friend_email, settings.EMAIL_HOST_USER ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        referal = Referal(myname=your_name, mymobile = your_phone, referalname= friend_name,referalmobile = friend_phone, referalemail = friend_email, referaladdress= friend_address,category=category,contacttime=contacttime, message=your_message)
        referal.save()
        plan = Plan.objects.all()
        return render(request, 'travello/friends.html', {"plan": plan, 'your_name': your_name, 'friend_name': friend_name})
    else:
        plan = Plan.objects.all()
        return render(request, "travello/friends.html", {"plan": plan})


def destinations(request):
    dests = Destination.objects.all()
    return render(request, "travello/destinations.html", {"dests": dests})


def slider(request):
    dests = Destination.objects.all()
    return render(request, "travello/slider.html", {"dests": dests})

def contact(request):
    if request.method == "POST":
        input_name = request.POST[ 'input_name' ]
        contact_input_email = request.POST[ 'contact_input_email' ]
        contact_input_subject = request.POST[ 'contact_input_subject' ]
        contact_input_mobile = request.POST[ 'contact_input_mobile' ]
        contact_input = request.POST[ 'contact_input' ]
        mobile = request.POST['contact_input_mobile' ]
        subject = "Thank you for contacting DSoft."
        message = "Dear " + input_name + ",\n\n"  \
                  + "We will get in touch with you soon."+"\n\n\n"\
                  + "Your message details : -"+"\n" \
                  + "Message From-" + input_name + "\n" \
                  + "Email:-" + contact_input_email + "\n\n" \
                  + "Mobile:-" + mobile + "\n\n" \
                  + "Subject-" + contact_input_subject + "\n\n" \
                  + "Details-" + contact_input+"\n\n\n" \
                  + "Warm Regards \n\n From: DSoft Support Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [contact_input_email, settings.EMAIL_HOST_USER ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        name = request.POST['input_name' ]
        email = request.POST['contact_input_email']
        subject = request.POST['contact_input_subject']
        message = request.POST['contact_input']
        engineer = "eng"
        comments = "nnn"
        status = 'Reg'
        contactme = Contactme(name=name, email=email,  mobile=mobile, subject=subject, message=message)
        contactme.save()
        return render(request, 'travello/contact.html', {'contact_input_name': input_name})
    else:
        return render(request, "travello/contact.html", {})


def home(request):
    dests = Destination.objects.all().order_by('id')
    return render(request, "travello/home.html", {"dests": dests})


def managecustomer(request):
    return render(request, "travello/managecustomer.html", {})


def dashboard(request):
    return render(request, "travello/dashboard.html", {})


def customer(request):
    return render(request, "travello/customer.html", {})


def product(request):
    return render(request, "travello/products.html", {})

def about(request):
    dests = Destination.objects.all()
    return render(request, "travello/about.html", {"dests": dests})


def display_contact(request):
    items = Contactme.objects.all().order_by('-id')
    context = {
        'items': items,
        'header': 'Contact',
    }
    return render(request, 'travello/managecustomer.html', context)


def display_referal(request):
    items = Referal.objects.all().order_by('-id')
    context = {
        'items': items,
        'header': 'Referal',
    }
    return render(request, 'travello/referal.html', context)


def display_customer(request):
    items = Newcustomer.objects.all().order_by('-id')
    context = {
        'items': items,
        'header': 'NewCustomer',
    }
    return render(request, 'travello/newcustomer.html', context)

def display_feasable(request):
    items = Feasable.objects.all()
    context = {
        'items': items,
        'header': 'Feasable',
    }
    return render(request, 'travello/feasablty.html', context)


def display_plan(request):
    items = Plan.objects.all()
    context = {
        'items': items,
        'header': 'Plan',
    }
    return render(request, 'travello/plan.html', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('managecustomer')

    else:
        form = cls()
        return render(request, 'travello/add_new.html', {'form': form})



def add_contact(request):
    return add_item(request, ContactForm)

def add_customer(request):
    return add_item(request, CustomerForm)

def add_referal(request):
    return add_item(request, ReferalForm)


def add_feasable(request):
    return add_item(request, FeasableForm)


def add_newcustomer(request):
    if request.method == "POST":
        form = NewcustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewcustomerForm()
        return render(request, 'travello/add_newcustomer.html', {'form': form})


def success(request):
    return  HttpResponse('successfully uploaded')


def add_plan(request):
    return add_item(request, PlanForm)


def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('managecustomer')
    else:
        form = cls(instance=item)
        return render(request, 'travello/edit_item.html', {'form': form})


def edit_referal(request, pk):
    return edit_device(request, pk, Referal, ReferalForm)


def edit_contact(request, pk):
    return edit_device(request, pk, Contactme, ContactForm)


def edit_customer(request, pk):
    return edit_device(request, pk, Newcustomer, CustomerForm)


def edit_feasable(request, pk):
    return edit_device(request, pk, Feasable, FeasableForm)


def edit_plan(request, pk):
    return edit_device(request, pk, Plan, PlanForm)


def delete_plan(request, pk):

    template = 'travello/plan.html'
    Plan.objects.filter(id=pk).delete()
    items = Plan.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_feasable(request, pk):

    template = 'travello/feasablty.html'
    Feasable.objects.filter(id=pk).delete()
    items = Feasable.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)