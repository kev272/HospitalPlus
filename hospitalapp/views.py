from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from hospitalapp.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'About.html')

def serve(request):
    return render(request, 'services.html')

def departments(request):
    return render(request, 'Departments.html')

def doctors(request):
    return render(request, 'Doctors.html')
def contact(request):
   if request.method == "POST":
       mycontacts = Contact(
       name = request.POST['name'],
       email = request.POST['email'],
       subject = request.POST['subject'],
       message = request.POST['message'],

       )
       mycontacts.save()
       return redirect('/contacts')
   else:
       return render(request, 'Contact.html')
def appointment(request):
   if request.method == 'POST':
      myappointments = Appointment(
           name = request.POST['name'],
           email = request.POST['email'],
           phone = request.POST['phone'],
           date = request.POST['date'],
           department = request.POST['department'],
           doctor = request.POST['doctor'],
           message = request.POST['message'],
       )
      myappointments.save()
      return redirect('/show')
   else:
       return render(request,'Appointment.html')
def show(request):
    #to fetch info stored in models and display them
    all = appointment.objects.all() #appointment is the name of the model
    return render(request, 'show.html', {'all': all})

def delete(request,id):
    deleteappointment = appointment.objects.get(id=id) #name of model
    deleteappointment.delete()
    return redirect("/show")

def edit(request,id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        appointment.name = request.POST.get('name')
        appointment.email = request.POST.get('email')
        appointment.phone = request.POST.get('phone')
        appointment.date = request.POST.get('date')
        appointment.department = request.POST.get('department')
        appointment.doctor = request.POST.get('doctor')
        appointment.message = request.POST.get('message')
        appointment.save()
        return redirect("/show")

    else:
        return render(request,'Edit.html' , {'appointment':appointment})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')