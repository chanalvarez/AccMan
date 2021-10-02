from django.shortcuts import render , HttpResponse , redirect
from home.models import Account
from home.forms import AccountForm


def index(request):




   accounts = Account.objects.all()
   form = AccountForm()
   


   if request.method == "POST":
      form = AccountForm(request.POST)
      if form.is_valid():
         form.save()
      return redirect('/')
   context = {'accounts' : accounts , 'form' : form}
   return render(request, 'list.html' , context)

def updateTask(request, pk):
   acc = Account.objects.get(id=pk)

   form = AccountForm(instance=acc)

   if request.method == 'POST':
      form = AccountForm(request.POST, instance=acc)
      if form.is_valid():
         form.save()
         return redirect('/')

   context = {'form' : form}

   return render(request, 'update.html',context)
def deleteTask(request, pk):
   item = Account.objects.get(id=pk)

   if request.method == 'POST':
      item.delete()
      return redirect('/')

   context = {'item' : item}
   return render(request, 'delete.html' , context)
def search(request):
   search_query = request.GET.get('search', '')
   if search_query:
      accounts = Account.objects.filter(title__icontains=search_query)
   else: 
      accounts = Account.objects.all()   
   
   context = {'accounts' : accounts}
  
  

   return render(request, 'search.html' , context)
def test(request):
   accounts = Account.objects.all()
   context = {'accounts' : accounts}

   return render(request , 'list.html' , context)
    
  