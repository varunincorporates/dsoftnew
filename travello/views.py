from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from telusko import settings
from .decorators import unauthenticated_user
from .forms import *
from .filters import *
from .models import *
from django.forms import inlineformset_factory
from django.core.paginator import Paginator, EmptyPage
from .views import *
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, auth
from django.contrib import messages


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Newcustomer.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'travello/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'travello/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    dests = Destination.objects.all()
    return render(request, "travello/home.html", {"dests": dests})


def salesfaq(request):
    feasable = Feasable.objects.all().order_by('-id')
    myFilter = FeasableFilter(request.GET, queryset=feasable)
    feasable = myFilter.qs[ :5 ]

    salesfaq = Salesfaq.objects.all().order_by('serial')
    return render(request, "travello/salesfaq.html", {'feasable':feasable, 'myFilter': myFilter,"dests": salesfaq})


def document(request):
    obj = Item.objects.all()
    return render(request, 'travello/document.html', {'obj': obj})


def indexdas(request):
    obj = Item.objects.all()
    return render(request, 'travello/indexdas.html', {'obj': obj})


def friends(request):
    if request.method == "POST":
        your_name = request.POST[ 'your_name' ]
        your_phone = request.POST[ 'your_phone' ]
        friend_name = request.POST[ 'friend_name' ]
        friend_phone = request.POST[ 'friend_phone' ]
        friend_email = request.POST[ 'friend_email' ]
        friend_address = request.POST[ 'fiend_address' ]
        category = request.POST[ 'category' ]
        contacttime = request.POST[ 'your_time' ]
        subject = " Welcome to DSoft Communications."
        your_message = request.POST[ 'your_message' ]
        message = "Dear " + friend_name + ",\n\n" \
                  + "Reference :- " + your_name + "\n\n" \
                  + "We like to introduce as one of the leading internet servive providers." + "\n" \
                  + "We are providing services for the last 10 years to valuable customers." + "\n" \
                  + "We assure you are best services at all times." + "\n\n" \
                  + "Our representative will contact you soon to explain the benefits and clarrify your doubts if any." + "\n" \
                  + "Warm Regards \n\n From: DSoft Support Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [ friend_email, settings.EMAIL_HOST_USER ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        referal = Referal(myname=your_name, mymobile=your_phone, referalname=friend_name, referalmobile=friend_phone,
                          referalemail=friend_email, referaladdress=friend_address, category=category,
                          contacttime=contacttime, message=your_message)
        referal.save()
        plan = Plan.objects.all()
        return render(request, 'travello/friends.html',
                      {"plan": plan, 'your_name': your_name, 'friend_name': friend_name})
    else:
        plan = Plan.objects.all()
        return render(request, "travello/friends.html", {"plan": plan})


def destinations(request):
    feasable = Feasable.objects.all().order_by('-id')
    myFilter = FeasableFilter(request.GET, queryset=feasable)
    feasable = myFilter.qs[ :5 ]
    dests = Destination.objects.all()
    return render(request, "travello/destinations.html", {"feasable":feasable, "myFilter":myFilter, "dests": dests})


def slider(request):
    dests = Destination.objects.all()
    return render(request, "travello/slider.html", {"dests": dests})


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        input_name = request.POST[ 'input_name' ]
        contact_input_email = request.POST[ 'contact_input_email' ]
        contact_input_subject = request.POST[ 'contact_input_subject' ]
        contact_input_mobile = request.POST[ 'contact_input_mobile' ]
        contact_input = request.POST[ 'contact_input' ]
        mobile = request.POST[ 'contact_input_mobile' ]
        subject = "Thank you for contacting DSoft."
        message = "Dear " + input_name + ",\n\n" \
                  + "We will get in touch with you soon." + "\n\n\n" \
                  + "Your message details : -" + "\n" \
                  + "Message From-" + input_name + "\n" \
                  + "Email:-" + contact_input_email + "\n\n" \
                  + "Mobile:-" + mobile + "\n\n" \
                  + "Subject-" + contact_input_subject + "\n\n" \
                  + "Details-" + contact_input + "\n\n\n" \
                  + "Warm Regards \n\n From: DSoft Support Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [ contact_input_email, settings.EMAIL_HOST_USER ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        name = request.POST[ 'input_name' ]
        email = request.POST[ 'contact_input_email' ]
        subject = request.POST[ 'contact_input_subject' ]
        message = request.POST[ 'contact_input' ]
        contactme = Contactme(name=name, email=email, mobile=mobile, subject=subject, message=message)
        contactme.save()
        dest = Contactme.objects.filter(name=name, email=email, mobile=mobile, message=message).order_by('-id')[ :1 ]

        feasable = Feasable.objects.all().order_by('-id')
        myFilter = FeasableFilter(request.GET, queryset=feasable)
        feasable = myFilter.qs[ :5 ]

        context = {
            'contact_input_name': input_name,
            'dest': dest,
            'header': 'Contact',
            "feasable": feasable,
            'myFilter': myFilter,
        }
        return render(request, 'travello/contact.html',context )
    else:
        feasable = Feasable.objects.all().order_by('-id')
        myFilter = FeasableFilter(request.GET, queryset=feasable)
        feasable = myFilter.qs[ :5 ]
        context = {
            'header': 'Contact',
            "feasable": feasable,
            'myFilter': myFilter,
        }
        return render(request, "travello/contact.html", context)


def home(request):
    dests = Destination.objects.all().order_by('id')

    feasable = Feasable.objects.all().order_by('-id')
    myFilter = FeasableFilter(request.GET, queryset=feasable)
    feasable = myFilter.qs[:5]

    context = {
        "dests": dests,
        "feasable": feasable,
        'myFilter': myFilter,
    }
    return render(request, "travello/home.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'customer', 'admin', 'staff' ])
def managecustomer(request):
    return render(request, "travello/managecustomer.html", {})


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'customer', 'admin', 'staff' ])
def maindashboard(request):
    return render(request, "travello/maindashboard.html", {})


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def dashboard(request):
    orders = Myorder.objects.all().order_by('-id')
    p = Paginator(orders, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    customers = Newcustomer.objects.all().order_by('-id')
    myFilter = CustomerFilter(request.GET, queryset=customers)
    customers = myFilter.qs

    p = Paginator(customers, 10)
    page_num = request.GET.get('page', 1)
    try:
        page1 = p.page(page_num)
    except EmptyPage:
        page1 = p.page(1)

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': page,
        'customers': page1,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'myFilter': myFilter,
    }
    return render(request, "travello/dashboard.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def dashcomplain(request):
    orders = Newcomplain.objects.all().order_by('-id')

    customers = Newcomplain.objects.all().order_by('-id')

    myFilter = ComplainFilter(request.GET, queryset=customers)
    orders = myFilter.qs

    p = Paginator(orders, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='SOLVED').count()
    pending = orders.filter(status='PENDING').count()
    context = {
        'orders': page,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'myFilter': myFilter,
    }
    return render(request, "travello/dashcomplain.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def customer(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    orders = Myorder.objects.filter(name=customer.id)
    installation = Installation.objects.filter(name=customer.id)

    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'installations': installation,
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, "travello/customer.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def product(request):
    items = Plan.objects.all().order_by('-id')
    context = {
        'items': items,
        'header': 'Contact',
    }
    return render(request, "travello/products.html", context)


def about(request):
    dests = Destination.objects.all()

    feasable = Feasable.objects.all().order_by('-id')
    myFilter = FeasableFilter(request.GET, queryset=feasable)
    feasable = myFilter.qs[ :5 ]

    header = "About Us"

    context = {
        "dests": dests,
        "header":header,
        "feasable": feasable,
        'myFilter': myFilter,
    }

    return render(request, "travello/about.html", context )


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_contact(request):
    items = Contactme.objects.all().order_by('-id')

    feasable = Feasable.objects.all().order_by('-id')

    context = {
        'items': items,
        'header': 'Contact',
    }

    return render(request, 'travello/managecustomer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_referal(request):
    items = Referal.objects.all().order_by('-id')
    context = {
        'items': items,
        'header': 'Referal',
    }
    return render(request, 'travello/referal.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_customer(request):
    items = Newcustomer.objects.all().order_by('-id')
    context = {
        'items': items,
        'header': 'NewCustomer',
    }
    return render(request, 'travello/newcustomer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_feasable(request):
    items = Feasable.objects.all()
    context = {
        'items': items,
        'header': 'Feasable',
    }
    return render(request, 'travello/feasablty.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_plan(request):
    items = Plan.objects.all()
    context = {
        'items': items,
        'header': 'Plan',
    }
    return render(request, 'travello/plan.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_employee(request):
    items = Employee.objects.all()
    context = {
        'items': items,
        'header': 'Employee',
    }
    return render(request, 'travello/employee.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def display_faq(request):
    items = Salesfaq.objects.all().order_by('serial')
    context = {
        'items': items,
        'header': 'FAQ',
    }
    return render(request, 'travello/faq.html', context)


@login_required(login_url='login')
def add_item(request, cls, name, osite):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect(osite)

    else:
        header = name
        form = cls()
        return render(request, 'travello/add_new.html', {'form': form, 'header': header})


@login_required(login_url='login')
def add_contact(request):
    return add_item(request, ContactForm, 'Contact Customers', 'display_contact')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def add_customer(request):
    if request.method == "POST":
        form = NewcustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_customer')
    else:
        form = NewcustomerForm()
        return render(request, 'travello/add_newcustomer.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def add_dashcustomer(request):
    if request.method == "POST":
        form = NewcustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NewcustomerForm()
        return render(request, 'travello/add_newcustomer.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def add_referal(request):
    return add_item(request, ReferalForm, 'Referal Customers', 'display_referal')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def add_feasable(request):
    return add_item(request, FeasableForm, 'Feasabilty', 'display_feasable')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def add_newcustomer(request):
    feasable = Feasable.objects.all().order_by('-id')
    myFilter = FeasableFilter(request.GET, queryset=feasable)
    feasable = myFilter.qs[ :5 ]
    header="New Registeration Form"
    newcustomer = request.user.newcustomer
    form = NewcustomerForm(instance=newcustomer)
    if request.method == "POST":
        form = NewcustomerForm(request.POST, request.FILES, instance=newcustomer)
        if form.is_valid():
            contact_new_customer = request.POST.get('first_name')
            obj = form.save(commit=False)
            obj.name = contact_new_customer
            obj.save()
            messages.info(request, "Record Saved")
    context = {'form': form,
               "feasable": feasable,
               'myFilter': myFilter,
               'header': header,
               }
    return render(request, 'travello/add_newcustomer.html', context)


@login_required(login_url='login')
def add_complain(request):
    feasable = Feasable.objects.all().order_by('-id')
    myFilter = FeasableFilter(request.GET, queryset=feasable)
    feasable = myFilter.qs[ :5 ]

    if request.method == "POST":
        form = ComplainForm(request.POST, request.FILES)
        if form.is_valid():
            contact_new_customer = request.POST[ 'name' ]
            note = request.POST[ 'note' ]
            mobile = request.POST[ 'mobile' ]
            email = request.POST[ 'email' ]
            category = request.POST[ 'category' ]
            accountno = request.POST[ 'accountno' ]
            subject = request.POST[ 'subject' ]
            note = request.POST[ 'note' ]
            comments = "NEW"
            df = User.objects.get(id=request.user.id)
            dc = Newcomplain(user1=df, name=contact_new_customer, mobile=mobile, email=email,
                             accountno=accountno, category=category, subject=subject, note=note, comments=comments)
            dc.save()
            dest = Newcomplain.objects.filter(name=contact_new_customer, note=note).order_by('-id')
            msg = "Regards-DSoft(020)-27800000"
            url = "http: // site.bulksmsnagpur.net / sendsms?"
            apikey = "sunilj1"
            pwd = "sunilj1"
            senderid = "SUNILJ"

            sendsms(url, apikey, pwd, senderid, mobile, msg)
            return render(request, 'travello/add_newcustomer.html',
                          {'feasable':feasable, 'myFilter': myFilter, 'contact_new_customer': contact_new_customer, 'dest': dest})

    else:
        form = ComplainForm(
            initial={'profile_id': request.user.id, 'mobile': request.user.last_name, 'name': request.user,
                     'email': request.user.email})
        header = 'Customer Suggestion Form'
        return render(request, 'travello/add_newcustomer.html', {'feasable':feasable, 'myFilter': myFilter, 'form': form, 'header': header})





def sendsms(url, apikeys, pwds, senderids, tonumber, msg):
    apikey = apikeys
    pwd = pwds
    address = url
    senderid = senderids
    import requests
    # url = "http://site.bulksmsnagpur.net/sendsms?uname=" + apikey + "&pwd=" + pwd + "&senderid=" + senderid +
    # "&to=" + tonumber + "&msg=" + msg + "&route=T"
    url = "http://site.bulksmsnagpur.net/sendsms?uname=sunilj1&pwd=sunilj1&senderid=SUNILJ&to="
    url = url + tonumber
    url = url + "&msg=Dear Sir, We have received your request. DSoft engineers will get in touch soon. Regards DSoft Support. Helpline:020-27800000"
    url = url + "&route=T"
    response = requests.request('POST', url)
    return HttpResponse('successfully sent')


def success(request):
    return HttpResponse('successfully uploaded')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def add_plan(request):
    return add_item(request, PlanForm, 'Plan', 'display_plan')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def add_employee(request):
    return add_item(request, EmployeeForm, 'Employee', 'display_employee')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def add_faq(request):
    return add_item(request, FaqForm, 'FAQ', 'display_faq')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def createorder(request, pk):
    OrderFormSet = inlineformset_factory(Newcustomer, Myorder, fields=('product', 'status'), extra=5)
    customer = Newcustomer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Myorder.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/customer/' + str(pk))
    header = customer.name
    context = {'form': formset, 'header': header}
    return render(request, 'travello/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def updateorder(request, pk):
    dk = Myorder.objects.get(id=pk)
    customer = Newcustomer.objects.get(id=dk.name.id)
    orders = Myorder.objects.filter(name=customer.id)
    installation = Installation.objects.filter(name=customer.id)

    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'installations': installation,
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, "travello/customer.html", context)
    #  return edit_device(request, pk, Myorder, OrderForm, 'dashboard', 'Order Form')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def updatecomplain(request, pk):
    return edit_device(request, pk, Newcomplain, ComplainForm1, 'dashcomplain', 'Customer Complain Form')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'customer' ])
def userpage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='SOLVED').count()
    pending = orders.filter(status='PENDING').count()
    context = {'orders': orders}
    return render(request, 'travello/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def updateorder1(request, pk):
    pk2 = Myorder.objects.get(id=pk)
    dk = str(pk2.name.id)
    return edit_device(request, pk, Myorder, OrderForm, '/customer/' + str(dk), 'Order Form')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff'])
def edit_device(request, pk, model, cls, modname, header):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(modname)
    else:
        form = cls(instance=item)
        return render(request, 'travello/edit_item.html', {'form': form, 'header': header})


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_custimage(request, pk, model, cls, modname, header):
    item = get_object_or_404(model, pk=pk)
    dk = item.pan.url
    dk1 = item.adharcard.url
    dk2 = item.drivinglicence.url
    dk3 = item.electricitybill.url
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(modname)
    else:
        form = cls(instance=item)
        header = 'CUSTOMER'
        return render(request, 'travello/edit_item.html', {'form': form, 'header': header,'dk3' : dk3,  'dk' : dk, 'dk1' : dk1, 'dk2' : dk2 })


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_referal(request, pk):
    return edit_device(request, pk, Referal, ReferalForm, 'display_referal', 'Referal Customer')


@login_required(login_url='login')
def edit_contact(request, pk):
    return edit_device(request, pk, Contactme, ContactForm, 'display_contact', 'Contact Customer')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_customer(request, pk):
    pk2 = Newcustomer.objects.get(id=pk)
    return edit_custimage(request, pk, Newcustomer, CustomerForm, '/customer/' + str(pk), 'New Customer ' + pk2.name)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_inst(request, pk):
    installation = Installation.objects.get(id=pk)
    pk2 = installation.name.id
    pk3 = installation.name.name
    return edit_device(request, pk, Installation, InstallForm, '/customer/' + str(pk2),
                       'New Customer Installation-' + pk3)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_ococ(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id
        return edit_device(request, dk, Installation, InstallococForm, '/customer/' + str(pk),
                           'OCOC DETAILS FOR ' + installation.name.name)
    messages.info(request, "Approval Pending")
    return redirect('/customer/' + str(pk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_cable(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id
        return edit_device(request, dk, Installation, InstallcableForm, '/customer/' + str(pk),
                           'CABLING DETAILS FOR  ' + installation.name.name)
    messages.info(request, "Approval Pending")
    return redirect('/customer/' + str(pk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_pay(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id
        return edit_device(request, dk, Installation, InstallpayForm, '/customer/' + str(pk),
                           'PAYMENT REALISED DETAILS FOR  ' + installation.name.name)
    messages.info(request, "Approval Pending")
    return redirect('/customer/' + str(pk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_feedback(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id
        return edit_device(request, dk, Installation, InstallfeedForm, '/customer/' + str(pk),
                           'PAYMENT REALISED DETAILS FOR  ' + installation.name.name)
    messages.info(request, "Approval Pending")
    return redirect('/customer/' + str(pk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_date(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id
        return edit_device(request, dk, Installation, InstalldateForm, '/customer/' + str(pk),
                           'INSTALLED DATE DETAILS FOR  ' + installation.name.name)
    messages.info(request, "Approval Pending")
    return redirect('/customer/' + str(pk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_wo(request, pk):
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id
        return edit_device(request, dk, Installation, InstallwoForm, '/customer/' + str(pk),
                           'WORK ORDER DETAILS FOR  ' + installation.name.name)
    messages.info(request, "Approval Pending")
    return redirect('/customer/' + str(pk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_installation(request, pk):
    InstallationFormSet = inlineformset_factory(Newcustomer, Installation,
                                                fields=(
                                                    'building', 'flatno', 'phone', 'type', 'voip', 'userid', 'plan'),
                                                extra=1)
    customer = Newcustomer.objects.get(id=pk)
    if Installation.objects.filter(name=customer.id).exists():
        customer = Newcustomer.objects.get(id=pk)
        installation = Installation.objects.get(name=customer.id)
        dk = installation.id

        return edit_device(request, dk, Installation, InstallationForm, '/customer/' + str(pk),
                           'APPROVAL FROM FRONT END FOR -  ' + installation.name.name)

    formset = InstallationFormSet(queryset=Installation.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = InstallationFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/customer/' + str(pk))
    header = customer.name
    context = {'form': formset, 'header': header}
    return render(request, 'travello/installation_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_dcustomer(request, pk):
    return edit_device(request, pk, Newcustomer, CustomerForm, '/customer/' + str(pk), 'New Customer')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_feasable(request, pk):
    return edit_device(request, pk, Feasable, FeasableForm, 'display_feasable', 'Feasable')

@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_ord(request, pk):
    return edit_device(request, pk, Myorder, OrderForm, 'customer', 'Myorder')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_plan(request, pk):
    return edit_device(request, pk, Plan, PlanForm, 'display_plan', 'Plan')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_employee(request, pk):
    return edit_device(request, pk, Employee, EmployeeForm, 'display_employee', 'Employee')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def edit_faq(request, pk):
    return edit_device(request, pk, Salesfaq, FaqForm, 'display_faq', 'FAQ')


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def delete_plan(request, pk):
    template = 'travello/plan.html'
    Plan.objects.filter(id=pk).delete()
    items = Plan.objects.all()

    context = {
        'items': items,
        'header': 'PLAN'
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def delete_order(request, pk):
    customer = Myorder.objects.get(id=pk)
    dk = customer.name.id
    Myorder.objects.filter(id=pk).delete()
    return redirect('/customer/' + str(dk))


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def delete_faq(request, pk):
    template = 'travello/faq.html'
    Salesfaq.objects.filter(id=pk).delete()
    items = Salesfaq.objects.all()

    context = {
        'items': items,
        'header': 'FAQ'
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def delete_feasable(request, pk):
    template = 'travello/feasablty.html'
    Feasable.objects.filter(id=pk).delete()
    items = Feasable.objects.all()
    header = 'Feasable'
    context = {
        'items': items,
        'header': 'Feasable'
    }

    return render(request, template, context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def delete_dashcomplain(request, pk):
    template = 'travello/dashcomplain.html'
    Newcomplain.objects.filter(id=pk).delete()

    orders = Newcomplain.objects.all().order_by('-id')

    customers = Newcomplain.objects.all().order_by('-id')

    myFilter = ComplainFilter(request.GET, queryset=customers)
    orders = myFilter.qs

    p = Paginator(orders, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='SOLVED').count()
    pending = orders.filter(status='PENDING').count()
    context = {
        'orders': page,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'myFilter': myFilter,
    }
    return render(request, "travello/dashcomplain.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=[ 'admin', 'staff' ])
def delete_dashboard(request, pk):
    template = 'travello/dashboard.html'
    Myorder.objects.filter(id=pk).delete()
    orders = Myorder.objects.all().order_by('-id')
    p = Paginator(orders, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    customers = Newcustomer.objects.all().order_by('-id')
    myfilter = CustomerFilter(request.GET, queryset=customers)
    customers = myfilter.qs

    p = Paginator(customers, 10)
    page_num = request.GET.get('page', 1)
    try:
        page1 = p.page(page_num)
    except EmptyPage:
        page1 = p.page(1)

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='SOLVED').count()
    pending = orders.filter(status='PENDING').count()
    context = {
        'orders': page,
        'customers': page1,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'myFilter': myfilter,
    }
    return render(request, template, context)

@login_required(login_url='login')
def newsletter(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        df = User.objects.get(id=request.user.id)
        newsletter = Newsletter(user1=df, name=name, email=email)
        newsletter.save
        dest = Destination.objects.all()
        messages.success(request, 'Subscription account created  for ' + name)
        contact1_input_name=name
        return render(request, 'travello/home.html',{"dest": dest,'contact1_input_name':contact1_input_name})
    else:
        dest = Destination.objects.all()
        return render(request, 'travello/home.html', {"dest": dest, })
