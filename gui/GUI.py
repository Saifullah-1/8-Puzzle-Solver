import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QHBoxLayout,QGridLayout, QPushButton, QComboBox, QLineEdit, QMessageBox, QPlainTextEdit, QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from algorithms.SearchFactory import SearchFactory

class Puzzle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.algorithm_index = 0
        self.initial_state = 12345678
        self.setWindowTitle("8-Puzzle Solver")
        self.setGeometry(650, 200, 700, 700)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(20, 20, 20, 20)
        self.vbox.setSpacing(10)

        self.label = QLabel("Search Algorithms")
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet("""
            font-size: 20px;
        """)
        self.label.setFixedHeight(30)

        self.algorithms_list = QComboBox()
        self.algorithms_list.addItem("Choose Algorithm")
        self.algorithms_list.addItems(['BFS','DFS','Iterative DFS', 'A*'])
        self.algorithms_list.setStyleSheet("""
            font-size: 15px;                                
        """)
        self.algorithms_list.setFixedHeight(30)
        self.algorithms_list.activated.connect(self.set_algorithm)

        self.solve_button = QPushButton("solve",self)
        self.solve_button.setFixedHeight(50)
        self.solve_button.setFixedWidth(100)
        self.solve_button.clicked.connect(self.solve)
       
      
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.algorithms_list)
        self.vbox.addWidget(self.solve_button)
        
        #for displaying output 
        self.vbox2 = QVBoxLayout() 
        self.vbox2.setSpacing(5)
        
        self.hbox = QHBoxLayout()

        self.label1 = QLabel("Expanded nodes")
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFixedHeight(30)

        self.label2 = QLabel("Running time")
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFixedHeight(30) 

        self.label3 = QLabel("cost")
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label3.setFixedHeight(30) 

        self.label4 = QLabel("Search depth")
        self.label4.setAlignment(Qt.AlignHCenter)
        self.label4.setFixedHeight(30) 

        self.hbox.addWidget(self.label1)
        self.hbox.addWidget(self.label2)
        self.hbox.addWidget(self.label3)
        self.hbox.addWidget(self.label4)

        self.hbox2 = QHBoxLayout()
        self.expanded_nodes= QLineEdit()
        self.expanded_nodes.setReadOnly(True)

        self.running_time= QLineEdit()
        self.running_time.setReadOnly(True)

        self.cost= QLineEdit()
        self.cost.setReadOnly(True)

        self.search_depth= QLineEdit()
        self.search_depth.setReadOnly(True)

        self.hbox2.addWidget(self.expanded_nodes)
        self.hbox2.addWidget(self.running_time)
        self.hbox2.addWidget(self.cost)
        self.hbox2.addWidget(self.search_depth)

        self.label5 = QLabel("Steps")
        self.label5.setAlignment(Qt.AlignHCenter)
        self.label5.setFixedWidth(200) 

        self.path = QPlainTextEdit()
        self.path.setReadOnly(True)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.path)
        self.scroll_area.setFixedWidth(200)
        self.scroll_area.setMinimumHeight(100)

        self.vbox2.addLayout(self.hbox)
        self.vbox2.addLayout(self.hbox2)
        self.vbox2.addWidget(self.label5)
        self.vbox2.addWidget(self.scroll_area)

       
        self.grid = QGridLayout()
        self.grid.setContentsMargins(300, 50, 300, 50)

        self.cell1 = QLineEdit(self) 
        self.cell2 = QLineEdit(self) 
        self.cell3 = QLineEdit(self) 
        self.cell4 = QLineEdit(self) 
        self.cell5 = QLineEdit(self) 
        self.cell6 = QLineEdit(self) 
        self.cell7 = QLineEdit(self) 
        self.cell8 = QLineEdit(self)
        self.cell9 = QLineEdit(self)

        self.cells = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8, self.cell9]
        cnt = 0
        for cell in self.cells:
            cell.setAlignment(Qt.AlignCenter)
            cell.setFixedSize(70, 70)
            cell.setText(str(cnt))
            cell.setStyleSheet("font-size: 20px; font-weight: bold;")
            cnt += 1


        self.grid.addWidget(self.cell1, 0, 0)
        self.grid.addWidget(self.cell2, 0, 1)
        self.grid.addWidget(self.cell3, 0, 2)
        self.grid.addWidget(self.cell4, 1, 0)
        self.grid.addWidget(self.cell5, 1, 1)
        self.grid.addWidget(self.cell6, 1, 2)
        self.grid.addWidget(self.cell7, 2, 0)
        self.grid.addWidget(self.cell8, 2, 1)
        self.grid.addWidget(self.cell9, 2, 2)
       
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setSpacing(10)
        main_layout.addLayout(self.grid)  
        main_layout.addLayout(self.vbox) 
        main_layout.addLayout(self.vbox2) 
        self.central_widget.setLayout(main_layout)

        #hiding output widgets
        self.label1.hide()
        self.label2.hide()
        self.label3.hide()
        self.label4.hide()
        self.label5.hide()
        self.expanded_nodes.hide()
        self.running_time.hide()
        self.cost.hide()
        self.search_depth.hide()
        self.scroll_area.hide()

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.solve_steps)
        # self.current_step = 0
        # # self.steps = ["125340678","120345678", "102345678", "012345678"] #for testing

    def solve(self):
            solution = {}
            self.set_initial_state() 
            
            factory = SearchFactory()

            if self.algorithm_index == 1:
                solution = factory.create_search_algorithm("BFS",self.initial_state)
            elif self.algorithm_index == 2:
                solution = factory.create_search_algorithm("DFS",self.initial_state)
            elif self.algorithm_index == 3:
                solution = factory.create_search_algorithm("IDS",self.initial_state)
            elif self.algorithm_index == 4:
                solution = factory.create_search_algorithm("A*",self.initial_state)
            else:
                QMessageBox.warning(self, "Warning", "Please Choose a Search Algorithm")
                return
            
            if solution == False :
                QMessageBox.warning(self, "Unfortunately", "This Puzzle is Unsolvable")
            else :
                self.show_output(solution)
                
       
    
    # def solve_steps(self):
    #     if self.current_step < len(self.steps):
    #         step = self.steps[self.current_step]
    #         idx = 0
    #         for cell in self.cells:
    #             if step[idx] != '0':
    #                 cell.setStyleSheet("font-size: 20px; font-weight: bold")
    #             else :
    #                 cell.setStyleSheet("font-size: 20px; font-weight: bold; background-color: #bac0cf")
    #             cell.setText(step[idx])
    #             idx +=1
    #         self.current_step += 1
    #     else:
    #         self.timer.stop()
    
    def set_algorithm(self):
        self.algorithm_index = self.algorithms_list.currentIndex()

    def set_initial_state(self):
        self.initial_state = 0 
        for cell in self.cells:
            self.initial_state = self.initial_state * 10 + int(cell.text())
        print(self.initial_state)
           

    def show_output(self, solution):
        print(str(solution["expanded_nodes"]))
        self.expanded_nodes.setText(str(solution["expanded_nodes"]))
        self.running_time.setText(str(solution["running_time"]))
        self.cost.setText(str(solution["cost"]))
        self.search_depth.setText(str(solution["search_depth"]))
        self.path.setPlainText(str(solution["path"])) #to be handeled

        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.label4.show()
        self.label5.show()
        self.expanded_nodes.show()
        self.running_time.show()
        self.cost.show()
        self.search_depth.show()
        self.scroll_area.show()


# to be placed in main
app = QApplication(sys.argv)
puzzle = Puzzle()
puzzle.show()
sys.exit(app.exec_())