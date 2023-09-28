from django.contrib import admin
from todo.models import Todo, TodoList


class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "due_date", "completed", "favourite", "create_at", "update_at"]
    list_filter = ["due_date", "completed", "favourite"]
    search_fields = ["title"]


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at", "update_at"]
    search_fields = ["name"]
    inlines = [TodoInline]
