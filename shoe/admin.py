from django.contrib import admin
from shoe.models import ShoeType, ShoeColor, Shoe
# Register your models here.

admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
