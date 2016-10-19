from django.shortcuts import render

# Create your views here.
from .models import Mnemonics

def me(request):
#     # if not request.user.is_authenticated:
#     #      return redirect('/')
#     item_list = TaichiMove.objects.filter(stylenum=19).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'Me','item_list': []}
    return render(request, 'app001/me.html', context)

# def style19(request):
#     # if not request.user.is_authenticated:
#     #      return redirect('/')
#     item_list = TaichiMove.objects.filter(stylenum=19).order_by('setnum', 'movenum')[:3000]
#     context = {'current_user':request.user,'page_title':'十九式','item_list': item_list}
#     return render(request, 'itaiching/style19.html', context)