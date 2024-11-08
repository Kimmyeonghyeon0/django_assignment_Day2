from django.db.models.expressions import result
from django.shortcuts import render
from django.http import Http404
from todo.models import Todo
from django.shortcuts import render
from django.core.paginator import Paginator
# from user_app.models import User

def todo_list(request):
    todo_list = Todo.objects.all().values_list('id', 'title')
    result = [{'id': todo[0], 'title': todo[1]} for i, todo in enumerate(todo_list)]

    return render(request, 'todo_list.html', {'date': result})

def todo_info(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        info = {
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.start_date,
            'end_date': todo.end_date,
            'is_completed': todo.is_completed,
        }
        return render(request, 'todo_info.html', {'data': info})
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")




def users_list(request):
    user_list = user.objects.all().values_list('id', 'username')
    result = [{'user_id': user_id, 'user_name': user_name} for user_id, user_name in user_list]

    # Pagination setup: 10 users per page
    paginator = Paginator(result, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_list.html', {'page_obj': page_obj})

def user_info(request, user_id):
    try:
        user = user.objects.get(id=user_id)
        info = {
            'user_id': user.user_id,
            'user_name': user.user_name,
            'start_date': user.start_date,
        }
        return render(request, 'user_info.html', {'data': info})
    except User.DoesNotExist:
        raise Http404("User does not exist")