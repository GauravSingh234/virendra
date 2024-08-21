from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
    result=0
    data=dict({})

   
    if request.method=="POST":
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        result=n1+n2
        data={
            "a1":n1,
            "a2":n2,
            "output":result}

    # print(sum)
    return render(request,"index.html",data)
