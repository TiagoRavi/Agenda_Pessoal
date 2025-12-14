from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Todo
from .forms import TodoForm


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("todo_list")

        return render(
            request,
            "auth/login.html",
            {"error": "Usuário ou senha inválidos"}
        )

    return render(request, "auth/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def todo_list(request):
    todo_list = Todo.objects.all()
    return render(
        request,
        "todos/todo_list.html",
        {"todo_list": todo_list}
    )


@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(
        request,
        "todos/todo_form.html",
        {"form": form, "title": "Nova Tarefa"}
    )


@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)

    return render(
        request,
        "todos/todo_form.html",
        {"form": form, "title": "Editar Tarefa"}
    )


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("todo_list")

    return render(
        request,
        "todos/todo_confirm_delete.html",
        {"todo": todo}
    )


@login_required
def todo_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if not todo.finished_at:
        todo.finished_at = timezone.now()
        todo.save()

    return redirect("todo_list")
