# Investment Management System

## Overview
This repository contains a generic implementation of an Investment Management System. The goal is to demonstrate a RESTful API for managing investment assets, including creating, updating, and deleting records, along with data persistence and testing.

## Task Breakdown

### Data Model Design
- **File**: `models.py`
- **Description**: Defines the `Asset` class representing an investment asset with properties like asset ID, name, manager, description, NAV, creation date, and performance. It includes serialization methods and a unique ID generator.

### REST API Development
- **Files**: `routes.py`, `__init__.py`
- **Description**: Implements a Flask-based RESTful API with endpoints to:
  - Retrieve all assets
  - Create a new asset
  - Retrieve details of a specific asset by its ID
  - Update an asset’s performance
  - Delete an asset

### Data Persistence
- **File**: `routes.py`
- **Description**: Uses a JSON file (`assets.json`) for data persistence, with functions to load and save asset data.

### SQL Database Schema
- **File**: `initial.sql`
- **Description**: Contains SQL statements to set up the database schema for storing investment asset data.

### SQL Data Migration
- **File**: `migration.sql`
- **Description**: Provides SQL scripts to migrate data from the JSON file to the SQL database.

### Error Handling and Testing
- **Files**: `errors.py`, `test_app.py`
- **Description**: Implements error handling for robust API responses and includes unit tests for API endpoints and database operations.

### Documentation
- **File**: `docs.md`
- **Description**: Provides API documentation, including sample requests, responses, and details of the SQL schema.

## How to Run the Project

1. **Run the Flask Application**:
   - Use the `run.py` file to start the app:
     ```bash
     python run.py
     ```

2. **Set Up the Database**:
   - Run `initial.sql` to create the database schema.
   - Execute `migration.sql` to migrate data from `assets.json` to the SQL database (update the file path if needed).

3. **Run Tests**:
   - Execute:
     ```bash
     python -m unittest test_app.py
     ```

## Contact
For questions or further clarifications, please submit an issue.

---

Thank you for reviewing this project!
