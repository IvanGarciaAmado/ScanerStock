from django.db import models

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()

class reference_table(models.Model):
    bar_code=models.IntegerField()
    friendlyId=models.IntegerField()


def search_reference_table(bar_code:int):
    try:
        referece_table_item=reference_table.objects.get(bar_code=bar_code)
        search_stock(referece_table_item.friendlyId)
        
    except:
        return False

def search_stock(friendly_id_parameter:int):
    stock_item=Stock.objects.get(friendlyId=friendly_id_parameter)
    return stock_item

def modify_quantity(item:int,quantity:int):
    item.quantity += quantity
    item.save()
    print(item.quantity)

def get_item_by_bar_code(bar_code:int):
    try:
        reference_table_item=reference_table.objects.get(bar_code=bar_code)
        stock_item=Stock.objects.get(id=reference_table_item.friendlyId)
        return stock_item
    except:
        print("Item not found")
        return None


def add_new_item(bar_code_value, name_value):
    #se busca en objeto en reference_table
    try:
        reference_table_item=reference_table.objects.get(bar_code=bar_code_value)
    except reference_table.DoesNotExist:
        reference_table_item=None
    #si existe se corta manda ese mensaje
    if reference_table_item is not None:    
        response="El código ya existe"
        #si no existe se crea
    else:

        try:
            #se busca si existe el nuevo objeto en Stock
            stock_item=Stock.objects.get(name=name_value)
        except Stock.DoesNotExist:
            stock_item=None

        if stock_item is not None:
            #Si existe el item en stock se crea una entrada en RT apuntando a ese item
            reference_table_new_item=reference_table.objects.create(bar_code=bar_code_value, friendlyId=stock_item.id)
            reference_table_new_item.save()
            response=f"Se añade un nuevo código de barras para {stock_item.name}"
        else:
            #Si no existe se crea
            stock_new_item=Stock.objects.create(name=name_value, quantity=1)
            stock_new_item.save()
            reference_table_item=reference_table.objects.create(bar_code=bar_code_value, friendlyId=stock_new_item.id)

            response="Nuevo objeto en stock"
    
    return response
    


