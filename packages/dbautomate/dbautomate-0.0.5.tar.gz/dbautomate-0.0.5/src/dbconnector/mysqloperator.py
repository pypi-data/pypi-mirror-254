import termcolor
import mysql.connector
import time
from prettytable import PrettyTable

import csv
import os

class MySQL_operation:
    def __init__(self):
        self.config=None
        self.connection = None
        self.cursor = None
        
    def __str__(self):
        termcolor.cprint("MySQLHandler Object -","dark_grey", attrs=['bold'], end='\n')
        termcolor.cprint("Config:",attrs=['bold'], end=' ')
        termcolor.cprint(f"{self.config}",'blue',attrs=['bold'], end='\n')
        termcolor.cprint("Connected:",attrs=['bold'], end=' ')
        termcolor.cprint(f"{self.connection is not None}",'blue',attrs=['bold'], end='\n')
        return ""
        
    def connect_to_mysql(self, config, attempts=3, delay=2):
        """
        Attempt to establish a connection to a MySQL database.

        Parameters:
        - attempts (int): The maximum number of connection attempts (default is 3).
        - delay (int): The delay in seconds between connection attempts (default is 2).

        Returns:
        - mysql.connector.connection.MySQLConnection or None: The MySQL database connection object if successful,
          or None if the connection attempts are exhausted.

        Raises:
        - mysql.connector.Error: If a MySQL-specific error occurs during connection.
        - IOError: If an I/O error occurs during connection.
        - Exception: For general exceptions during connection.
        
        Example Usage:
        ```python
        config = {
            'host': 'your_mysql_host',
            'user': 'your_mysql_user',
            'password': 'your_mysql_password',
            'database': 'your_database_name'
        }
        # Initiate MySQL object
        mysql_handler=MySQL_connector()
        connection = mysql_handler.connect_to_mysql(config, attempts=3, delay=2)
        ```
        """
        self.config=config
        attempt = 1
        # Implement a reconnection routine
        while attempt < attempts + 1:
            try:
                no_dict=""
                if type(self.config)!= dict:
                    no_dict="Not dict type"
                self.connection=mysql.connector.connect(**self.config)
                self.cursor = self.connection.cursor()                 
                termcolor.cprint("Connected successfully....","green", attrs=['bold'], end='\n')
                return self.connection  
            except (mysql.connector.Error, IOError, Exception) as e:
                if (attempts is attempt):
                    # Attempts to reconnect failed; returning None
                    termcolor.cprint("Failed to connect, exiting without a connection:","red", attrs=['bold'], end=' ')
                    print(e, no_dict)
                    return None
                # progressive reconnect delay
                time.sleep(delay ** attempt)
                attempt += 1
        return None
        
    def execute_query(self, query):
        """
        Execute a SQL query and display displays the results in a formatted table. Or simply execute query only.
        
        Parameters:
        - query (str): The SQL query to be executed.
        
        Returns:
        None
        
        Raises:
        - Exception: If an error occurs during the query execution or result retrieval.
        
        Example Usage:
        ```python
        # Assuming an instance of your class is created, let's call it 'mysql_handler'
        # Assuming you have a database connection

        # Execute a query
        select_query = "SELECT * FROM my_table"
        mysql_handler.execute_query(select_query)
        ```
        """
        try:
            self.cursor.execute(query) 
            try:
                rows = self.cursor.fetchall()
                column_names = [desc[0] for desc in self.cursor.description]
                # Display results using PrettyTable
                if rows:
                    table = PrettyTable(column_names)
                    table.align = 'l'
                    for row in rows:
                        table.add_row(row)
                    termcolor.cprint("Query executed successfully....","green", attrs=['bold'], end='\n')
                    print(table)
                else:
                    termcolor.cprint("No results found.","red", attrs=['bold'], end=' ')

            except Exception as e:
                termcolor.cprint("Query:","green", attrs=['bold'], end=' ')
                termcolor.cprint(f"\"{query}\"","blue", attrs=['bold'], end=' ')
                termcolor.cprint("executed successfully.","green", attrs=['bold'], end=' ')
                return
        except Exception as e:
            termcolor.cprint("Error executing query:","red", attrs=['bold'], end=' ')
            print(e)
    
    # Helper function
    def fetch_db(self,db_name):
        """
        Set the active database for the current connection and retrieve the current database.

        Parameters:
        - db_name (str): The name of the database to use. If an empty string is provided,
          the method retrieves the current active database.
        
        Returns:
        - cursor (object): A cursor object connected to the selected database.
        - db_name (str): The name of the database that was fetched or switched to.
        
        Raises:
        - Exception: If an error occurs during the database selection or retrieval.
        """
        if db_name=="":
            cursor=self.connection.cursor()
            query_select="select database()"
            cursor.execute(query_select)
            db=cursor.fetchall()
            db_name=db[0][0]
            return cursor,db_name
        else:
            try:
                cursor=self.connection.cursor()
                query_db=f"use {db_name}"
                cursor.execute(query_db)
                return cursor,db_name
            except Exception as e:
                termcolor.cprint("Error using db_name:","red", attrs=['bold'], end=' ')
                print(e,end='')
                return None,None
            
    # Helper function
    def fetch_tables(self,cursor):
        """
        Retrieve a list of table names in the connected database using the provided database cursor.

        Parameters:
        - cursor: The database cursor used to execute the query.

        Returns:
        - list: A list containing the names of the tables in the connected database.
        """
        query_tables='show tables'
        cursor.execute(query_tables)
        tables=cursor.fetchall()
        list_table=[table[0]  for table in tables]
        return list_table
    
    
    def insert_data(self, table_name, values, db_name =""):
        """
        Insert data into a specified table in the connected database.

        Parameters:
        - table_name (str): The name of the table where the data will be inserted.
        - values (list or tuple): The values to be inserted into the table.
        - db_name (str, optional): The name of the database. If not provided, the active database is used.

        Returns:
        None

        Raises:
        - Exception: If an error occurs during the data insertion process.
        
        Example Usage:
        ```python
        # Assuming an instance of your class is created, let's call it 'mysql_handler'
        # Assuming you have an established database connection
        
        # Insert single entry into the 'example_table' in the active database
        values_single_entry = (1, 'John Doe', 25)
        mysql_handler.insert_data("example_table", values_single_entry)

        # Insert multiple entries into the 'example_table' in the specified database
        values_multiple_entries = [
            (1, 'John Doe', 25),
            (2, 'Jane Smith', 30),
            (3, 'Bob Johnson', 22)
        ]
        mysql_handler.insert_data("example_table", values_multiple_entries, db_name="my_database")
        ```
        """
        # Fetch the database and cursor
        cursor,db_name=self.fetch_db(db_name)
        if db_name==None:
            return
        else:
            print(f"Your database: '{db_name}'")

        try: 
            # Fetch the tables of the database
            list_table=self.fetch_tables(cursor)
            
            if table_name in list_table:
                termcolor.cprint("Your table:","green", attrs=['bold'], end=' ')
                termcolor.cprint(f"'{table_name}'", "blue", attrs=['bold'], end=' ')
                termcolor.cprint(", present in the database", end=' ')
                termcolor.cprint(f"'{db_name}'", "blue", attrs=['bold'], end='\n')

            else:
                termcolor.cprint("Table not found:", "red", attrs=['bold'], end=' ')
                print(f"'{table_name}' is not present in the database '{db_name}'.")
                print(f"Select one of the following tables ", end='')
                termcolor.cprint(f"{list_table}", attrs=['bold'], end=' ')
                print("or create new table or use another database.")
                return
        except Exception as e:
            termcolor.cprint("Error fetching the tables:","red", attrs=['bold'], end=' ')
            print(e)
            return

        # Fetch the columns of table
        try:   
            query_table=f"select * from {table_name}"
            cursor.execute(query_table)
            cursor.fetchall()
            desc=cursor.description
            columns=[t[0] for t in desc]

            flag=input("Enter yes if the first value of argument is 'id' and you have not provided: ").lower()
            if flag=='y' or flag=='yes':
                columns=columns[1:]
            d=str(tuple(columns))
            column_table=d.replace('\'','')

        except Exception as e:
            termcolor.cprint("Error fetching column names:","red", attrs=['bold'], end=' ')
            print(e)
            return

        # Write query and insert the data
        query= f"INSERT INTO {table_name} {column_table} VALUES ({', '.join('%s' for _ in columns)})"
        try:
            tmp=0
            while(tmp<3):
                flag_insert=input("Are you inserting more than one entry?(y/n) ").lower()
                if flag_insert=='y':
                    cursor.executemany(query, values)
                    break
                elif flag_insert=='n':    
                    cursor.execute(query, values)
                    break
                else:
                    print("Incorrect option..")
                tmp+=1
            if tmp==3:
                termcolor.cprint("Program exited without inserting","magenta", attrs=['bold'], end=' ')
                return
            self.connection.commit()
            termcolor.cprint("Inserted successfully....", 'green', attrs=['bold'], end=' ')
        except Exception as e:
            termcolor.cprint("Error inserting data:","red", attrs=['bold'], end=' ')
            print(e)
        
    def save_data(self, table_name, db_name=""):
        """
        Save data from a specified table in the connected database to a CSV file.

        Parameters:
        - table_name (str): The name of the table from which data will be saved.
        - db_name (str, optional): The name of the database where the given table is present. If not provided, the active database is used.

        Returns:
        None

        Raises:
        - Exception: If an error occurs during the data retrieval or CSV file creation process.
        
        Example Usage:
        ```python
        # Assuming an instance of your class is created, let's call it 'mysql_handler'
        # Assuming you have an established database connection

        # Save data from the 'example_table' in the active database to a CSV file
        mysql_handler.save_data("example_table")

        # Save data from the 'another_table' in the specified database to a CSV file
        mysql_handler.save_data("another_table", db_name="my_database")
        ```       
        """
        cursor,db_name=self.fetch_db(db_name)
        if db_name==None:
            return

        try: 
            list_table=self.fetch_tables(cursor)
            
            if table_name not in list_table:
                termcolor.cprint("Table not found:", "red", attrs=['bold'], end=' ')
                print(f"'{table_name}' is not present in the database '{db_name}'.")
                print(f"Select one of the following tables ", end='')
                termcolor.cprint(f"{list_table}", attrs=['bold'], end=' ')
                print("or create new table or use another database.")
                return

        except Exception as e:
            termcolor.cprint("Error fetching the tables:","red", attrs=['bold'], end=' ')
            print(e)
            return

        try:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            csv_file_name =input("Enter the filename: ")
            # Create the full path for the output CSV file
            file_path=os.path.join(os.getcwd(), csv_file_name)
            with open(file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(column_names)
                csv_writer.writerows(rows)
            if os.path.exists(csv_file_name):
                termcolor.cprint("File:", 'green', attrs=['bold'], end=' ')
                termcolor.cprint(f"'{csv_file_name}'", 'blue', attrs=['bold'], end=' ')
                termcolor.cprint("saved successfully....", 'green', attrs=['bold'])

        except Exception as e:
            termcolor.cprint("Error saving data:","red", attrs=['bold'], end=' ')
            print(e)
            
    def close_connection(self):
        """
        Close the active MySQL database connection.

        If a connection is active, close both the cursor and the connection. If no active connection is found,
        print a message indicating that the MySQL connection is not active.

        Parameters:
        None

        Returns:
        None
        
        Example Usage:
        ```python
        # Assuming an instance of your class is created, let's call it 'mysql_handler'
        # Assuming you have an established database connection

        # Close the active MySQL connection
        mysql_handler.close_connection()
        ```
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
            termcolor.cprint("MySQL connection closed.","dark_grey", attrs=['bold'], end=' ')
            self.connection=None
        else:
            termcolor.cprint("MySQL connection is not active, may be connection is already closed.","magenta", attrs=['bold'], end=' ')
         