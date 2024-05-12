import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import json

#შევქმენით კლასი, რომელშიც ვქმნით მთავარ ფანჯარას
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("design.ui", self) #შემოვიტანეთ დიზაინის ფაილი
        self.btnadd.clicked.connect(self.add_task)
        self.btnremove.clicked.connect(self.remove_task)
        self.load_tasks()

    def add_task(self): #ფუნქცია, რომელიც ამატებს ახალ დავალებას
        task = self.lineEdit.text()
        if task:
            self.listWidget.addItem(task)
            self.lineEdit.clear()
            self.save_tasks()


    def remove_task(self): #ფუნქცია, რომელიც წაშლის მონიშულ დავალებას
        selected_task = self.listWidget.selectedItems()
        if selected_task:
            for task in selected_task: #ციკლი, რომელიც წაშლის ყველა მონიშულ დავალებას
                self.listWidget.takeItem(self.listWidget.row(task))
            self.save_tasks()

    def load_tasks(self): #ფუნქცია, რომელიც ჩაგვიტვირთავს დავალებებს ფაილის ყოველი ახალი გახსნისას
            try:
                with open("tasks.json", "r") as file:
                    tasks = json.load(file)
                    for task in tasks:
                        self.listWidget.addItem(task)
            except FileNotFoundError:
                pass

    def save_tasks(self):
        tasks = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)



app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("To-Do List")
window.show()
sys.exit(app.exec_())
