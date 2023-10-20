import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit

class EquipmentCatalogApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Справочник оборудования")

        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Наименование", "Модель", "Количество"])

        add_button = QPushButton("Добавить оборудование")

        layout.addWidget(self.table_widget)
        layout.addWidget(add_button)

        central_widget.setLayout(layout)

        add_button.clicked.connect(self.show_add_dialog)

    def show_add_dialog(self):
        add_dialog = AddEquipmentDialog()
        result = add_dialog.exec_()

        if result == AddEquipmentDialog.Accepted:
            name = add_dialog.name_line_edit.text()
            model = add_dialog.model_line_edit.text()
            quantity = add_dialog.quantity_line_edit.text()

            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(model))
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(quantity)


class AddEquipmentDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить оборудование")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText("Наименование")

        self.model_line_edit = QLineEdit()
        self.model_line_edit.setPlaceholderText("Модель")

        self.quantity_line_edit = QLineEdit()
        self.quantity_line_edit.setPlaceholderText("Количество")

        add_button = QPushButton("Добавить")
        cancel_button = QPushButton("Отмена")

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(cancel_button)

        layout.addWidget(self.name_line_edit)
        layout.addWidget(self.model_line_edit)
        layout.addWidget(self.quantity_line_edit)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        add_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)


def main():
    app = QApplication(sys.argv)
    window = EquipmentCatalogApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
