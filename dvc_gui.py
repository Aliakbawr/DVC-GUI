import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("DVC Status Checker")
        layout = QVBoxLayout(self)

        self.button = QPushButton("Check DVC Status")
        self.button.clicked.connect(self.check_status)
        layout.addWidget(self.button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

    def check_status(self) -> None:
        try:
            completed = subprocess.run(
                ["dvc", "status"],
                text=True,
                capture_output=True,
                check=False,
            )
            text = completed.stdout + completed.stderr
        except Exception as exc:  # pragma: no cover - error path
            text = str(exc)
        self.output.setPlainText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
