import tkinter as tk

def add_task():
    task = task_entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox.insert(tk.END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection() # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox.delete(selected_task) # удаляем выбранный элемент из списка

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        current_color = task_listBox.itemcget(selected_task, "bg") # `itemcget()` — это метод позволяет получить текущее значение определенной опции конфигурации для конкретного элемента на холсте.
        # Проверяем текущий цвет и изменяем его
        if current_color == "dark gray":
            task_listBox.itemconfig(selected_task, bg="azure")  # меняем на стандартный цвет
        else:
            task_listBox.itemconfig(selected_task, bg="dark gray")  # меняем на цвет выполненной задачи

root = tk.Tk()
root.title("Task list")
root.configure(background="aquamarine")
text2 = tk.Label(root, text="Список задач:", bg="aquamarine")
text2.pack(pady=5)
text1 = tk.Label(root, text="Введите вашу задачу:", bg="aquamarine")
text1.pack(pady=5)
task_entry = tk.Entry(root, width=30, bg="azure")
task_entry.pack(pady=10)
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)
task_listBox = tk.Listbox(root, height=10, width=50, bg="azure")
task_listBox.pack(pady=10)
root.mainloop()

