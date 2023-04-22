import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(250, 250)

        # Create the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create the grid layout for the buttons
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # Create the display line edit
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        grid_layout.addWidget(self.display, 0, 0, 1, 4)

        # Create the buttons
        button_labels = ['7', '8', '9', '/',
                         '4', '5', '6', '*',
                         '1', '2', '3', '-',
                         '0', '.', '=', '+']
        button_positions = [(i, j) for i in range(1, 5) for j in range(4)]

        self.buttons = {}
        for position, label in zip(button_positions, button_labels):
            button = QPushButton(label)
            button.clicked.connect(self.button_clicked)
            self.buttons[position] = button
            grid_layout.addWidget(button, *position)

        # Create the clear button
        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clear_clicked)
        grid_layout.addWidget(clear_button, 5, 0, 1, 2)

        # Create the backspace button
        backspace_button = QPushButton('Backspace')
        backspace_button.clicked.connect(self.backspace_clicked)
        grid_layout.addWidget(backspace_button, 5, 2, 1, 2)

    def button_clicked(self):
        button = self.sender()
        label = button.text()

        if label == '=':
            # Evaluate the expression and display the result
            expression = self.display.text()
            try:
                result = str(eval(expression, {}, {}))
            except:
                result = 'Error'
            self.display.setText(result)
        else:
            # Append the button label to the display
            self.display.setText(self.display.text() + label)

    def clear_clicked(self):
        self.display.clear()

    def backspace_clicked(self):
        self.display.backspace()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
