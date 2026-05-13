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
    


