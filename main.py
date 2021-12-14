import database
import sys
from PyQt5 import Qt as Q
from gui import Ui


class MainWindow(Q.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui()
        self.ui.setupUi(self)
        self.db_name = ""
        # Create database
        self.ui.open_db_button.clicked.connect(self.create_db)
        # Delete database
        self.ui.delete_db_button.clicked.connect(self.delete_db)
        # Add record to Services
        self.ui.services.add_record_button.clicked.connect(self.add_services)
        # Add record to Branches
        self.ui.branches.add_record_button.clicked.connect(self.add_branches)
        # Add record to Customers
        self.ui.customers.add_record_button.clicked.connect(self.add_customers)
        # Add record to Types of service
        self.ui.tos.add_record_button.clicked.connect(self.add_tos)
        # Remove all records from Services
        self.ui.services.remove_all_button.clicked.connect(
            self.delete_services)
        # Remove all records from Branches
        self.ui.branches.remove_all_button.clicked.connect(
            self.delete_branches)
        # Remove all records from Customers
        self.ui.customers.remove_all_button.clicked.connect(
            self.delete_customers)
        # Remove all records from Types of service
        self.ui.tos.remove_all_button.clicked.connect(self.delete_tos)
        # Remove records from all tables
        self.ui.remove_all_button.clicked.connect(self.delete_all_tables)
        # Remove customers by first name
        self.ui.customers.remove_record.clicked.connect(
            self.delete_customers_by_name)
        # Remove branches by name
        self.ui.branches.remove_record.clicked.connect(
            self.delete_branches_by_name)
        # Remove tos by type
        self.ui.tos.remove_record.clicked.connect(self.delete_tos_by_type)
        # Remove services by date
        self.ui.services.remove_record.clicked.connect(
            self.delete_services_by_date)

    def delete_services_by_date(self):
        date = self.ui.services.date.edit.text()
        if not date:
            self.missing_value_message("Date")
            return
        if self.db_name:
            self.db.delete_services_by_date(date)
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_tos_by_type(self):
        type = self.ui.tos.type.edit.text()
        if not type:
            self.missing_value_message("Type")
            return
        if self.db_name:
            self.db.delete_tos_by_type(type)
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_branches_by_name(self):
        name = self.ui.branches.name.edit.text()
        if not name:
            self.missing_value_message("Name")
            return
        if self.db_name:
            self.db.delete_branches_by_name(name)
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_customers_by_name(self):
        name = self.ui.customers.first_name.edit.text()
        if not name:
            self.missing_value_message("Name")
            return
        if self.db_name:
            self.db.delete_clients_by_name(name)
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_tos(self):
        if self.db_name:
            self.db.delete_tos()
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_customers(self):
        if self.db_name:
            self.db.delete_clients()
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_branches(self):
        if self.db_name:
            self.db.delete_branches()
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_services(self):
        if self.db_name:
            self.db.delete_services()
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def no_db_name_message(self):
        message = Q.QMessageBox()
        message.setIcon(Q.QMessageBox.Warning)
        message.setText("Enter database name")
        message.setWindowTitle("Warning")
        message.exec_()

    def missing_value_message(self, name):
        message = Q.QMessageBox()
        message.setIcon(Q.QMessageBox.Warning)
        message.setText(f"{name} missing value")
        message.setWindowTitle("Warning")
        message.exec_()

    def add_tos(self):
        if self.db_name:
            # Check id
            id = self.ui.tos.id.edit.text()
            if not id:
                self.missing_value_message("Id")
                return
            # Check name
            name = self.ui.tos.name.edit.text()
            if not name:
                self.missing_value_message("Name")
                return
            # Check type
            type = self.ui.tos.type.edit.text()
            if not type:
                self.missing_value_message("Type")
                return
            # Check cost
            cost = self.ui.tos.cost.edit.text()
            if not cost:
                self.missing_value_message("Cost")
                return
            self.db.add_to_tos(id, name, type, cost)
            self.refresh_tos_table()
        else:
            self.no_db_name_message()

    def refresh_tos_table(self):
        records = self.db.get_tos()
        table = self.ui.tos.table
        table.setRowCount(len(records))
        for i in range(len(records)):
            for j in range(len(records[i])):
                if records[i][j]:
                    table.setItem(i, j, Q.QTableWidgetItem(str(records[i][j])))

    def add_customers(self):
        if self.db_name:
            # Check id
            id = self.ui.customers.id.edit.text()
            if not id:
                self.missing_value_message("Id")
                return
            # Check last name
            last_name = self.ui.customers.last_name.edit.text()
            if not last_name:
                self.missing_value_message("Last name")
                return
            # Check first name
            first_name = self.ui.customers.first_name.edit.text()
            if not first_name:
                self.missing_value_message("First name")
                return
            # Check phone number
            phone_number = self.ui.customers.phone_number.edit.text()
            if not phone_number:
                self.missing_value_message("Phone number")
                return
            # Check total sum
            total_sum = self.ui.customers.total_sum.edit.text()
            if not total_sum:
                self.missing_value_message("Total sum")
                return
            self.db.add_to_clients(id, first_name, last_name, phone_number)
            self.refresh_customers_table()
        else:
            self.no_db_name_message()

    def refresh_customers_table(self):
        records = self.db.get_clients()
        table = self.ui.customers.table
        table.setRowCount(len(records))
        for i in range(len(records)):
            for j in range(len(records[i])):
                if records[i][j]:
                    table.setItem(i, j, Q.QTableWidgetItem(str(records[i][j])))

    def add_branches(self):
        if self.db_name:
            # Check id
            id = self.ui.branches.id.edit.text()
            if not id:
                self.missing_value_message("Id")
                return
            # Check name
            name = self.ui.branches.name.edit.text()
            if not name:
                self.missing_value_message("Name")
                return
            # Check address
            address = self.ui.branches.address.edit.text()
            if not address:
                self.missing_value_message("Address")
                return
            # Check phone number
            phone_number = self.ui.branches.phone_number.edit.text()
            if not phone_number:
                self.missing_value_message("Phone number")
                return
            self.db.add_to_branches(id, name, address, phone_number)
            self.refresh_branches_table()
        else:
            self.no_db_name_message()

    def refresh_branches_table(self):
        records = self.db.get_branches()
        table = self.ui.branches.table
        table.setRowCount(len(records))
        for i in range(len(records)):
            for j in range(len(records[i])):
                if records[i][j]:
                    table.setItem(i, j, Q.QTableWidgetItem(str(records[i][j])))

    def add_services(self):
        if self.db_name:
            # Check branch
            branch_id = self.ui.services.branch.edit.text()
            if not branch_id:
                self.missing_value_message("Branch id")
                return
            # Check type
            type_id = self.ui.services.type.edit.text()
            if not type_id:
                self.missing_value_message("Type id")
                return
            # Check customer
            customer_id = self.ui.services.customer.edit.text()
            if not customer_id:
                self.missing_value_message("Customer id")
                return
            # Check date
            date = self.ui.services.date.edit.text()
            if not date:
                self.missing_value_message("Date")
                return
            self.db.add_to_services(branch_id, type_id, customer_id, date)
            self.refresh_services_table()
            self.refresh_customers_table()
        else:
            self.no_db_name_message()

    def refresh_services_table(self):
        records = self.db.get_services()
        table = self.ui.services.table
        table.setRowCount(len(records))
        for i in range(len(records)):
            for j in range(len(records[i])):
                if records[i][j]:
                    table.setItem(i, j, Q.QTableWidgetItem(str(records[i][j])))

    def refresh_all_tables(self):
        self.refresh_services_table()
        self.refresh_branches_table()
        self.refresh_customers_table()
        self.refresh_tos_table()

    def delete_all_tables(self):
        if self.db_name:
            self.delete_services()
            self.delete_branches()
            self.delete_customers()
            self.delete_tos()
        else:
            self.no_db_name_message()

    def create_db(self):
        self.db_name = self.ui.open_db_edit.text()
        if self.db_name:
            self.db = database.DatabasePy(self.db_name)
            self.ui.open_db_edit.setReadOnly(True)
            self.ui.open_db_button.setEnabled(False)
            self.refresh_all_tables()
        else:
            self.no_db_name_message()

    def delete_db(self):
        if self.db_name:
            self.db.drop_db()
            self.ui.open_db_edit.setReadOnly(False)
            self.ui.open_db_button.setEnabled(True)
            self.db_name = ""
            self.ui.open_db_edit.setText("")
            self.delete_all_tables()


if __name__ == '__main__':
    app = Q.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
