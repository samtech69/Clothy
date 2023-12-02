from django import template

register=template.Library()

@register.filter(name="paymentMode")
def paymentMode(Request, num):
    if(num==0):
        return "COD"
    else:
        return "NetBanking"

@register.filter(name="paymentStatus")
def paymentMode(Request, num):
    if(num==0):
        return "Pending"
    else:
        return "Done"
    
@register.filter(name="orderStatus")
def paymentMode(Request, num):
    if(num==0):
        return "Order is Placed"
    elif(num==1):
        return "Order is Packed"
    elif(num==2):
        return "Ready to dispatch"
    elif(num==3):
        return "Dispached"
    elif(num==4):
        return "Out for delivery"
    elif(num==5):
        return "Delivered"
    else:
        return "Done"
    
@register.filter(name="paymentCondition")
def paymentCondtion(mode, status):
    if(mode==1 and status==0):
        return False
    else:
        return True 


