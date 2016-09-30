from django.shortcuts import render

# Create your views here.
def myidea(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
        
    item_list = Myidea.objects.order_by('f00')[:400]
    context = {'current_user':request.user,'page_title':'my idea','item_list': item_list}
    #使用ITEM005  template
    return render(request, 'myidea/index.html', context)  
  