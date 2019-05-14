from django.shortcuts import render
from django.http import HttpResponse
import django.views.decorators.csrf

from .models import Greeting
from .helloworld import sayhello
from .extract_registration import parsevin, decodevin
from .extract_license import extractinfo
from .insurancecalculator import calcinsurance

userprofile = dict()
qval = 0

# Create your views here.
def index(request):
	userprofile.clear()
	return render(request, "index.html")

def dlphoto(request):
	return render(request, "dlphoto.html")

def postdlphoto(request):
	adddlinfo()

	return render(request, "regphoto.html")

def regphoto(request):
	return render(request, "regphoto.html")

def postregphoto(request):
	addreginfo()

	return render(request, "carphoto.html")

def carphoto(request):
	return render(request, "carphoto.html")

def postcarphoto(request):
	return render(request, "userform.html", userprofile)

def userform(request):
	return render(request, "userform.html", userprofile)

def postuserform(request):
    global qval
    data = request.POST.copy()
    qval = calcinsurance(data)
    return render(request, "quote.html", {"yourquote":qval})

def quote(request):
	return render(request, "quote.html")

def updatedquote(request):
    uval = (int)(qval * 0.9)
    return render(request, "updatedquote.html", {"yournewquote":uval})

# def proofphoto(request):
#     return render(request, "proofphoto.html")

# def showphoto(request):
#     if request.method == 'POST':
#         form = request.FILES.size()
#         image = form.cleaned_data['image']

#     return render(request, "showphoto.html", {"image": image})

def generatejsonrequest(bytestream):
	return '{"requests":[{"image":{"content":' + str(bytestream) + '},"features":[{"type":"LABEL_DETECTION","maxResults":1}]}]}'

def adddlinfo():
    licinfo = extractinfo()
    userprofile["user_first_name"] = licinfo["firstname"]
    userprofile["user_middle_init"] = licinfo["middle_initial"]
    userprofile["user_last_name"] = licinfo["lastname"]
    userprofile["user_dob"] = "8/6/87"
    userprofile["user_address"] = licinfo["address"]
    return

def addreginfo():
    #userprofile["user_make"] = "Nissan"
    #userprofile["user_model"] = "Altima"
    #userprofile["user_year"] = "2015"
    userprofile["user_vin"] = parsevin()
    vindict = decodevin()
    userprofile["user_make"] = vindict["make"]
    userprofile["user_model"] = vindict["model"]
    userprofile["user_year"] = vindict["modelyear"]
    return

