import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QFileDialog,
)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("DVC Status Checker")
        layout = QVBoxLayout(self)

        self.directory = "."

        self.dir_button = QPushButton("Select Directory")
        self.dir_button.clicked.connect(self.select_directory)
        layout.addWidget(self.dir_button)

        self.button = QPushButton("Check DVC Status")
        self.button.clicked.connect(self.check_status)
        layout.addWidget(self.button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

    def select_directory(self) -> None:
        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", self.directory
        )
        if directory:
            self.directory = directory
            self.dir_button.setText(f"Directory: {directory}")

    def check_status(self) -> None:
        try:
            completed = subprocess.run(
                ["dvc", "status"],
                text=True,
                capture_output=True,
                check=False,
                cwd=self.directory,
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
