import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
import termcolor

from pymongo.database import Database 
from pymongo.collection import Collection

from bson import SON, raw_bson
from collections.abc import MutableMapping

import pandas as pd
import json
from bson import ObjectId
import os

class Mongo_operation:
    def __init__(self):
        self.uri=None
        self.client=None
        self.database=None
        self.collection=None
        self.is_closed=True
        
    def __str__(self):
        termcolor.cprint("MongoDB_CRUD Object -","dark_grey", attrs=['bold'], end='\n')
        termcolor.cprint("Connection String:",'dark_grey',attrs=['bold'], end=' ')
        termcolor.cprint(f"{self.uri}",'blue',attrs=['bold'], end='\n')
        termcolor.cprint("Database:",'dark_grey',attrs=['bold'], end=' ')
        termcolor.cprint(f"{None if self.database==None else self.database.name}",'blue',attrs=['bold'], end='\n')
        termcolor.cprint("Collection:",'dark_grey',attrs=['bold'], end=' ')
        termcolor.cprint(f"{None if self.collection==None else self.collection.name}",'blue',attrs=['bold'], end='\n')   
        termcolor.cprint("MongoClient:",'dark_grey',attrs=['bold'], end=' ')
        termcolor.cprint(f"{'Closed' if self.is_closed else 'Open'}",'blue',attrs=['bold'], end='\n')
        return ""     
        
    def get_mongo_client(self, uri):
        """
        Establishes a connection to MongoDB using the provided URI.
        
        Args:
        uri (str): MongoDB connection string.
        
        Returns:
        MongoClient: A MongoDB client object if the connection is successful.

        Raises:
        Exception: If there is an error during the connection process, an exception is raised.
        
        Example Usage:
        ```python
        client = my_object.get_mongo_client(uri)
        ```
        """
        try:
            self.uri=uri
            
            # Attempt to establish a connection to MongoDB
            client=MongoClient(self.uri)
            
            # Check the connection by issuing a command to the 'admin' database
            client.admin.command('ismaster')
            
            # Retrieve server information to further validate the connection
            client.server_info()
            
            # Check if the returned object is an instance of MongoClient
            if isinstance(client, MongoClient)==False:
                self.client=None
                raise Exception('The object is not a MongoDB client')
            
            # Set class attributes for the connected client
            self.client=client
            self.is_closed=False
            
            # Print the success message
            termcolor.cprint("Connected to MongoDB Successfully....",'green',attrs=['bold'])
            
            # Return the connected client
            return client
        
        except Exception as e:
            # Exception handling
            termcolor.cprint("Error during connection:","red", attrs=['bold'], end=' ')
            print(e)        
        
    def create_database(self, database_name):
        """
        Creates a MongoDB database with the specified name.

        Args:
        database_name (str): The name of the database to be created.

        Returns:
        None: Returns None if the database is created successfully.

        Raises:
        Exception: If there is an error during the database creation process, an exception is raised.
        
        Example Usage:
        ```python
        my_object.create_database("my_database")
        ```
        """
        try:
            client=self.client
            
            # Attempt to create a new database with the provided name
            self.database=client[database_name]
            
            if isinstance(self.database, Database)==False:
                self.database=None
                raise Exception("The object is not a database")
            termcolor.cprint("Database created successfully....",'green',attrs=['bold'])
            return None
        except Exception as e:
            termcolor.cprint("Error creating the database:","red", attrs=['bold'], end=' ')
            print(e) 
            
    def create_collection(self, collection_name):
        """
        Creates a MongoDB collection with the specified name within the current database.

        Args:
        collection_name (str): The name of the collection to be created.

        Returns:
        Collection: Returns the created collection object if successful.

        Raises:
        Exception: If there is an error during the collection creation process, an exception is raised.
        
        Example Usage:
        ```python
        # Assume that you have already get the MongoClient and create_collection
        
        collection=my_object.create_collection("my_database")
        ```
        """

        try:
            # Attempt to create a new collection with the provided name within the current database
            self.collection=self.database[collection_name]
            
            if isinstance(self.collection, Collection)==False:
                self.collection=None
                raise Exception("The object is not a collection")
            termcolor.cprint("Collection created successfully....",'green',attrs=['bold'])
            return self.collection
        except Exception as e:
            termcolor.cprint("Error creating the collection:","red", attrs=['bold'], end=' ')
            print(e)         
            
    def insert_data(self, data):  
        """
        Inserts data into the MongoDB collection.

        Args:
        data (dict or list): The data to be inserted. It can be a dictionary for a single document
                             or a list of dictionaries for multiple documents.

        Returns:
        None: Returns None if the data is inserted successfully.

        Raises:
        Exception: If there is an error during the insertion process, an exception is raised,
                   and an error message is printed.
                   
        Example Usage:
        ```python
        data={"name": "abc", "age": 27, "city": "New York"}
        my_object.insert_data(data)
        ```
        """
        try:
            if type(data) != list:
                if not isinstance(data, (dict, SON, raw_bson.RawBSONDocument, MutableMapping)):
                    raise Exception("Data is not in the correct format")
                    
            # Insert the one data entry
            if type(data) == dict:
                self.collection.insert_one(data)
                termcolor.cprint("Inserted successfully(Single entry)....",'green',attrs=['bold'])
                
            # Insert the multiple entries   
            elif type(data) ==list:
                # Verify all the elements of the list as a dict type
                for i,entry in enumerate(data):
                    if type(entry) != dict:
                        dtype=str(type(entry)).split("'")[1]
                        raise Exception(f"Data is not in correct format. \nData type at index {i} of list is '{dtype}', but the entries inside the 'list' should be 'dict' type.")
                self.collection.insert_many(data)
                termcolor.cprint("Data inserted successfully....",'green',attrs=['bold'])
            
            # If the data is not in correct format
            else:
                dtype=str(type(data)).split("'")[1]
                raise Exception(f"Data is not in correct format. \nThe data type of argument 'data' is '{dtype}', but argument 'data' should pass as 'list' or 'dict' type.")
        except Exception as e:
            termcolor.cprint("Error inserting the entry:","red", attrs=['bold'], end=' ')
            print(e) 
            
    def bulk_insert(self,datafile, collection_name=""):
        """
        Bulk insert data from a CSV, Excel, or JSON file into a MongoDB collection.

        Args:
        - datafile (str): Path to the data file (CSV, Excel, or JSON).
        - collection_name (str, optional): Name of the MongoDB collection. If not provided, the default collection is used.

        Raises:
        - Exception: If an error occurs during the data insertion process.

        Note:
        - The method assumes the MongoDB connection is already established.

        Example:
        ```python
        # If you want to save the data into existing collection
        my_object.bulk_insert('path/to/data.csv')
        
        # If you want to save the data into new collection
        my_object.bulk_insert('path/to/data.csv', 'my_collection')
        ```
        """
        try:
            self.path=datafile
            
            # Configure the type of the file
            if self.path.endswith('.csv'):
                dataframe=pd.read_csv(self.path,encoding='utf-8')

            elif self.path.endswith(".xlsx"):
                dataframe=pd.read_excel(self.path)

            elif self.path.endswith(".json"):
                with open(self.path, 'r') as json_file:
                    datajson = json.load(json_file)

            if not self.path.endswith(".json"):
                datajson=json.loads(dataframe.to_json(orient='records'))
            
            # Set the collection
            if collection_name!="":
                collection=self.create_collection(collection_name)
                
            # call the function to insert the data
            self.insert_data(datajson)
        except Exception as e:
            termcolor.cprint("Error in insert the data:",'red',attrs=['bold'],end=' ')
            print(e)
            
    def find_data(self, key_value=""):
        """
        Retrieves data from the MongoDB collection based on the specified key-value pair.

        Args:
        key_value (dict, optional): A dictionary representing the key-value pair to filter the results.
                                    If not provided or an empty dictionary, all documents are retrieved.

        Returns:
        DataFrame or list: Returns a Pandas DataFrame if the user chooses to display the data as a DataFrame,
                           otherwise returns a list of documents.

        Raises:
        Exception: If there is an error during the data retrieval process, an exception is raised,
                   and an error message is printed.
                   
        Example Usage:
        ```python
        # Find all the documents of the collection
        my_object.find_data()
        
        # Find the documents based on key_value
        key_value={'name': 'abc'}
        my_object.find_data(key_value)        
        ```
        """

        try:
            # Find all the documents 
            if key_value == "":
                item_details=self.collection.find()
            
            # Find the documents based on the key_value
            else:
                item_details=self.collection.find(key_value)
            
            # Store documents in list
            item_list=[]
            for item in item_details:
                item_list.append(item)
            
            # If list contains at least one document
            if len(item_list) != 0:
                flag=input("Do you want to print the data as a dataframe(y/n): ").lower()
                if flag=='y':
                    df=pd.DataFrame(item_list)
                    return df
                return item_list
            
            # If list does not contains any document
            else:
                termcolor.cprint("There are no document in the collection or no document for key_value.", 'dark_grey', attrs=['bold'])
        except Exception as e:
            termcolor.cprint("Error finding the data:","red", attrs=['bold'], end=' ')
            print(e)     
            
    def delete_data(self, key_value=""):
        """
        Deletes data from the MongoDB collection based on the specified key-value pair.

        Args:
        key_value (dict, optional): A dictionary representing the key-value pair to identify the documents to delete.
                                    If not provided or an empty dictionary, the user is prompted to delete all entries.

        Returns:
        None: Returns None after the deletion process is completed.

        Raises:
        Exception: If there is an error during the deletion process, an exception is raised,
                   and an error message is printed.
                   
        Example Usage:
        ```python
        # For delete the entire data of collection
        my_object.delete_data()
        
        # Delete the documents based on the key_value
        key_value={'age':38}
        my_object.delete_data(key_value)
        ```
        """

        try:
            # Delete the entire data of collection
            if key_value=="":
                flag=input("It will delete entire data, Do you want to delete the data?(y/n): ").lower()
                if flag=='y':
                    self.collection.delete_many({})
                    termcolor.cprint("All entry deleted",'magenta',attrs=['bold'])
                    return

                else:
                    termcolor.cprint("Nothing deleted")
                    return 
                
            # Delete the documents based on the key_value
            else:
                # Check the documents based on the key value
                item_list = list(self.collection.find(key_value))
                if len(item_list)==0:
                    termcolor.cprint("Entry doesn't exists of given key value.", 'dark_grey', attrs=['bold'])
                    return
                
                # Ask for delete single or multiple entries
                flag=input("Do you want delete the one entry or mutiple entries?(one/many) ").lower()

                if flag=='one':
                    self.collection.delete_one(key_value)
                    termcolor.cprint("Entry deleted successfully ","green", attrs=['bold'], end=' ')

                elif flag=='many':
                    self.collection.delete_many(key_value)
                    termcolor.cprint("Multiple entries deleted successfully ","green", attrs=['bold'], end=' ')
                else:
                    termcolor.cprint("Incorrect option:", "red", attrs=['bold'], end=' ')
                    print("choose either 'one' or 'many'")

        except Exception as e:
            termcolor.cprint("Error deleting the data:","red", attrs=['bold'], end=' ')
            print(e)
            
            
    def update_data_entry(self, filter_criteria, update_data):
        """
        Updates data in the MongoDB collection based on the specified filter criteria.

        Args:
        filter_criteria (dict): A dictionary representing the criteria to identify the documents to update.
        update_data (dict): A dictionary representing the update operation to be applied to matching documents.

        Returns:
        None: Returns None after the update operation is completed.

        Raises:
        Exception: If there is an error during the update process, an exception is raised,
                   and an error message is printed.
                   
        Example Usage:
        ```python
        filter_criteria = {'age': 28}
        update_data = [{'$set': {'age': 55}}]
        my_object.update_data_entry(filter_criteria, update_data)
        ```
        """

        try:
            # Retrieve documents based on the specified filter criteria
            item_list=list(self.collection.find(filter_criteria))
            
            # Raise the error if there is no document based on filter_criteria
            if len(item_list) == 0:
                raise Exception("Entry does not exist, can not update the data")

            # Ask to update single or multiple entries
            flag=input("Do you want single entry update on multiple?(one/many) ").lower()
            
            if flag=='one':    
                self.collection.update_one(filter_criteria, update_data)  
                termcolor.cprint("Updated Successfully (one entry)...","green", attrs=['bold'], end=' ')
            elif flag=='many':
                self.collection.update_many(filter_criteria, update_data)
                termcolor.cprint("Updated Successfully (multiple entries)....","green", attrs=['bold'], end=' ')
            else:
                raise Exception("Invalid input")
        except Exception as e:
            termcolor.cprint("Error updating the data:","red", attrs=['bold'], end=' ')
            print(e) 
    
    def save_data(self):
        """
        Save data from the MongoDB collection to either a JSON or CSV file.

        This method retrieves data from the MongoDB collection and allows the user
        to choose between saving it as a JSON or CSV file. The user is prompted to
        input the desired file format and filename. The data is then serialized and
        saved to the specified file.

        Args:
            No argument requires.

        Returns:
            None: The method doesn't return any value.

        Raises:
            Exception: Raised if there is an error during the file-saving process,
                       or if the specified file path does not exist.

         Example Usage:
        ```python
        my_object.save_data()
        ```
        """
    
        try:
            # Retrieve data from the MongoDB collection
            item_list=list(self.collection.find())
            data=item_list
            
            # Ask the user to save the type of the file
            flag=input("Do you want to save the data as json file or csv file?(json/csv)").lower()
            file_name=""
            
            # Store the file as json format
            if flag=='json':
                json_file=input("Enter the filename: ")
                serialized_data = json.dumps(data, default=self.convert_to_serializable, indent=2)
                with open(json_file, 'w') as jsonfile:
                    jsonfile.write(serialized_data)
                file_name=json_file
                
            # Store the file as csv format
            elif flag=='csv':
                csv_file_name =input("Enter the filename: ")
                df=pd.DataFrame(data)
                df.to_csv(csv_file_name)
                file_name=csv_file_name
                
            else:
                termcolor.cprint("Incorrect option:",'red',attrs=['bold'],end=' ')
                print("choose either 'json' or 'csv'")
                return
            
            # Check if the file is created or not
            if os.path.exists(file_name):
                    termcolor.cprint("File:", 'green', attrs=['bold'], end=' ')
                    termcolor.cprint(f"'{file_name}'", 'blue', attrs=['bold'], end=' ')
                    termcolor.cprint("saved successfully....", 'green', attrs=['bold'])
            else:
                raise Exception("File path is not exist")
                
        except Exception as e:
            termcolor.cprint("Error saving data:",'red',attrs=['bold'],end=' ')
            print(e)
            
            
    def close_mongo_client(self):
        """
        Closes the MongoDB client connection.

        Returns:
        None: Returns None after closing the MongoDB client.

        Raises:
        Exception: If there is an error during the closing process, an exception is raised,
                   and an error message is printed.
        """

        try:
            # Check the status of the MongoDB client connection
            result=self.client.admin.command('ismaster')
            primary=result.get('ismaster')==True
            secondary=result.get('ismaster')==False
            
            # Close the MongoDB client if it is open
            if primary or secondary or self.client:
                self.client.close()
                self.is_closed=True
                termcolor.cprint("MongoDB client closed successfully..",'magenta',attrs=['bold'])
            else:
                termcolor.cprint("MongoDB client is already closed or not provided.",'dark_grey',attrs=['bold'])

        except Exception as e:
            if str(e)=='Cannot use MongoClient after close':
                termcolor.cprint("MongoDB client is already closed.",'dark_grey',attrs=['bold'])
            else:
                termcolor.cprint("Error closing MongoDB client:","red", attrs=['bold'], end=' ')
                print(e) 