from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your message submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'Oops! Something goes wrong!')
            
    form = ContactForm()
    return render(request,'index.html',{'form':form})
