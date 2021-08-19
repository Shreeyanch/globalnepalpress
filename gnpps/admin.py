from django.contrib import admin
from .models import Image
from .models import services , faq

# Register your models here.
admin.site.register(Image)
admin.site.register(services)
admin.site.register(faq)

