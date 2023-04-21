from django.contrib import admin
 #from Cal.models import Question
# from Faculty.models import Teacher
# from Nikita.models import Table
from .models import MainCategoryFood
from .models import Tables
from .models import Waiters
from .models import bookOrders
# Register your models here.

 #admin.site.register(Question)
#admin.site.register(Table)
admin.site.register(MainCategoryFood)
admin.site.register(Tables)
admin.site.register(Waiters)
admin.site.register(bookOrders)