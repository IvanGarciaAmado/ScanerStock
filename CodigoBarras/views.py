from django.template import loader
from django.shortcuts import render,redirect
from Model.models import *


def scanner_view(request):
    if request.method == "GET":
        return render(request,"scanner.html")
    
    elif request.method == "POST":
        bar_code=request.POST.get("bar_code")
        if bar_code:
            found_stock_item=get_item_by_barcode(bar_code)
            if found_stock_item:
                context={"response":f"{found_stock_item.name} x{found_stock_item.quantity}"}
            else:
                return redirect(new_item_view)
        else:
            context={
                "response":"Introduce un código de barras"
                }
        return render(request,"scanner.html",context)
    
def new_item_view(request):
    context={}
    if request.method == "POST":
        bar_code=request.POST.get("bar_code")
        name=request.POST.get("name")

        response=add_new_item(bar_code, name)
        context={"response":response}
    
    return render(request,"new_item.html",context)

def template_modif_quantity(request):
    context={}
    quantity=request.POST.get("quantity")
    if quantity is "":
        quantity=1
    bar_code=request.POST.get("bar_code")
    item=get_item_by_barcode(bar_code)

    if request.POST.get("action") == "Sumar":
        print("se añade",quantity)
        modifyQuantity(item,int(quantity))
    elif request.POST.get("action") == "Restar":
        print("se quita",quantity)
        modifyQuantity(item,-int(quantity))
    return render(request,"template_modif_quantity.html",context)

def home(request):
    if request.method== "POST":
        if request.POST.get("action") == "Scanner":
            return redirect(scanner_view)
        elif request.POST.get("action") == "Añadir nuevo objeto":
            return redirect(new_item_view)
        elif request.POST.get("action") == "Sumar/Restar":
            return redirect(template_modif_quantity)
    else:
        return render(request,"home.html")

