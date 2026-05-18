from django.db import models
from Model import Product

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()

class ReferenceTable(models.Model):
    barCode=models.IntegerField()
    friendyId=models.IntegerField()


def browseReferenceTable(barCode:int):
    try:
        RTItem=ReferenceTable.objects.get(barCode=barCode)
        browseStock(RTItem.friendyId)
        
    except:
        return False

def browseStock(friendyIdParameter:int):
    StockItem=Stock.objects.get(friendyId=friendyIdParameter)
    return StockItem

def modifyQuantity(item,quantity):
    item.quantity += quantity
    item.save()
    product=Product(item.name, item.quantity)
    return product.str()

def add_new_item(bar_code_value, name):
    ReferenceTable.objects.create(barCode=bar_code_value,friendyId=0)
    reference_table_item=ReferenceTable.objects.get(barCode=bar_code_value)
    
    stock_item=Stock.objects.get(name=name)

    if stock_item:
        friendly_id=stock_item.id
        ReferenceTable.objects.update(friendlyId=friendly_id)
    else:
        new_stock_item=Stock.objects.create(name=name, quantity=1)
        ReferenceTable.objects.update(friendlyId=new_stock_item.id)
    
    response="Stock item: ",Stock,object.get(id=stock_item.id),"Reference item: ",ReferenceTable.object.get(friendlyId=stock_item.id)
    return response
    


