"""
Database Class Documentation

This module defines a simple Database class that allows storing, updating, and retrieving data in a key-value format.
The data is stored in a JSON file and can be optionally converted to a CSV file.

Usage:
    1. Create an instance of the Database class by providing a name for the database.
    2. Use various methods to interact with the database, such as adding, updating, deleting, and retrieving entries.
    3. Optionally, convert the stored data to a CSV file using the json2csv method.

Example:
    # Create a database instance
    my_database = DataBase("example_database")

    # Add an entry to the database
    my_database.add_entry("key1", {"name": "John", "age": 30, "city": "New York"})

    # Retrieve an entry from the database
    entry = my_database.get_entry("key1")
    print(entry)

    # Update an entry in the database
    my_database.update_entry("key1", {"name": "John Doe", "age": 31, "city": "San Francisco"})

    # Delete an entry from the database
    my_database.del_entry("key1")

    # Convert JSON data to CSV
    my_database.json2csv()

    # Clear all entries in the database
    my_database.clear()

Note:
    - The data is stored in a JSON file named "{database_name}.json".
    - The CSV file, if generated, will be named "{database_name}.csv".
"""


import json
import csv
from exceptions import EntryNotFoundError

class DataBase:

    def __init__(self, name) -> None:
        """
        Initialize a database instance.

        Parameters:
        - name (str): The name of the database.
        """
        self.name: str = name
        self.data: dict = self.__load_data()

    
    def __load_data(self) -> dict:
        """
        Load data from the specified JSON file.

        Returns:
        dict: Loaded data from the JSON file.
        """
        try:
            with open(f'{self.name}.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}


    def __save_data(self):
        """
        Save data to the specified JSON file.
        """
        try:
            with open(f'{self.name}.json', 'w', encoding='utf-8') as file:
                json.dump(self.data, file)
        except IOError as e:
            # Handle the exception, e.g., logging or raising a custom exception
            print(f"Error saving data: {e}")

        
    
    def add_entry(self, key: str, value: dict) -> None:
        """
        Add an entry to the database.

        Parameters:
        - key (str): The key of the entry.
        - value (dict): The value (data) associated with the key.
        """
        self.data[key] = value
        self.__save_data()


    def update_entry(self, key: str, value: dict) -> None:
        """
        Update an entry in the database.

        Parameters:
        - key (str): The key of the entry to be updated.
        - value (dict): The updated value (data) associated with the key.
        """
        self.data[key] = value
        self.__save_data()


    def del_entry(self, key: str) -> None:
        """
        Delete an entry from the database.

        Parameters:
        - key (str): The key of the entry to be deleted.

        Raises:
        EntryNotFoundError: If the specified key is not found.
        """
        try:
            del self.data[key]
            self.__save_data()
        except KeyError:
            raise EntryNotFoundError(f"Entry with key '{key}' not found.")
    

    def get_entry(self, key: str) -> dict:
        """
        Get an entry from the database.

        Parameters:
        - key (str): The key of the entry to retrieve.

        Returns:
        dict: The value (data) associated with the specified key.
        """
        return self.data.get(key)


    def get_all_entries(self, order_by=None) -> dict:
        """
        Get all entries from the database, optionally ordered by a specific attribute.

        Parameters:
        - order_by (str): The attribute by which to order the entries (optional).

        Returns:
        dict: All entries from the database.
        """
        if order_by:
            sorted_entries = self.__sort_entries(self.data, [order_by])
            return sorted_entries
        else:
            return self.data
    

    def clear(self) -> None:
        """
        Clear all entries in the database.
        """
        self.data = {}
        self.__save_data()


    def __sort_entries(self, entries, sort_attrs):
        """
        Sort entries based on specified attributes.

        Parameters:
        - entries (dict): The entries to be sorted.
        - sort_attrs (list): The attributes by which to sort the entries.

        Returns:
        dict: Sorted entries.
        """
        return dict(sorted(entries.items(), key=lambda item: tuple(item[1].get(attr, '') for attr in sort_attrs)))

    
    def filter(self, key_filter, key_value):
        """
        Filter entries based on a specific key-value pair.

        Parameters:
        - key_filter (str): The key to filter by.
        - key_value: The value to filter for.

        Returns:
        dict: Filtered entries.
        """
        return {key: value for key, value in self.data.items() if value.get(key_filter) == key_value}


    def json2csv(self):
        """
        Convert JSON data to CSV and save to the specified CSV file.
        """
        with open(f'{self.name}.csv', 'w', newline='', encoding='utf-8') as csv_file:
            # Extract headers from the first entry in the data
            headers = self.__get_headers()

            # Create a CSV writer
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)

            # Write the header row
            csv_writer.writeheader()

            # Write each entry to the CSV file
            csv_writer.writerows(self.data.values())


    def __get_headers(self):
        """
        Get headers from the first entry in the data.

        Returns:
        list: List of headers.
        """
        first_entry = next(iter(self.data.values()), None)
        return list(first_entry.keys()) if first_entry else []


