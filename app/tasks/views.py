from django.shortcuts import render, redirect
from django.contrib import messages
  
## import tasks form and models
  
from .forms import TasksForm
from .models import Tasks
  
###############################################
  
def index(request):
  
    item_list = Tasks.objects.order_by("-date")
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    form = TasksForm()
  
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "TASK LIST",
           }
    return render(request, 'tasks/index.html', page)
  
  
  
### function to remove item, it receive todo item id from url ##
def remove(request, item_id):
    item = Tasks.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('tasks')