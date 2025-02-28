from django.shortcuts import render,redirect
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
       return redirect('/contacts/')
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
      return redirect('/Appointment/')
   else:
       return render(request,'Appointment.html')
