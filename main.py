import sys
from PyQt5.QtWidgets import QApplication
from gui.GUI import Puzzle

def main():
    app = QApplication(sys.argv)
    puzzle = Puzzle()
    puzzle.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
   main()