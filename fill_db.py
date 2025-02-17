from db_access import connection_string
import pyodbc
import names


def fill_names(i_range):
    """Fills the database with random names

    Args:
        range (int): The number of names to fill
    """
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    for i in range(i_range):
        cursor.execute(
            "update A set firstname=?, surname =? from (select subject_id, firstname, surname, ROW_NUMBER() over (order by subject_id) rn from dbo.patients) A where rn = ?",
            names.get_first_name(),
            names.get_last_name(),
            i,
        )

    cursor.commit()


# fill_names(101)

# password = "test"  # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
# password2 = "hallo"  # d3751d33f9cd5049c4af2b462735457e4d3baf130bcbb87f389e349fbaeb20b9


# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()


# print(hash_password(password))
# print(hash_password(password2))
