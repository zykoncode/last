from django.shortcuts import render,redirect,reverse
from .models import Enquiry,Complain,Career,LoginInfo
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from . import smssender
from adminzone.models import Notification,Consignment

# Create your views here.
def index(request):
    nf=Notification.objects.all()
    return render(request,'index.html',{'nf':nf})
def contact(request):
    nf=Notification.objects.all()
    return render(request,'contact.html',{'nf':nf})
    def savecomplain(request):
        name=request.POST['name']
        contactno = request.POST['contactno']
        emailaddress = request.POST['emailaddress']
        complaintext = request.POST['complaintext']
        complaindate=datetime.datetime.now().strftime('%Y/%m/%d')
        en=Complain(name=name,contactno=contactno,emailaddress=emailaddress,complaintext=complaintext,complaindate=complaindate)
        en.save()
        return redirect('index')
def track_shipment(request):
    nf=Notification.objects.all()
    return render(request,'track_shipment.html',{'nf':nf})
def login(request):
    nf=Notification.objects.all()
    return render(request,'login.html',{'nf':nf})
def career(request):
    nf=Notification.objects.all()
    if request.method=='POST' and request.FILES['myfile']:
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        qualification=request.POST['qualification']
        experience=request.POST['experience']
        keyskills=request.POST['keyskills']
        myfile=request.FILES['myfile']
        cv=myfile.name
        connectdate = datetime.datetime.now().strftime('%Y/%m/%d')
        if Career.objects.filter(emailaddress=emailaddress).exists():
            msg='The user already registered'
        else:
            c=Career(name=name,keyskills=keyskills,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,qualification=qualification,experience=experience,cv=cv,connectdate=connectdate)
            c.save()
            fs=FileSystemStorage()
            fs.save(cv,myfile)
            msg='Your registration is done.'
        return render(request,'career.html',{'msg':msg},{'nf':nf})
    return render(request,'career.html',{'nf':nf})
def complain(request):
    nf=Notification.objects.all()
    return render(request,'complain.html',{'nf':nf})
def enquiry(request):
    nf=Notification.objects.all()
    return render(request,'enquiry.html',{'nf':nf})
def about(request):
    nf=Notification.objects.all()
    return render(request,'about.html',{'nf':nf})
def saveenquiry(request):
    name=request.POST['name']
    gender=request.POST['gen']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.now().strftime('%Y/%m/%d')
    e=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    e.save()
    #smssender.sendsms(contactno,'''Thanks for enquiry!
    #We will contact you soon.

    #-Team HR''')
    return redirect('index')
def savecomplain(request):
    name=request.POST['name']
    contactno = request.POST['contactno']
    emailaddress = request.POST['emailaddress']
    complaintext = request.POST['complaintext']
    complaindate=datetime.datetime.now().strftime('%Y/%m/%d')
    en=Complain(name=name,contactno=contactno,emailaddress=emailaddress,complaintext=complaintext,complaindate=complaindate)
    en.save()
    return redirect('index')
def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        v=LoginInfo.objects.get(userid=userid,password=password)
        if v is not None:
            request.session['userid']=userid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        return redirect('login')
def search(request):
    try:
        refNo=request.POST['refNo']
        con=Consignment.objects.get(refNo=refNo)
        return  render(request,'track_shipment.html',{'con':con})
    except ObjectDoesNotExist:
        return render(request, 'track_shipmenterror.html')
