from django.shortcuts import render, redirect  
from customer.forms import CustomerForm 
from customer.models import Customer  
# Create your views here.  
def customer(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CustomerForm() 
    return render(request,'index.html',{'form':form})  
def show(request):  
    cust = Customer.objects.all()  
    return render(request,"show.html",{'customer':cust})  
def edit(request, id):  
    cust = Customer.objects.get(id=id)  
    print("Customer :",cust.custid)
    return render(request,'edit.html', {'customer':cust})  
def update(request, id):  
    cust = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = cust)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'cust': cust})  
def destroy(request, id):  
    cust = Customer.objects.get(id=id)  
    cust.delete()  
    return redirect("/show")  