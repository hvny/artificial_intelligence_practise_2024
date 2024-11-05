import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

class PhonebookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Телефонный справочник")
        self.setGeometry(100, 100, 400, 300)
        
        #основной layout
        main_layout = QVBoxLayout()

        #layout для ввода данных
        input_layout = QHBoxLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")
        input_layout.addWidget(self.name_input)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Введите телефон")
        self.phone_input.setInputMask("8(999)-999-99-99")
        input_layout.addWidget(self.phone_input)
        
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_contact)
        input_layout.addWidget(add_button)


        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Имя", "Телефон"])
        self.table.horizontalHeader().setStretchLastSection(True)
        
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()

        if phone.count('-') < 3 or len(phone) < 16:
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите полный номер телефона.")
            return
        
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

        name_item = QTableWidgetItem(name)
        phone_item = QTableWidgetItem(phone)

        self.table.setItem(row_count, 0, name_item)
        self.table.setItem(row_count, 1, phone_item)

        self.name_input.clear()
        self.phone_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhonebookApp()
    window.show()
    sys.exit(app.exec_())
