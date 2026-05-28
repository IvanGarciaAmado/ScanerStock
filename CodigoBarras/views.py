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
                context={"response":"Objeto encontrado"}
            else:
                return redirect(new_item_view)
        else:
            context={"response":"Introduce un código de barras"}
        return render(request,"scanner.html",context)
    
def new_item_view(request):
    context={}
    if request.method == "POST":
        bar_code=request.POST.get("bar_code")
        name=request.POST.get("name")

        response=add_new_item(bar_code, name)
        context={"response":response}
    
    return render(request,"new_item.html",context)

