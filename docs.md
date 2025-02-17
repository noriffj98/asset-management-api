# API Documentation

## Overview
This API allows you to interact with the Investment Management system. It provides endpoints to manage investment assets, retrieve asset data, and update records.

## Endpoints

### GET /assets

#### Description:
Retrieves a list of all investment assets in the system.

#### Request:
- **Method**: GET

#### Response:
- **Status Code**: 200 OK
- **Body**:
```json
[
    {
        "asset_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "asset_name": "Demo Asset",
        "manager_name": "David Suh",
        "description": "A demo asset.",
        "nav": 150.75,
        "creation_date": "2024-11-05",
        "performance": 12.5
    },
    {
        "asset_id": "216dae2a-3463-4728-9df7-b4aa2aece4e5",
        "asset_name": "Demo Asset 2",
        "manager_name": "Alice Wong",
        "description": "A demo asset.",
        "nav": 450000,
        "creation_date": "2020-01-01",
        "performance": 16.5
    }
]
```

### POST /assets

#### Description:
Creates a new investment asset.

#### Request:
- **Method**: POST
- **Body**:
```json
    {
        "asset_name": "Demo Asset",
        "manager_name": "David Suh",
        "description": "A demo asset.",
        "nav": 150.75,
        "creation_date": "2024-11-05",
        "performance": 12.5
    }
```

#### Response:
- **Status Code**: 201 Created
- **Body**:
```json
    {
        "asset_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "asset_name": "Demo Asset",
        "manager_name": "David Suh",
        "description": "A demo asset.",
        "nav": 150.75,
        "creation_date": "2024-11-05",
        "performance": 12.5
    }
```

### GET /assets/<asset_id>

#### Description:
Retrieves details of a specific asset.

#### Request:
- **Method**: GET

#### Response:
- **Status Code**: 200 OK
- **Body**:
```json
    {
        "asset_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "asset_name": "Demo Asset",
        "manager_name": "David Suh",
        "description": "A demo asset.",
        "nav": 150.75,
        "creation_date": "2024-11-05",
        "performance": 12.5
    }
```

### PUT /assets/<asset_id>/performance

#### Description:
Updates the performance of a specific asset.

#### Request:
- **Method**: PUT
- **Body**:
```json
  {
    "performance": 15.0
  }
```

#### Response:
- **Status Code**: 200 OK
- **Body**:
```json
    {
        "asset_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "asset_name": "Demo Asset",
        "manager_name": "David Suh",
        "description": "A demo asset.",
        "nav": 150.75,
        "creation_date": "2024-11-05",
        "performance": 15.0
    }
```

### DELETE /assets/<asset_id>

#### Description:
Deletes an investment asset.

#### Request:
- **Method**: DELETE

#### Response:
- **Status Code**: 204 No Content

# Database Schema

## Tables
1. Managers: Contains manager information.
2. Assets: Stores asset data.

## Relationships
- Each asset is managed by one manager.

## Managers Table
- `name`: Text, Name of the manager

## Assets Table
- `id`: UUID, Primary Key
- `name`: Text, Name of the asset
- `manager_name`: Text, Manager of the asset
- `description`: Text, Description of the asset
- `nav`: Real, Net Asset Value
- `created_at`: Text, Date of creation
- `performance`: Real, Performance percentage

# Notes

- **Error Handling**: All responses should include an appropriate status code and a meaningful message. Common status codes include:

  - `200 OK`: Request succeeded.
  - `201 Created`: Resource successfully created.
  - `204 No Content`: Resource successfully deleted.
  - `401 Unauthorized`: Invalid authentication credentials.
  - `404 Not Found`: Resource not found.
  - `500 Internal Server Error`: General server error.
