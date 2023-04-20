from django.shortcuts import render
from .models import Question
from .models import MainCategoryFood
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

    return render(request, "person.html",{'msg':"Data Saved Successfully",'obj':obj})


