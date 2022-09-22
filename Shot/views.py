from django.shortcuts import render,redirect
from . models import Post, ContactUs

# Create your views here.
def home(request):
    p = Post.objects.all()
    return render(request,'home.html',{'mypost':p})

def profile(request):
    return render(request,'profile.html')

# def contact(request):
#     return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        form = ContactUs(first=first, last=last, email=email,
                         phone=phone, message=message)
        form.save()
        return redirect("contact1")
    return render(request, 'contact.html', context={})


def contact1(request):
    if request.method == "POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        form = ContactUs(first=first, last=last, email=email,phone=phone, message=message)
        form.save()
        return redirect("contact1")
    return render(request, 'contact1.html', context={})

