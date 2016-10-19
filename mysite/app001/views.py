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
    context = {'current_user':request.user,'page_title':'十九式','item_list': item_list}
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
    
    