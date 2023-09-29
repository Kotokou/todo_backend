from datetime import datetime
from django.test import TestCase
from todo.models import Todo, TodoList


class TodoTestCase(TestCase):

    def setUp(self):
        self.todoList = TodoList()
        self.todoList.name = "Courses"
        self.todoList.save()

        self.todoElemForTest = Todo()
        self.todoElemForTest.title = "Python"
        self.todoElemForTest.due_date = datetime.today()
        self.todoElemForTest.favourite = False
        self.todoElemForTest.completed = True
        self.todoElemForTest.list = self.todoList
        self.todoElemForTest.save()

    def test_create_todo(self):
        # Number of Todos we have in DB
        numbers_of_todos_before_add = Todo.objects.count()

        # Create new Todo
        new_todo = Todo()
        new_todo.title = "Buy Tomato"
        new_todo.due_date = datetime.today()
        new_todo.favourite = True
        new_todo.completed = False
        new_todo.list = self.todoList
        new_todo.save()

        # Number of Todos we have in DB
        numbers_of_todos_after_add = Todo.objects.count()

        # check
        self.assertTrue(numbers_of_todos_after_add == numbers_of_todos_before_add + 1)

    def test_update_todo(self):
        # First check
        self.assertEqual(self.todoElemForTest.title, "Python")

        # Change title value
        self.todoElemForTest.title = "Dart"
        self.todoElemForTest.save()

        # Create temporary element to store the update
        temp = Todo.objects.get(pk=self.todoElemForTest.pk)

        # Finally Check
        self.assertEqual(temp.title, "Dart")

    def test_delete_todo(self):
        # Number of Todos we have in DB
        numbers_of_todo_before_delete = Todo.objects.count()

        # Delete element
        self.todoElemForTest.delete()

        # Number of Todos we have in DB
        numbers_of_todo_after_delete = Todo.objects.count()

        # Check
        self.assertTrue(numbers_of_todo_after_delete == numbers_of_todo_before_delete - 1)





