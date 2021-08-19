from django.shortcuts import get_object_or_404, render
from .models import Image
from .models import services 
from .models import faq 

# Create your views here.
    
def index(request):
    pics=Image.objects.all()
    service=services.objects.all()
    faqs=faq.objects.all()
   
    return render(request,"gnpps/index.html",{
    "pics":pics,
    "service":service,
    "faq":faqs,
    
    })
