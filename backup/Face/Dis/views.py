from django.shortcuts import render
from Dis.models import Face

# Create your views here.
def index(request):
    return render(request,'index.html')

def go(request):
    que = request.POST.get('stud')
    z=''
    nn = Face.objects.all().values(que)
    for i in nn:
        z+=str(i[que])
    
    return render(request,'result.html',{'que':z})
    #return render(request,'linear.html',{'que':z})
