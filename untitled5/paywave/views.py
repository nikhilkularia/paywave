from django.shortcuts import render
from .models import mobiles,dthcardform,creditcard,eletricity,gasprovider,datacardform,waterform,landlineform,broadbandform,metroform
from users.models import wallet_act
def mobile(request):
   return render(request,'paywave/mobile.html')

def actmobile(request):
    context={}
    if request.method=="POST":
      action='mobile_detail'
      context.update({'action1':action})
    service_type=request.POST["service"]
    phone_number=request.POST["phone_number"]
    operator = request.POST["operator"]
    circle = request.POST["circle"]
    amount = request.POST["amount"]
    mobile_info = mobiles(service_type=service_type, phone_number=phone_number, operator=operator, circle=circle,
                          amount=amount)
    mobile_info.save()

    wallet_act.objects.filter(pk=9).update(t_amount=amount)
    return render(request,'paywave/payment.html',context)


def dthcard(request):
    return render(request,'paywave/dthcard.html')

def actdth(request):
    context1 ={}
    if request.method == "POST":
        action = 'dth_detail'
        context1.update({'action1': action})
    dth_operator = request.POST["dthoperator"]
    dth_customer = request.POST["dthcustomer"]
    dth_amount = request.POST["dthamount"]
    dth_card = dthcardform(dth_operator=dth_operator, dth_customer=dth_customer, dth_amount=dth_amount)
    dth_card.save()

    wallet_act.objects.filter(pk=9).update(t_amount=dth_amount)
    return render(request,'paywave/payment.html',context1)

def electricity(request):
    return render(request,'paywave/electricity.html')


def actelectricity(request):
    context = {}
    if request.method == "POST":
        action = 'elec_detail'
        context.update({'action1': action})
    service_provider = request.POST["elecoperator"]
    elec_customer_id = request.POST["knumber"]
    elec_info = eletricity(service_provider=service_provider,elec_customer_id=elec_customer_id)
    elec_info.save()
    return render(request,'paywave/payment.html',context)

def movie(request):
    return render(request,'paywave/movie.html')

def gas(request):
    return render(request,'paywave/gas.html')

def actgas(request):
    context = {}
    if request.method == "POST":
        action = 'gas_detail'
        context.update({'action1': action})
    gas_provider = request.POST["gasprovider"]
    bp_number = request.POST["bpnumber"]
    gas_info = gasprovider(gas_provider=gas_provider,bp_number=bp_number)
    gas_info.save()
    return render(request,'paywave/payment.html',context)

def payment(request):
    return render(request,'paywave/payment.html')

def credit_payment(request):
    email = request.POST["email"]
    first_name = request.POST["first_name"]
    name_on_card = request.POST["name_on_card"]
    card_number = request.POST["card_number"]
    expire_month = request.POST["expire_month"]
    expire_year = request.POST["expire_year"]
    cvv_number = request.POST["cvv_number"]
    credit_info=creditcard(email=email,first_name=first_name,name_on_card=name_on_card,card_number=card_number,expire_month=expire_month,expire_year=expire_year,cvv_number=cvv_number)
    credit_info.save()
    return render(request,'paywave/final.html')

def final(request):
    return render(request,'paywave/final.html')

def datacard(request):
    return render(request,'paywave/datacard.html')

def actdatacard(request):
    context = {}
    if request.method == "POST":
        action = 'datacard_detail'
        context.update({'action1': action})
    service_type=request.POST["service"]
    phone_number=request.POST["phone_number"]
    operator = request.POST["operator"]
    circle = request.POST["circle"]
    amount = request.POST["amount"]
    datacard_info = datacardform(service_type=service_type, phone_number=phone_number, operator=operator, circle=circle, amount=amount)
    datacard_info.save()
    wallet_act.objects.filter(pk=9).update(t_amount=amount)
    return render(request,'paywave/payment.html',context)

def water(request):
    return render(request,'paywave/water.html')

def actwater(request):
    context = {}
    if request.method == "POST":
        action = 'water_detail'
        context.update({'action1': action})
    water_operator = request.POST["wateroperator"]
    wnumber = request.POST["wnumber"]
    water_info = waterform(water_operator=water_operator,wnumber=wnumber)
    water_info.save()
    return render(request,'paywave/payment.html',context)


def landline(request):
    return render(request,'paywave/landline.html')

def actlandline(request):
    context = {}
    if request.method == "POST":
        action = 'land_detail'
        context.update({'action1': action})
    landline_operator = request.POST["land_operator"]
    phone_number = request.POST["phone_number"]
    landline_info = landlineform(landline_operator=landline_operator,phone_number=phone_number)
    landline_info.save()
    return render(request,'paywave/payment.html',context)


def broadband(request):
    return render(request,'paywave/broadband.html')

def actbroadband(request):
    context = {}
    if request.method == "POST":
        action = 'broad_detail'
        context.update({'action1': action})
    broadband_operator = request.POST["broad_operator"]
    phone_number = request.POST["phone_number"]
    broad_info = broadbandform(broadband_operator=broadband_operator,phone_number=phone_number)
    broad_info.save()
    return render(request,'paywave/payment.html',context)

def metro(request):
    return render(request,'paywave/metro.html')

def actmetro(request):
    context = {}
    if request.method == "POST":
        action = 'metro_detail'
        context.update({'action1': action})
    metro_operator = request.POST["metro_operator"]
    metro_number = request.POST["metro_number"]
    metro_info = metroform(metro_operator=metro_operator,metro_number=metro_number)
    metro_info.save()
    return render(request,'paywave/payment.html',context)


def mobile_detail(request):
    obj=mobiles.objects.last()
    action="mobile"
    context = {
        'data':action,
        'mservice':obj.service_type,
        'mnumber':obj.phone_number,
        'moperator':obj.operator,
        'mcircle':obj.circle,
        'mamount':obj.amount
    }
    return render(request,'paywave/final.html',context)

def dth_detail(request):
    obj1=dthcardform.objects.last()
    action = "dth"
    context1 = {
    'data': action,
    'dthoperator':obj1.dth_operator,
    'dthcustomer':obj1.dth_customer,
    'dthamount':obj1.dth_amount
    }
    return render(request, 'paywave/final.html', context1)

def elec_detail(request):
    obj2=eletricity.objects.last()
    action = "elec"
    context2 = {
        'data': action,
        'elecoperator':obj2.service_provider,
        'eleccustomer':obj2.elec_customer_id
    }
    return render(request, 'paywave/final.html', context2)

def gas_detail(request):
    obj3=gasprovider.objects.last()

    action = "gas"
    context3 = {
        'data': action,
        'gasoperator':obj3.gas_provider,
        'bpnumber':obj3.bp_number
    }
    return render(request, 'paywave/final.html', context3)


def land_detail(request):
    obj4=landlineform.objects.last()
    action = "land"
    context4 = {
        'data': action,
        'landoperator':obj4.landline_operator,
        'landnumber':obj4.phone_number
    }
    return render(request, 'paywave/final.html', context4)

def water_detail(request):
    obj5=waterform.objects.last()
    action = "water"
    context5 = {
        'data': action,
        'wateroperator':obj5.water_operator,
        'wnumber':obj5.wnumber
    }
    return render(request, 'paywave/final.html', context5)

def datacard_detail(request):
    obj6=datacardform.objects.last()
    action = "data"
    context6 = {
        'data': action,
        'dataservice':obj6.service_type,
        'datanumber':obj6.phone_number,
        'dataoperator':obj6.operator,
        'datacircle':obj6.circle,
        'dataamount':obj6.amount
    }
    return render(request,'paywave/final.html',context6)

def broad_detail(request):
    obj7=broadbandform.objects.last()
    action = "broad"
    context7 = {
        'data': action,
        'broadoperator':obj7.broadband_operator,
        'broadnumber':obj7.phone_number

    }
    return render(request,'paywave/final.html',context7)

def metro_detail(request):
    obj8=metroform.objects.last()
    action = "metro"
    context8 = {
        'data': action,
        'metrooperator':obj8.metro_operator,
        'metronumber':obj8.metro_number
    }
    return render(request,'paywave/final.html',context8)






