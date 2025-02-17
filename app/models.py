import uuid

class InvestmentAsset:
    def __init__(self, asset_id, asset_name, manager_name,
                 description, nav, creation_date, performance):
        self.asset_id = asset_id  # Unique identifier for the asset
        self.asset_name = asset_name  # Name of the asset
        self.manager_name = manager_name  # Manager overseeing the asset
        self.description = description  # Description of the asset
        self.nav = nav  # Net Asset Value (NAV)
        self.creation_date = creation_date  # Date of creation
        self.performance = performance  # Performance percentage

    def to_dict(self):
        return {
            "asset_id": self.asset_id,
            "asset_name": self.asset_name,
            "manager_name": self.manager_name,
            "description": self.description,
            "nav": self.nav,
            "creation_date": self.creation_date,
            "performance": self.performance
        }

def generate_asset_id():
    return str(uuid.uuid4())
