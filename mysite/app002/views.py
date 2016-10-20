from django.shortcuts import render

# Create your views here.
from .models import Mnemonics

def me(request):
#     # if not request.user.is_authenticated:
#     #      return redirect('/')
#     item_list = TaichiMove.objects.filter(stylenum=19).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'Me','item_list': []}
    return render(request, 'app001/me.html', context)

def index(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=19).order_by('num2', 'num2')[:3000]
    context = {'current_user':request.user,'page_title':'xxxapp002 index','item_list': item_list}
    return render(request, 'app001/index.html', context)
    
    
def index19(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=19).order_by('num2', 'num2')[:3000]
    context = {'current_user':request.user,'page_title':'19only 十九式','item_list': item_list}
    return render(request, 'app001/index19.html', context)    
    
def index13(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=13).order_by('num2', 'num2')[:3000]
    context = {'current_user':request.user,'page_title':'十三式','item_list': item_list}
    return render(request, 'app001/index13.html', context)   
    
def index08(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=8).order_by('num2', 'num2')[:3000]
    context = {'current_user':request.user,'page_title':'八式','item_list': item_list}
    return render(request, 'app001/index13.html', context)   
    
def form(request,num):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=num).order_by('num2', 'num3')[:3000]
    context = {'current_user':request.user,'page_title':num,'item_list': item_list}
    return render(request, 'app001/form.html', context)  
    
def num1(request,num1):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=num1).order_by('num2', 'num3')[:3000]
    context = {'current_user':request.user,'page_title':num1,'item_list': item_list}
    return render(request, 'app001/num1.html', context) 
def num2(request,num1,num2):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Mnemonics.objects.filter(num1=num1,num2=num2).order_by('num2', 'num3')[:3000]
    context = {'current_user':request.user,'page_title':num1,'item_list': item_list}
    return render(request, 'app001/num2.html', context)     
 
def num3(request,num1,num2,num3):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # item_list = Mnemonics.objects.filter(num1=num1,num2=num2,num3=num3).order_by('num2', 'num3')[:3000]
    item_list = Mnemonics.objects.filter(num1=num1,num2=num2).order_by('num2', 'num3')[:3000]
    context = {'current_user':request.user,'page_title':num3,'item_list': item_list,'num1':num1,'num2':num2,'num3':num3}
    return render(request, 'app001/num3.html', context)     
 