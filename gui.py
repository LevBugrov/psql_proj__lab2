from PyQt5 import Qt as Q


class LineEdit(Q.QWidget):
    def __init__(self, text):
        super().__init__()
        self.label = Q.QLabel(text)
        self.label.setMinimumSize(100, 0)
        self.label.setAlignment(Q.Qt.AlignRight | Q.Qt.AlignVCenter)
        self.edit = Q.QLineEdit()
        layout = Q.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        self.setLayout(layout)


class Table1(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create table Services
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Branch id", "Type id", "Customer id", "Date"))
        # Create buttons
        self.branch = LineEdit("Branch id")
        self.type = LineEdit("Type id")
        self.customer = LineEdit("Customer id")
        self.date = LineEdit("Date")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from Services")
        self.search_record = Q.QPushButton("Search by Date")
        self.remove_record = Q.QPushButton("Remove by Date")
        self.update_record = Q.QPushButton("Update record")
        self.delete_record = Q.QPushButton("Delete record")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.branch)
        buttons_layout.addWidget(self.type)
        buttons_layout.addWidget(self.customer)
        buttons_layout.addWidget(self.date)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addWidget(self.update_record)
        buttons_layout.addWidget(self.delete_record)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)


class Table2(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create Branches table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Address", "Phone Number"))
        # Create buttons
        self.id = LineEdit("Id")
        self.name = LineEdit("Name")
        self.address = LineEdit("Address")
        self.phone_number = LineEdit("Phone Number")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from Branches")
        self.search_record = Q.QPushButton("Search by Name")
        self.remove_record = Q.QPushButton("Remove by Name")
        self.update_record = Q.QPushButton("Update record")
        self.delete_record = Q.QPushButton("Delete record")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.id)
        buttons_layout.addWidget(self.name)
        buttons_layout.addWidget(self.address)
        buttons_layout.addWidget(self.phone_number)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addWidget(self.update_record)
        buttons_layout.addWidget(self.delete_record)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)


class Table3(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create Customers table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(("Id", "Last Name", "First Name", "Phone Number", "Total Sum"))
        self.table.setMinimumSize(650, 0)
        # Create buttons
        self.id = LineEdit("Id")
        self.last_name = LineEdit("Last Name")
        self.first_name = LineEdit("First Name")
        self.phone_number = LineEdit("Phone Number")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from Customers")
        self.search_record = Q.QPushButton("Search by First Name")
        self.remove_record = Q.QPushButton("Remove by First Name")
        self.update_record = Q.QPushButton("Update record")
        self.delete_record = Q.QPushButton("Delete record")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.id)
        buttons_layout.addWidget(self.last_name)
        buttons_layout.addWidget(self.first_name)
        buttons_layout.addWidget(self.phone_number)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addWidget(self.update_record)
        buttons_layout.addWidget(self.delete_record)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)


class Table4(Q.QWidget):
    def __init__(self):
        super().__init__()
        # Create Types of service table
        self.table = Q.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Type", "Cost"))
        # Create buttons
        self.id = LineEdit("Id")
        self.name = LineEdit("Name")
        self.type = LineEdit("Type")
        self.cost = LineEdit("Cost")
        self.add_record_button = Q.QPushButton("Add record")
        self.remove_all_button = Q.QPushButton("Remove all records from Types of service")
        self.search_record = Q.QPushButton("Search by Type")
        self.remove_record = Q.QPushButton("Remove by Type")
        self.update_record = Q.QPushButton("Update record")
        self.delete_record = Q.QPushButton("Delete record")
        self.buttons_widget = Q.QWidget()
        buttons_layout = Q.QVBoxLayout()
        buttons_layout.addWidget(self.id)
        buttons_layout.addWidget(self.name)
        buttons_layout.addWidget(self.type)
        buttons_layout.addWidget(self.cost)
        buttons_layout.addWidget(self.add_record_button)
        buttons_layout.addWidget(self.search_record)
        buttons_layout.addWidget(self.remove_record)
        buttons_layout.addWidget(self.remove_all_button)
        buttons_layout.addWidget(self.update_record)
        buttons_layout.addWidget(self.delete_record)
        buttons_layout.addItem(Q.QSpacerItem(0, 0, Q.QSizePolicy.Expanding,
                                             Q.QSizePolicy.Expanding))
        self.buttons_widget.setLayout(buttons_layout)
        # Set tab layout
        widget_layout = Q.QHBoxLayout()
        widget_layout.addWidget(self.table)
        widget_layout.addWidget(self.buttons_widget)
        self.setLayout(widget_layout)

class Ui(Q.QMainWindow):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.resize(1200, 800)
        MainWindow.setWindowTitle("Company")
        MainWindow.setWindowIcon(Q.QIcon("database-icon.jpeg"))
        self.central_widget = Q.QWidget()
        MainWindow.setCentralWidget(self.central_widget)
        # Open data base
        self.open_db_label = Q.QLabel("Open database")
        self.open_db_edit = Q.QLineEdit()
        self.open_db_button = Q.QPushButton("Open")
        # Delete data base
        self.delete_db_button = Q.QPushButton("Delete database")
        # Delete all records
        self.remove_all_button = Q.QPushButton("Remove all records")
        # Tab widget
        self.tabs = Q.QTabWidget()
        self.services = Table1()
        self.branches = Table2()
        self.customers = Table3()
        self.tos = Table4()
        self.tabs.addTab(self.services, "Services")
        self.tabs.addTab(self.branches, "Branches")
        self.tabs.addTab(self.customers, "Customers")
        self.tabs.addTab(self.tos, "Types of service")
        # Set layout
        main_layout = Q.QGridLayout()
        main_layout.addWidget(self.open_db_label, 0, 0)
        main_layout.addWidget(self.open_db_edit, 0, 1)
        main_layout.addWidget(self.open_db_button, 0, 2)
        main_layout.addWidget(self.delete_db_button, 0, 3)
        main_layout.addWidget(self.remove_all_button, 1, 2, 1, 2)
        main_layout.addWidget(self.tabs, 2, 0, 1, 4)
        self.central_widget.setLayout(main_layout)


        
