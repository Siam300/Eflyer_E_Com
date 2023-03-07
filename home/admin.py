from django.contrib import admin

# Register your models here.

from .models import manTshirt, manShirt, womanScart,laptop, mobile, computer, jumkas, kangans, necklaces

admin.site.register(manTshirt)
admin.site.register(manShirt)
admin.site.register(womanScart)

admin.site.register(laptop)
admin.site.register(mobile)
admin.site.register(computer)

admin.site.register(jumkas)
admin.site.register(kangans)
admin.site.register(necklaces)