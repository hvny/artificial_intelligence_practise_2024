import sys
import collections
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import psutil

class CPUUsageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #окно и интерфейс
        self.setWindowTitle("CPU Usage")
        self.setGeometry(100, 100, 400, 400)

        #график
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        #очередь для хранения данных о загрузке процессора
        self.data_len = 100
        self.data = collections.deque(maxlen=self.data_len)
        for _ in range(self.data_len):
            self.data.append(0)  # Заполнение очереди начальными значениями

        #таймер для обновления графика
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(300)  # Таймер срабатывает каждую секунду

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_plot(self):
        cpu_load = psutil.cpu_percent(interval=1)
        self.data.append(cpu_load)
        
        #очистка предыдущего графика и создание нового
        self.ax.clear()
        self.ax.plot(list(self.data), label="CPU Usage")
        self.ax.set_ylim(0, 100)
        self.ax.set_xlabel("Time (seconds)")
        self.ax.set_ylabel("CPU Load (%)")
        self.ax.set_title("CPU Usage")
        self.ax.legend(loc="upper right")

        #перерисовка графика на экране
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CPUUsageApp()
    window.show()
    sys.exit(app.exec_())