from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import CreateTodo

# Create your views here.
def event(request):
    context = {}
    system = request.POST.get('buttonAdd', None)
    context['buttonAdd': system]

def index(request):
    if request.method == 'POST':
        form = CreateTodo(request.POST)

        if form.is_valid():
            typeT = request.POST.get('addButton', 'day')
            print(typeT)
            textT = request.POST['text'] + str(typeT)
            new_item = Todo(text=textT, type=typeT)
            new_item.save()
            return redirect('index')

    else:
        form = CreateTodo() #creates the form


    items = Todo.objects.order_by('id')    
    context = {'form': form, 'items': items } #can now be passed to the HTML file
    return render(request, 'todo_list/index.html', context)




def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')    


def deleteAll(request):
    all = Todo.objects.all()
    all.delete()

    return redirect('index')  






    