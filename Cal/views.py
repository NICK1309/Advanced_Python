from django.shortcuts import render
from .models import Question
from .models import MainCategoryFood
from .models import Tables
from .models import Waiters
from .models import bookOrders
# Create your views here.
# def index(request):
#     return render(request,"index.html")

def assesment(request):
    objQuestion = Question.objects.all()
    return render(request,"Question.html",{'objQuestion':objQuestion})

def person(request):
    return render(request, "person.html")

def savePersonData(request):
    f_name = request.POST["mainStreamFoodName"]    
    f_charge = request.POST["subCategoryFoodCharge"] 
     

    p_obj = MainCategoryFood(mainStreamFoodName =f_name,subCategoryFoodCharge=f_charge)
    p_obj.save() # to save the data
    obj = MainCategoryFood.objects.all()

    return render(request, "Question.html",{'msg':"Data Saved Successfully",'obj':obj}) #
    #-----------------------------------------------
def savePerson_Data(request):
    t_name = request.POST["tName"]    
     
    p_obj1 = Tables(tName = t_name)
    p_obj1.save() # to save the data
    obj1 = Tables.objects.all()

    return render(request, "Question.html",{'msg':"Data Saved Successfully",'obj1':obj1})    

#----------------------------------------------
def savePerson_Data1(request):
    w_name = request.POST["waiterName"]    
     
    p_obj2 = Waiters(waiterName = w_name)
    p_obj2.save() # to save the data
    obj2 = Waiters.objects.all()

    return render(request, "Question.html",{'msg':"Data Saved Successfully",'obj2':obj2}) 

#------------------------------------------------       
def savePerson_Data2(request):
    food_name = request.POST["foodName"]
    food_prize = request.POST["foodPrize"] 
    n_table = request.POST["nameOfTable"] 
    n_waiter = request.POST["nameOfWaiter"]     
     
    p_obj3 = bookOrders(foodName = food_name, foodPrize = food_prize,nameOfTable = n_table,nameOfWaiter = n_waiter)
    p_obj3.save() # to save the data
    obj3 = bookOrders.objects.all()

    return render(request, "Question.html",{'msg':"Data Saved Successfully",'obj3':obj3}) 

