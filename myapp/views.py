from re import template
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,UpdateView,DetailView,DeleteView,CreateView
from myapp.forms import LoginForm, TodoForm,TodoModelForm,RegistraionForm,LoginForm
from myapp.models import Todos, todos
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

def signing_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
@method_decorator(signing_required,name="dispatch")
# Create your views here.kj
class TodoCreateView(CreateView):


    model=Todos
    form_class=TodoModelForm
    template_name="add_todo.html"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    # def get(self,request,*args, **kwargs):
    #     form=TodoModelForm()
    #     return render(request,"add_todo.html",{"form":form})

    # def post(self,request,*args, **kwargs):
    #     form=TodoModelForm(request.POST)
    #     form.instance.user=request.user
    #     if form.is_valid():
    #         form.save()
            # messages.success(request,"Todo has been created Sucessfully")
            # t_name=form.cleaned_data.get("task_name")
            # usr=form.cleaned_data.get("user")
            # Todos.objects.create(task_name=t_name,user=usr)
           
            # print(form.cleaned_data)
            # lastid=todos[-1].get("id")
            # id=lastid+1
            # form.cleaned_data["id"]=id

            # todos.append(form.cleaned_data)
            # print(todos)

        #     return redirect("todo-list")
        # else:
        #     messages.error(request,"Todo creation Failed")

        #     return render(request,"add_todo.html",{"form":form})


@method_decorator(signing_required,name="dispatch")
class TodoListView(ListView):
    model=Todos
    context_object_name="todos"
    template_name="todolist.html"

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
    
    # def get(self,request,*args, **kwargs):
    #     qs=Todos.objects.filter(user=request.user)
    #     return render(request,"todolist.html",{"todos":qs})


@method_decorator(signing_required,name="dispatch")
class TodoDetailView(DetailView):
    model=Todos
    context_object_name="todo"
    template_name="tododetail.html"
    pk_url_kwarg="id"
    # def get(self,request,*args, **kwargs):
    #     id=kwargs.get("id")

    #     qd=Todos.objects.filter(id=id)
    #     # todo=[ todo for todo in todos if todo.get("id")==id].pop()

    #     return render(request,"tododetail.html",{"todo":qd})

@method_decorator(signing_required,name="dispatch")
class TodoDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        Todos.objects.filter(id=id).delete()
        # todo=[todo for todo in todos if todo.get("id")==id].pop()
        # todos.remove(todo)
        messages.success(request,"Todo Sucessfully Deleted")
        return redirect("todo-list")


@method_decorator(signing_required,name="dispatch")
class TodoEditView(UpdateView):
    model=Todos
    form_class=TodoModelForm
    template_name="todo-update.html"
    pk_url_kwarg: str="id"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        messages.success(self.request,"Todo has been Updated")
        return super().form_valid(form)

       # def get(self,request,*args, **kwargs):
    #     id=kwargs.get("id")
    #     # todo=[todo for todo in todos if todo.get("id")==id].pop()
    #     # qs=Todos.objects.filter(id=id).values()[0]
    #     qs=Todos.objects.get(id=id)
    #     form=TodoModelForm(instance=qs)
    #     return render(request,"todo-update.html",{"form":form})
    # def post(self,request,*args, **kwargs):
    #     id=kwargs.get("id")
    #     qs=Todos.objects.get(id=id)
    #     form=TodoModelForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Todo Updated Sucessfully")
    #         # Todos.objects.filter(id=id).update(**form.cleaned_data)
    #         # data=form.cleaned_data
            
    #         # todo=[todo for todo in todos if todo.get("id")==id].pop()
    #         # todo.update(data)
    #         return redirect("todo-list")
    #     else:
    #           messages.error(request,"Todo updation Failed")
    #           return render(request,"todo-update.html",{"form":form})

class RegistrationView(View):
    def get(self,request,*args, **kwargs):
        form=RegistraionForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args, **kwargs):
        form=RegistraionForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Registered Sucessfully")
            return redirect("login")
        else:
              messages.error(request,"Registration Failed")
              return render(request,"registration.html",{"form":form})


class LoginView(View):

    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(sel,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("todo-list")
            else:
                messages.error(request,"invalid input")
                return render(request,"login.html",{"form":form})
@signing_required
def signout(request,*args, **kwargs):
    logout(request)
    return redirect("login")

                
                

    
    

