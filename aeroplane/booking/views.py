from django.shortcuts import render
from booking.models import Detail

# Create your views here.
def fun1(request):
    details=Detail.objects.all()
    context={"res":details}
    return render(request,"home.html",context)



def fun2(request):
    detail=Detail.objects.all()
    if request.method=="POST":
        Name=request.POST.get("name")
        Source=request.POST.get("fname")
        Destiny=request.POST.get("dname")
        Date=request.POST.get("datee")
        Cost=int(request.POST.get("Price"))
        obj=Detail(name=Name,source=Source,destiny=Destiny,date=Date,Price=Cost)
        obj.save()
        detail=Detail.objects.all()
        return render(request,"det.html",{"d":detail,"obj":obj})
    return render(request,"det.html")
