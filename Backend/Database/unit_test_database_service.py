import unittest
from Database.database_service import User_service
from unittest.mock import MagicMock
import pandas as pd


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.mock_row = MagicMock()
        self.mock_row_firstname = "Terry"
        self.mock_row_surname = "Forest"
        self.mock_row_department = "Surgery"
        self.mock_row_age = 45
        self.df = pd.DataFrame(
            {
                "subject_id": [10002495],
                "password": [
                    "d3751d33f9cd5049c4af2b462735457e4d3baf130bcbb87f389e349fbaeb20b9"
                ],
                "role": ["Patient"],
            }
        )

    def test_getRole(self):
        us = User_service()
        self.assertEqual(us.get_role_by_id(30000000), "Doctor")
        self.assertEqual(us.get_role_by_id(40000000), "Admin")
        self.assertEqual(us.get_role_by_id(10002495), "Patient")

    def test_get_doctor_by_name(self):
        us = User_service()
        doctor = us.get_doctor_by_name("Forest")
        self.assertEqual(doctor.firstname, self.mock_row_firstname)
        self.assertEqual(doctor.surname, self.mock_row_surname)
        self.assertEqual(doctor.department, self.mock_row_department)
        self.assertEqual(doctor.age, self.mock_row_age)

    def test_getTable(self):
        us = User_service()
        data = us.read_table_sa("login_data")
        data2 = us.read_table_sa("omr").head(1)
        self.assertEqual(data.head(1).equals(self.df), True)
        self.assertEqual(data2.equals(self.df), False)
        self.assertEqual(len(data), 4)

    def test_getMore(self):
        us = User_service()
        email = us.get_admin_email()
        self.assertEqual(email, "konsti.krümmel@stud.txt-uni.de")


if __name__ == "__main__":
    unittest.main()
