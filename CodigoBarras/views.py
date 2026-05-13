from django.template import loader
from django.shortcuts import render
from Model.models import *


def scannerView(request):

    if request.method == "GET":
        return render(request, "scanner.html")
    
    elif request.method == "POST":
        barCodeValue=request.POST.get("barCode")
        item=browseReferenceTable(barCodeValue)
        response=""
        if item == False:
            createNewItem(request)
        else:
            if request.POST.get("name") == "add":
                modifyQuantity(item,1)
                response="Se ha añadido un item"
                
            elif request.POST.get("name") == "substract":
                modifyQuantity(item,-1)
                response="Se ha quitado un item"

        context={response:"response"}
        return render(request, "scanner.html",context)    
    
def createNewItem(request):

    return render(request, "newItem.html")