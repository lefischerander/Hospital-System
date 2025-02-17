from Database.db_access import connection_string
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
