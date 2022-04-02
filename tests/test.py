"""Testing database app"""
import sys
from os.path import dirname
from hamcrest import assert_that, equal_to
from utils import get_app, open_db, compare_list_and_table
sys.path.insert(0, dirname(__file__))
from main import MainWindow


def test_delete_record():
    """Test delete record function"""
    app = get_app()
    window = MainWindow()
    assert_that(window.delete_record("", [""]), equal_to(None))


def test_get_service_record_empty():
    """Test get service record function with empty line edits"""
    app = get_app()
    window = MainWindow()
    assert_that(window.get_service_record(), equal_to(None))


def test_get_service_record():
    """Test get service record function with filled line edits"""
    app = get_app()
    window = MainWindow()
    window.ui.services.branch.edit.setText("1")
    window.ui.services.type.edit.setText("2")
    window.ui.services.customer.edit.setText("3")
    window.ui.services.date.edit.setText("4")

    expected_values = ["1", "2", "3", "4"]
    assert_that(window.get_service_record(), equal_to(expected_values))


def test_get_tos_record_empty():
    """Test get tos record function with empty line edits"""
    app = get_app()
    window = MainWindow()
    assert_that(window.get_tos_record(), equal_to(None))


def test_get_tos_record():
    """Test get tos record function with filled line edits"""
    app = get_app()
    window = MainWindow()
    window.ui.tos.id.edit.setText("1")
    window.ui.tos.name.edit.setText("2")
    window.ui.tos.type.edit.setText("3")
    window.ui.tos.cost.edit.setText("4")

    expected_values = ["1", "2", "3", "4"]
    assert_that(window.get_tos_record(), equal_to(expected_values))


def test_get_branches_record_empty():
    """Test get branches record function with empty line edits"""
    app = get_app()
    window = MainWindow()
    assert_that(window.get_branches_record(), equal_to(None))


def test_get_branches_record():
    """Test get branches record function with filled line edits"""
    app = get_app()
    window = MainWindow()
    window.ui.branches.id.edit.setText("1")
    window.ui.branches.name.edit.setText("2")
    window.ui.branches.address.edit.setText("3")
    window.ui.branches.phone_number.edit.setText("4")

    expected_values = ["1", "2", "3", "4"]
    assert_that(window.get_branches_record(), equal_to(expected_values))


def test_get_customers_record_empty():
    """Test get customers record function with empty line edits"""
    app = get_app()
    window = MainWindow()
    assert_that(window.get_customers_record(), equal_to(None))


def test_get_customers_record():
    """Test get customers record function with filled line edits"""
    app = get_app()
    window = MainWindow()
    window.ui.customers.id.edit.setText("1")
    window.ui.customers.last_name.edit.setText("2")
    window.ui.customers.first_name.edit.setText("3")
    window.ui.customers.phone_number.edit.setText("4")

    expected_values = ["1", "2", "3", "4"]
    assert_that(window.get_customers_record(), equal_to(expected_values))


def test_search_branches_by_name_empty():
    """Test search branches by name function with empty data"""
    app = get_app()
    window = MainWindow()

    assert_that(window.search_branches_by_name(), equal_to(None))


def test_search_branches_by_name():
    """Test search branches by name function with filled data"""
    app = get_app()
    window = MainWindow()
    open_db(window)

    window.ui.branches.id.edit.setText("1")
    window.ui.branches.name.edit.setText("1")
    window.ui.branches.address.edit.setText("1")
    window.ui.branches.phone_number.edit.setText("1")
    window.add_branches()

    window.ui.branches.id.edit.setText("2")
    window.ui.branches.name.edit.setText("2")
    window.ui.branches.address.edit.setText("2")
    window.ui.branches.phone_number.edit.setText("2")
    window.add_branches()

    window.ui.branches.name.edit.setText("1")
    window.search_branches_by_name()

    expected_lst = [["1", "1", "1", "1"]]
    assert_that(compare_list_and_table(expected_lst, window.ui.branches.table), equal_to(True))


def test_search_tos_by_type_empty():
    """Test search tos by type function with empty data"""
    app = get_app()
    window = MainWindow()

    assert_that(window.search_tos_by_type(), equal_to(None))


def test_search_tos_by_type():
    """Test search tos by type function with filled data"""
    app = get_app()
    window = MainWindow()
    open_db(window)

    window.ui.tos.id.edit.setText("1")
    window.ui.tos.name.edit.setText("1")
    window.ui.tos.type.edit.setText("1")
    window.ui.tos.cost.edit.setText("1")
    window.add_tos()

    window.ui.tos.id.edit.setText("2")
    window.ui.tos.name.edit.setText("2")
    window.ui.tos.type.edit.setText("2")
    window.ui.tos.cost.edit.setText("2")
    window.add_tos()

    window.ui.tos.type.edit.setText("1")
    window.search_tos_by_type()

    expected_lst = [["1", "1", "1", "1"]]
    assert_that(compare_list_and_table(expected_lst, window.ui.tos.table), equal_to(True))


def test_search_by_first_name_empty():
    """Test search by first name function with empty data"""
    app = get_app()
    window = MainWindow()

    assert_that(window.search_by_first_name(), equal_to(None))


def test_search_by_first_name():
    """Test search by first name function with filled data"""
    app = get_app()
    window = MainWindow()
    open_db(window)

    window.ui.customers.id.edit.setText("1")
    window.ui.customers.last_name.edit.setText("1")
    window.ui.customers.first_name.edit.setText("1")
    window.ui.customers.phone_number.edit.setText("1")
    window.add_customers()

    window.ui.customers.id.edit.setText("2")
    window.ui.customers.last_name.edit.setText("2")
    window.ui.customers.first_name.edit.setText("2")
    window.ui.customers.phone_number.edit.setText("2")
    window.add_customers()

    window.ui.customers.first_name.edit.setText("1")
    window.search_by_first_name()

    expected_lst = [["1", "1", "1", "1"]]
    assert_that(compare_list_and_table(expected_lst, window.ui.customers.table), equal_to(True))
