import unittest
from unittest.mock import patch, MagicMock #for mocking the database
from Service_Database import User_service



#Mock means simulate

class TestService:
    
    def Set_up(self):
        """Set up the test environment before each test runs"""
        self.service = User_service()

    #Mock pyodbc connection
    
    @patch("pyodbc.connect") #replace pyodbc.connect with a mock object
    
    
    def test_get_role_by_id(self, fake_connect):

         # Mock database behavior
        fake_conn = MagicMock() #creating an instance of the subclass that replaces pyodbc.connect()
                                
        fake_cursor = MagicMock() #replacecs 'cursor = connection.cursor()'
        fake_cursor.fetchone.return_value = ["Doctor"]  # Mocking return value
        fake_conn.cursor.return_value = fake_cursor # returning a mocked object
        fake_connect.return_value = fake_conn # instead returning a database connectio it will return a mock connection

         # Test function
        role = self.service.get_role_by_id(123)

        # Assertions
        self.assertEqual(role, "Doctor")
        fake_cursor.execute.assert_called_with(
            f"select role from {self.service.LOGIN_DATA} where subject_id = ?", 123
        )
    
    def test_delete_user_not_admin(self):
        """Test delete_user() when caller is not admin"""

        # Mocking get_role_by_id to return "Doctor" instead of "admin"
        self.service.get_role_by_id = MagicMock(return_value="Doctor")

        with patch("tkinter.messagebox.showinfo") as mock_msgbox:
            self.service.delete_user(123, 456)  # 456 is caller_id

            mock_msgbox.assert_called_with("user deleted successfully")

    @patch("pyodbc.connect")
    
    def test_create_user(self, fake_connect):
        """Test create_user() function"""

        # Mock database connection
        fake_conn = MagicMock() #creating an instance of the subclass that replaces pyodbc.connect()
        fake_cursor = MagicMock()  #replacecs 'cursor = connection.cursor()'
        fake_conn.cursor.return_value = fake_cursor # returning a mocked object
        fake_cursor.return_value = fake_conn # instead returning a database connectio it will return a mock connection


        # Test function
        self.service.create_user(2000, "pass123", "Doctor", "Leander", "Kolbek")

        # Assertions
        fake_cursor.execute.assert_called_with(
            f"INSERT INTO {self.service.LOGIN_DATA} (subject_id, password, role, firstname, surname) VALUES (?, ?, ?, ?, ?)",
            2000,
            "pass123",
            "Doctor",
            "Leander",
            "Kolbek",
        )
        fake_conn.commit.assert_called()




if __name__ == "__main__":
    unittest.main()