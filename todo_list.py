# todo_list.py
class TodoList:
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        if not task:
            return "Tarefa inválida"
        self.todo_list.append(task)
        return f"Tarefa '{task}' adicionada com sucesso!"

    def remove_task(self, index):
        try:
            removed_task = self.todo_list.pop(index - 1)
            return f"Tarefa '{removed_task}' removida com sucesso!"
        except IndexError:
            return "Índice inválido. Tente novamente."

    def view_tasks(self):
        if not self.todo_list:
            return "Nenhuma tarefa na lista."
        return [f"{i + 1}. {task}" for i, task in enumerate(self.todo_list)]
