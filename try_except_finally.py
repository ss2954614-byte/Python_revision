try:
    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    print("Database connected successfully.")

except ImportError:
    print("MySQL connector is not installed.")

except Exception as error:
    print(f"Unexpected Error: {error}")

finally:
    print("Connection process completed.")