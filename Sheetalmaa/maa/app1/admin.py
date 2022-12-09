from django.contrib import admin

from .models import Customer
admin.site.register(Customer)

from .models import Product
admin.site.register(Product)

from .models import Order
admin.site.register(Order)

from .models import Tag
admin.site.register(Tag)

from .models import Name
admin.site.register(Name)

from .models import Fast
admin.site.register(Fast)
from .models import oom
admin.site.register(oom)

# Register your models here.
