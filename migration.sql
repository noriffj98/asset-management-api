-- migration.sql
-- This script migrates data from a JSON data source (e.g., assets.json) into the SQL database.

-- Load JSON data from the file into a variable
DECLARE @json_data NVARCHAR(MAX);

SELECT @json_data = BulkColumn
FROM OPENROWSET(
    BULK 'G:\My Drive\your_path\assets.json', -- Adjust the path to your JSON file
    SINGLE_CLOB
) AS datasource;

-- Insert unique manager names into the Managers table
INSERT INTO Managers (name)
SELECT DISTINCT JSON_VALUE(asset.value, '$.manager_name') AS manager_name
FROM OPENJSON(@json_data) AS asset
WHERE JSON_VALUE(asset.value, '$.manager_name') IS NOT NULL
  AND JSON_VALUE(asset.value, '$.manager_name') NOT IN (SELECT name FROM Managers);

-- Insert data into the Assets table
INSERT INTO Assets (id, name, manager_name, description, nav, created_at, performance)
SELECT
    JSON_VALUE(asset.value, '$.asset_id') AS id,
    JSON_VALUE(asset.value, '$.asset_name') AS name,
    JSON_VALUE(asset.value, '$.manager_name') AS manager_name,
    JSON_VALUE(asset.value, '$.description') AS description,
    CAST(JSON_VALUE(asset.value, '$.nav') AS REAL) AS nav,
    JSON_VALUE(asset.value, '$.creation_date') AS created_at,
    CAST(JSON_VALUE(asset.value, '$.performance') AS REAL) AS performance
FROM OPENJSON(@json_data) AS asset;

-- View the migrated data
SELECT * FROM Managers;
SELECT * FROM Assets;
