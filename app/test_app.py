import unittest
import json
from app import create_app
from .models import InvestmentAsset

class TestInvestmentAsset(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.client.testing = True

        self.sample_asset = InvestmentAsset(
            asset_id="123e4567-e89b-12d3-a456-426614174000",
            asset_name="Sample Asset",
            manager_name="Manager 1",
            description="A sample investment asset.",
            nav=100.0,
            creation_date="2024-01-01",
            performance=10.0
        )
        self.sample_asset_dict = self.sample_asset.to_dict()

        self.json_data = '''
        {
            "123e4567-e89b-12d3-a456-426614174000": {
                "asset_id": "123e4567-e89b-12d3-a456-426614174000",
                "asset_name": "Sample Asset",
                "manager_name": "Manager 1",
                "description": "A sample investment asset.",
                "nav": 100.0,
                "creation_date": "2024-01-01",
                "performance": 10.0
            },
            "223e4567-e89b-12d3-a456-426614174001": {
                "asset_id": "223e4567-e89b-12d3-a456-426614174001",
                "asset_name": "Sample Asset 2",
                "manager_name": "Manager 2",
                "description": "Another sample asset.",
                "nav": 200.0,
                "creation_date": "2024-02-01",
                "performance": 12.0
            }
        }
        '''

    def test_initialization(self):
        self.assertEqual(self.sample_asset.asset_id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.sample_asset.asset_name, "Sample Asset")
        self.assertEqual(self.sample_asset.manager_name, "Manager 1")
        self.assertEqual(self.sample_asset.description, "A sample investment asset.")
        self.assertEqual(self.sample_asset.nav, 100.0)
        self.assertEqual(self.sample_asset.creation_date, "2024-01-01")
        self.assertEqual(self.sample_asset.performance, 10.0)

    def test_to_dict(self):
        expected_dict = {
            "asset_id": "123e4567-e89b-12d3-a456-426614174000",
            "asset_name": "Sample Asset",
            "manager_name": "Manager 1",
            "description": "A sample investment asset.",
            "nav": 100.0,
            "creation_date": "2024-01-01",
            "performance": 10.0
        }
        self.assertEqual(self.sample_asset.to_dict(), expected_dict)

    def test_get_all_assets(self):
        response = self.client.get('/assets')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_asset(self):
        response = self.client.post('/assets', data=json.dumps(self.sample_asset_dict), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['asset_name'], self.sample_asset_dict['asset_name'])
        self.assertIn('asset_id', data)

    def test_create_asset_missing_field(self):
        incomplete_data = self.sample_asset_dict.copy()
        incomplete_data.pop("asset_name")  # Remove a required field
        response = self.client.post('/assets', data=json.dumps(incomplete_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing field", response.get_json()["message"])

    def test_get_asset_details(self):
        create_response = self.client.post('/assets', data=json.dumps(self.sample_asset_dict), content_type='application/json')
        asset_id = create_response.get_json()["asset_id"]
        response = self.client.get(f'/assets/{asset_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["asset_id"], asset_id)

    def test_get_asset_details_not_found(self):
        response = self.client.get('/assets/nonexistent_id')
        self.assertEqual(response.status_code, 404)

    def test_update_asset_performance(self):
        create_response = self.client.post('/assets', data=json.dumps(self.sample_asset_dict), content_type='application/json')
        asset_id = create_response.get_json()["asset_id"]
        update_data = {"performance": 15.5}
        response = self.client.put(f'/assets/{asset_id}/performance', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["performance"], 15.5)

    def test_update_asset_performance_invalid(self):
        create_response = self.client.post('/assets', data=json.dumps(self.sample_asset_dict), content_type='application/json')
        asset_id = create_response.get_json()["asset_id"]
        update_data = {"performance": "invalid"}
        response = self.client.put(f'/assets/{asset_id}/performance', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_asset(self):
        create_response = self.client.post('/assets', data=json.dumps(self.sample_asset_dict), content_type='application/json')
        asset_id = create_response.get_json()["asset_id"]
        response = self.client.delete(f'/assets/{asset_id}')
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f'/assets/{asset_id}')
        self.assertEqual(response.status_code, 404)

    def test_parse_json(self):
        data = json.loads(self.json_data)
        self.assertEqual(len(data), 2)
        assets = list(data.values())
        self.assertEqual(assets[0]['asset_name'], "Sample Asset")
        self.assertEqual(assets[1]['manager_name'], "Manager 2")

    def test_insert_managers(self):
        managers = [
            {"manager_name": "Manager 1"},
            {"manager_name": "Manager 2"}
        ]
        insert_statements = []
        for manager in managers:
            stmt = f"INSERT INTO Managers (name) VALUES ('{manager['manager_name']}')"
            insert_statements.append(stmt)
        self.assertEqual(len(insert_statements), 2)
        self.assertEqual(insert_statements[0], "INSERT INTO Managers (name) VALUES ('Manager 1')")
        self.assertEqual(insert_statements[1], "INSERT INTO Managers (name) VALUES ('Manager 2')")

    def test_insert_assets(self):
        assets = json.loads(self.json_data)
        insert_statements = []
        for asset in assets.values():
            stmt = f"""
            INSERT INTO Assets (id, name, manager_name, description, nav, created_at, performance)
            VALUES ('{asset['asset_id']}', '{asset['asset_name']}', '{asset['manager_name']}',
                    '{asset['description']}', {asset['nav']}, '{asset['creation_date']}', {asset['performance']})
            """
            insert_statements.append(stmt)
        self.assertEqual(len(insert_statements), 2)
        self.assertIn("INSERT INTO Assets", insert_statements[0])
        self.assertIn("Sample Asset 2", insert_statements[1])

if __name__ == "__main__":
    unittest.main()
