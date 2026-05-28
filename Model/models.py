from django.db import models
from Model import Product

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()

class ReferenceTable(models.Model):
    barCode=models.IntegerField()
    friendlyId=models.IntegerField()


def browseReferenceTable(barCode:int):
    try:
        RTItem=ReferenceTable.objects.get(barCode=barCode)
        browseStock(RTItem.friendlyId)
        
    except:
        return False

def browseStock(friendlyIdParameter:int):
    StockItem=Stock.objects.get(friendlyId=friendlyIdParameter)
    return StockItem

def modifyQuantity(item,quantity):
    item.quantity += quantity
    item.save()
    product=Product(item.name, item.quantity)
    return product.str()

def get_item_by_barcode(bar_code:int):
    try:
        reference_table_item=ReferenceTable.objects.get(barCode=bar_code)
        stock_item=Stock.objects.get(id=reference_table_item.friendlyId)
        return stock_item
    except:
        return None


#hayq ue crear unos cuentos objetos en las bbdd y crear el flujo de creacion de objetos desde el principio para probarlo bien
def add_new_item(bar_code_value, name_value):
    reference_table_item=ReferenceTable.objects.create(barCode=bar_code_value, friendlyId=0)
    try:
        stock_item=Stock.objects.get(name=name_value)
    except Stock.DoesNotExist:
        stock_item=None

    if stock_item is not None:
        friendly_id=stock_item.id
        reference_table_item.friendlyId=friendly_id
        reference_table_item.save()
        response="Stock item: ",Stock.objects.get(id=stock_item.id)
    else:
        new_stock_item=Stock.objects.create(name=name_value, quantity=1)
        reference_table_item.friendlyId = new_stock_item.id
        reference_table_item.save()
        response="Se crea el objeto",new_stock_item
    
    return response
    


