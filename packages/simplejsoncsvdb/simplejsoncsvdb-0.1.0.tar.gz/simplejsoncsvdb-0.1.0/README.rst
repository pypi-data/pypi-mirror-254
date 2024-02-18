Welcome to simplejsoncsvdb Documentation
=======================================

Overview
--------

`simplejsoncsvdb` is a lightweight Python package providing a `DataBase` class for key-value storage. This documentation aims to help users understand how to use the package effectively.

Installation
------------

You can install the package using `pip`:

.. code-block:: bash

    pip install simplejsoncsvdb

Usage
-----

For usage instructions and examples, please refer to the [simplejsoncsvdb README](https://github.com/EmilTsaturyan/json-db).

Examples
========

Example 1: Creating a Database Instance and Adding an Entry
----------------------------------------------------------

.. code-block:: python

    from PyKeyValueStore import DataBase

    # Create a database instance
    my_database = DataBase("example_database")

    # Add an entry to the database
    my_database.add_entry("key1", {"name": "John", "age": 30, "city": "New York"})

Example 2: Retrieving an Entry from the Database
------------------------------------------------

.. code-block:: python

    # Retrieve an entry from the database
    entry = my_database.get_entry("key1")
    print(entry)

Example 3: Updating an Entry in the Database
--------------------------------------------

.. code-block:: python

    # Update an entry in the database
    my_database.update_entry("key1", {"name": "John Doe", "age": 31, "city": "San Francisco"})

Example 4: Deleting an Entry from the Database
----------------------------------------------

.. code-block:: python

    # Delete an entry from the database
    my_database.del_entry("key1")

Example 5: Converting JSON Data to CSV
---------------------------------------

.. code-block:: python

    # Convert JSON data to CSV
    my_database.json2csv()

Example 6: Clearing All Entries in the Database
-----------------------------------------------

.. code-block:: python

    # Clear all entries in the database
    my_database.clear()

Example 7: Filtering Entries Based on a Specific Key-Value Pair
----------------------------------------------------------------

Suppose you want to filter entries based on a specific key-value pair. Here's how you can achieve this using the `get_all_entries` method with a filter:

.. code-block:: python

    # Filter entries where 'age' is 30
    filtered_entries = my_database.filter('age', 30)
    print(filtered_entries)

Example 8: Retrieving and Sorting All Entries Based on an Attribute
------------------------------------------------------------------

Suppose you want to retrieve all entries from the database and order them by the 'name' attribute. Here's how you can use the `get_all_entries` method with sorting:

.. code-block:: python

    # Retrieve all entries sorted by the 'name' attribute
    sorted_entries = my_database.get_all_entries(order_by='name')
    print(sorted_entries)

    