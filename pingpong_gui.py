"""
-----------------------------------------------------
Author: Yousf Al Salti
Date: 31/03/2025
Time: 2:11 PM
Version: 1.0
-----------------------------------------------------

Filename: pingpong_gui

-----------------------------------------------------
Description: [Describe the purpose of the script]
-----------------------------------------------------

Inputs: [Describe inputs]
Outputs: [Describe outputs]
-----------------------------------------------------

Contact Information:
📧 Outlook: [yousefalsalti2411@outlook.com]
📧 Gmail: [yousefalsalti024@gmail.com]
🔗 GitHub: [https://github.com/yoyo24ii]
🔗 LinkedIn: [https://www.linkedin.com/in/yousfsalti24ii/]
-----------------------------------------------------

Copyright (c) 2025 Yousf Al Salti. All rights reserved.
-----------------------------------------------------
"""

import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import numpy as np

class MatplotlibWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My skipidi")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and set layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Add the canvas to the layout
        layout.addWidget(self.canvas)

        # Plot something
        self.plot_data()

    def plot_data(self):
        x = np.linspace(-10, 10, 101)
        y = x**2
        self.ax.plot(x, y, marker="o",markevery=10, linestyle="-", color="b", label="Line")
        self.ax.legend()
        self.canvas.draw()  # Update the figure

def main():
    app = QApplication(sys.argv)
    window = MatplotlibWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting...")

