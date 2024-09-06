# RESTful CRUD Application with Flask

This project is a RESTful CRUD (Create, Read, Update, Delete) application built with Python and Flask. It provides a web-based interface and a backend service to manage transactions in a database. The application utilizes RESTful APIs to perform CRUD operations and manages routing between multiple HTML pages for different operations.

## Features

- **RESTful API**: All CRUD operations are implemented using REST principles with HTTP methods (`GET`, `POST`, etc.).
- **Create Operation**: Add a new transaction entry with date and amount details.
- **Read Operation**: View all existing transaction entries in a tabular format.
- **Update Operation**: Edit the details of an existing transaction entry.
- **Delete Operation**: Remove a transaction entry from the database.
- **Advanced Routing and Request Management**: Uses Flask's advanced routing features for efficient request handling and page navigation.
- **Multi-page Navigation**: Manages routing between multiple HTML pages to handle different operations and views.

## RESTful Endpoints

The following RESTful API endpoints are available:

- `GET /` - Retrieve all transaction entries.
- `POST /add` - Add a new transaction entry.
- `GET /edit/<transaction_id>` - Retrieve a specific transaction entry for editing.
- `POST /edit/<transaction_id>` - Update a specific transaction entry.
- `GET /delete/<transaction_id>` - Delete a specific transaction entry.

## Project Overview

The application is structured around three main web pages:

1. **Transaction Records**: This is the main page that displays all the recorded transactions in a table format. Users can add new transactions, edit existing ones, or delete any entry directly from this page.

2. **Add Transaction**: This page is used to add new transaction entries. Users can input the transaction date and amount, which is then stored in the database.

3. **Edit Transaction**: When users choose to edit an entry from the "Transaction Records" page, they are navigated to this page. It allows users to update the date and amount for the selected transaction entry.

### How It Works

- **Adding a Transaction**: On the "Transaction Records" page, click "Add Transaction" to navigate to the "Add Transaction" page. Enter the transaction date and amount, and submit the form to add a new entry to the database.
- **Viewing Transactions**: All transactions are listed on the "Transaction Records" page, displaying the date, amount, and available actions (Edit/Delete).
- **Editing a Transaction**: On the "Transaction Records" page, click "Edit" next to the desired transaction entry. This action takes you to the "Edit Transaction" page, where you can update the transaction details.
- **Deleting a Transaction**: Click "Delete" next to the transaction entry you wish to remove. The entry is immediately deleted from the database and the list is updated.


![image](https://github.com/user-attachments/assets/9072d1ba-3d85-46ba-8181-dae7db2ae547)
![image](https://github.com/user-attachments/assets/a14b089e-c2bf-45aa-9b6f-fc5b10b669b5)
