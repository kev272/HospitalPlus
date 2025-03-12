import json

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from requests.auth import HTTPBasicAuth

from hospitalapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
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
    all = Appointment.objects.all() #appointment is the name of the model
    return render(request, 'Show.html', {'all': all})

def delete(request,id):
    deleteappointment = Appointment.objects.get(id=id) #name of model
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

    return render(request, 'Register.html')

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

    return render(request, 'Login.html')
#mpesa API
def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request_data, headers=headers)

        # Parse response
        response_data = response.json()
        transaction_id = response_data.get("CheckoutRequestID", "N/A")
        result_code = response_data.get("ResponseCode", "1")  # 0 is success, 1 is failure

        # Save transaction to database
        transaction = Transaction(
            phone_number=phone,
            amount=amount,
            transaction_id=transaction_id,
            status="Success" if result_code == "0" else "Failed"
        )
        transaction.save()

        return HttpResponse(
            f"Transaction ID: {transaction_id}, Status: {'Success' if result_code == '0' else 'Failed'}")


def transactions_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transactions.html', {'transactions': transactions})