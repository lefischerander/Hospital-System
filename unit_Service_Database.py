import unittest
from unittest.mock import patch, MagicMock
from Service_Database import User_service



#Mock means simulate

class TestService:
    
    def Set_up(self):
        """Set up the test environment before each test runs"""
        self.service = User_service()

    #Mock pyodbc connection
    @patch("pyodbc.connect") 
    
    
    def test_get_role_by_id(self, mock_connect):

         # Mock database behavior
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = ["Doctor"]  # Mocking return value
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

         # Test function
        role = self.service.get_role_by_id(123)

        # Assertions
        self.assertEqual(role, "Doctor")
        mock_cursor.execute.assert_called_with(
            f"select role from {self.service.LOGIN_DATA} where subject_id = ?", 123
        )
    
    def test_delete_user_not_admin(self, mock_connect):
        """Test delete_user() when caller is not admin"""

        # Mocking get_role_by_id to return "Doctor" instead of "admin"
        self.service.get_role_by_id = MagicMock(return_value="Doctor")

        with patch("tkinter.messagebox.showinfo") as mock_msgbox:
            self.service.delete_user(123, 456)  # 456 is caller_id

            mock_msgbox.assert_called_with("Diagnosis added successfully")

    @patch("pyodbc.connect")
    def test_create_user(self, mock_connect):
        """Test create_user() function"""

        # Mock database connection
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        # Test function
        self.service.create_user(101, "pass123", "Doctor", "John", "Doe")

        # Assertions
        mock_cursor.execute.assert_called_with(
            f"INSERT INTO {self.service.LOGIN_DATA} (subject_id, password, role, firstname, surname) VALUES (?, ?, ?, ?, ?)",
            101,
            "pass123",
            "Doctor",
            "Leander",
            "Kolbek",
        )
        mock_conn.commit.assert_called()




if __name__ == "__main__":
    unittest.main()