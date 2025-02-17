-- initial.sql
-- This script sets up the database schema for the Generic Investment Management System.

-- Drop tables if they exist (for reinitialization purposes)
DROP TABLE IF EXISTS Assets;
DROP TABLE IF EXISTS Managers;

-- Create Managers table
CREATE TABLE Managers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Create Assets table
CREATE TABLE Assets (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    manager_name TEXT NOT NULL,
    description TEXT,
    nav REAL NOT NULL,
    created_at DATE NOT NULL,
    performance REAL NOT NULL,
    FOREIGN KEY (manager_name) REFERENCES Managers(name)
);
