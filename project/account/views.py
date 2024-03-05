from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.

class TodoListView(View):
    def get(self,request):
        data=Todomodel.objects.all()
        return render(request,'list.html',{"data":data})
    
class TodoaddView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,'add.html',{"form":form})
    
    def post(self,request):
        form_data=TodoForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"ToDo Addedd succesfuly!!")
            messages.error(request,"ERORR!!")
            return redirect('tlist')
        else:
            messages.error(request,"ToDo Addedd is Failded ")
            return render(request,'add.html',{"form":form_data})

class TodoDeleteView(View):
    def get(self,request,**kwargs):
        sid=kwargs.get('id')
        data=Todomodel.objects.get(id=sid)
        data.delete()
        messages.warning(request,"DELETED !!")
        return redirect('tlist')
    
class TodoEditView(View):
    def get(self,request,**kwargs):
        sid=kwargs.get('id')
        todo=Todomodel.objects.get(id=sid)
        form=TodoForm(instance=todo)
        return render(request,'edit.html',{"form":form})
    def post(self,request,**kwargs):
        sid=kwargs.get('id')
        todo=Todomodel.objects.get(id=sid)
        form_data=TodoForm(data=request.POST,files=request.FILES,instance=todo)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Tddo is Updated")
            return redirect('tlist')
        else:
            return render(request,'edit.html',{"form":form_data})