from django.contrib import admin
from events.models import acc_crt
from events.models import create_poc
from events.models import details_comp

# Register your models here.
admin.site.register(acc_crt)
admin.site.register(create_poc)
admin.site.register(details_comp)
