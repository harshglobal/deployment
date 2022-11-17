from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')
    
def other(request):
    mydict = {'name': 'Harshwardhan', 'Mob':9970544367}
    return render(request,'basicapp/other.html',mydict)

def relative(request):
    return render(request,'basicapp/relative_url.html')
