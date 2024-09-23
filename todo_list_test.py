# test_todo_list.py
import unittest
from todo_list import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_add_single_task(self):
        result = self.todo.add_task("Comprar pão")
        self.assertIn("Tarefa 'Comprar pão' adicionada", result)
        self.assertEqual(len(self.todo.todo_list), 1)

    def test_add_multiple_tasks(self):
        self.todo.add_task("Tarefa 1")
        self.todo.add_task("Tarefa 2")
        self.assertEqual(len(self.todo.todo_list), 2)

    def test_add_empty_task(self):
        result = self.todo.add_task("")
        self.assertEqual(result, "Tarefa inválida")
        self.assertEqual(len(self.todo.todo_list), 0)

    def test_remove_task_valid_index(self):
        self.todo.add_task("Tarefa 1")
        self.todo.add_task("Tarefa 2")
        result = self.todo.remove_task(1)
        self.assertIn("Tarefa 'Tarefa 1' removida", result)
        self.assertEqual(len(self.todo.todo_list), 1)

    def test_remove_task_invalid_index(self):
        self.todo.add_task("Tarefa 1")
        result = self.todo.remove_task(5)
        self.assertEqual(result, "Índice inválido. Tente novamente.")
        self.assertEqual(len(self.todo.todo_list), 1)

    def test_remove_task_negative_index(self):
        self.todo.add_task("Tarefa 1")
        result = self.todo.remove_task(-1)
        self.assertEqual(result, "Índice inválido. Tente novamente.")
        self.assertEqual(len(self.todo.todo_list), 1)

    def test_view_tasks_with_items(self):
        self.todo.add_task("Tarefa 1")
        self.todo.add_task("Tarefa 2")
        result = self.todo.view_tasks()
        self.assertEqual(result, ["1. Tarefa 1", "2. Tarefa 2"])

    def test_view_tasks_empty(self):
        result = self.todo.view_tasks()
        self.assertEqual(result, "Nenhuma tarefa na lista.")

    def test_add_task_with_special_characters(self):
        result = self.todo.add_task("@!#&")
        self.assertIn("Tarefa '@!#&' adicionada", result)
        self.assertEqual(len(self.todo.todo_list), 1)

    def test_remove_task_from_empty_list(self):
        result = self.todo.remove_task(1)
        self.assertEqual(result, "Índice inválido. Tente novamente.")
        self.assertEqual(len(self.todo.todo_list), 0)

if __name__ == '__main__':
    unittest.main()
