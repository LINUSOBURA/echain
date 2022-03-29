from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Evidence, Case
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.signing import Signer
from django.core import signing

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def home(request):
    return render(request, 'home.html')


def create_case(request):
    if request.method == 'POST':
        caseNumber = request.POST['caseNumber']
        creator = request.POST['creator']
        starting_date = request.POST['date']

        new_case = Case(caseNumber=caseNumber, creator=creator,
                        starting_date=starting_date)

        new_case.save()
        messages.info(request, 'Case created successfully.')

        return redirect( 'cases')
        
    else:
        return render(request, 'create_case.html')



def cases(request):
    cases = Case.objects.all()
    return render(request, 'cases.html', {'cases': cases})


def case(request, pk):
    cases = Case.objects.get(id=pk)
    return render(request, 'case.html', {'cases': cases})


def evidence(request):
    evidences = Evidence.objects.all()
    return render(request, 'evidence.html', {'evidences': evidences})

def s_evidence(request, pk):
    evidences = Evidence.objects.get(id=pk)
    #signer = Signer()
    #try:
        #evidences = signer.unsign(Evidence.description)
    #except signing.BadSignature:
        #messages.info(request, 'This evidence has been tampered with')
    

    return render(request, 's_evidence.html', {'evidences': evidences})

def check_integrity(request):
    integrity = Evidence.objects.all()
    if integrity.id == 11:
        messages.info(request, 'Evidence is OK')
    else:
        messages.info(request, 'Evedence has been tampered with')
        
    return render(request, 'integrity.html', {'integrity': integrity})

new_evidence = ()

def add_evidence(request):
    if request.method == 'POST':
        caseNumber = request.POST['caseNumber']
        creator = request.POST['creator']
        date = request.POST['date']
        description = request.POST['description']
        
        #signer = Signer()

        new_evidence = Evidence(
            caseNumber=caseNumber, creator=creator, date=date, description=description)

        new_evidence.save()


        messages.info(request, 'Evidence added successfully.')
    return render(request, 'add_evidence.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

# Authenticating if the user is real or not.
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def closed(request):
    return render(request, 'closedcases.html')