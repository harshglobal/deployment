from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def details(request):
    return render(request,'details.html')
def userform(request):
    final_op = 0
    try:
        if request.method=="GET":
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            final_op=num1+num2
            data={
                'num1':num1,
                'num2':num2,
                'output':final_op
        }
    except:
        pass
    print(final_op)
    return render(request,'userform.html',data)