from django.shortcuts import render,redirect
from .forms import userregiterform,userupdateform,profileupdateform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import wallet_act
# Create your views here.
def register(request):
    if request.method == 'POST':
      form = userregiterform(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request,f'Account created successfully for {username}!')
          return redirect('login')
    else:
       form = userregiterform()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
       u_form = userupdateform(request.POST,instance=request.user)
       p_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
       messages.success(request, f'Account profile updated!')
       return redirect('profile')

    else:
       u_form = userupdateform(instance=request.user)
       p_form = profileupdateform(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)

def wpayment(request):
    obj = wallet_act.objects.last()
    value1 = int(obj.wallet_amount)
    value2 = int(obj.t_amount)
    context = {
        'wamount': value1,
        'tamount': value2
    }
    return render(request, 'users/wpayment.html', context)

def wallet(request):
    obj = wallet_act.objects.last()
    context = {
        'amount': obj.wallet_amount
    }
    return render(request,'users/wallet.html',context)


def wallet_update(request):
    obj = wallet_act.objects.last()
    value1 = int(obj.wallet_amount)
    value2 = int(request.POST['addamount'])
    value3 = (value1+value2)
    context = {
        'amount1':value3
    }
    wallet_act.objects.filter(pk=9).update(wallet_amount=value3)
    return render(request,'users/wallet.html',context)

def wallet_payment(request):
    obj =wallet_act.objects.last()
    value1=int(obj.wallet_amount)
    value2=int(obj.t_amount)
    if (value1 >= value2):
       value3=value1-value2
       wallet_act.objects.filter(pk=9).update(wallet_amount=value3)
       print(value3)
       return render(request,'paywave/final.html')
    else:
       return render(request,'users/error.html')

def error(request):
    return render(request,'users/error.html')
