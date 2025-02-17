from flask import request, jsonify, abort
from .models import InvestmentAsset, generate_asset_id
import json
import os

# Using a generic JSON file name for data persistence.
ASSET_FILE = 'assets.json'

def load_assets():
    if os.path.exists(ASSET_FILE):
        try:
            with open(ASSET_FILE, 'r') as file:
                data = json.load(file)
                return {k: InvestmentAsset(**v) for k, v in data.items()}
        except (json.JSONDecodeError, TypeError, ValueError):
            abort(500, "Error loading asset data.")
    return {}

assets = load_assets()

def save_assets():
    with open(ASSET_FILE, 'w') as file:
        json.dump({asset_id: asset.to_dict() for asset_id, asset in assets.items()}, file, indent=4)

def setup_routes(app):
    @app.route('/assets', methods=['GET'])
    def get_assets():
        return jsonify([asset.to_dict() for asset in assets.values()]), 200

    @app.route('/assets', methods=['POST'])
    def create_asset():
        data = request.get_json()
        try:
            asset_id = generate_asset_id()
            asset = InvestmentAsset(
                asset_id=asset_id,
                asset_name=data['asset_name'],
                manager_name=data['manager_name'],
                description=data['description'],
                nav=float(data['nav']),
                creation_date=data['creation_date'],
                performance=float(data['performance'])
            )
            assets[asset.asset_id] = asset
            save_assets()
            return jsonify(asset.to_dict()), 201
        except KeyError as e:
            abort(400, f"Missing field: {e.args[0]}")
        except ValueError:
            abort(400, "Invalid data type provided.")

    @app.route('/assets/<asset_id>', methods=['GET'])
    def get_asset_details(asset_id):
        asset = assets.get(asset_id)
        if not asset:
            abort(404, "Asset not found.")
        return jsonify(asset.to_dict()), 200

    @app.route('/assets/<asset_id>/performance', methods=['PUT'])
    def update_asset_performance(asset_id):
        asset = assets.get(asset_id)
        if asset:
            data = request.get_json()
            try:
                asset.performance = float(data['performance'])
                save_assets()
                return jsonify(asset.to_dict()), 200
            except KeyError:
                abort(400, "Missing or invalid performance data.")
            except ValueError:
                abort(400, "Performance data must be a valid number.")
        else:
            abort(404, "Asset not found.")

    @app.route('/assets/<asset_id>', methods=['DELETE'])
    def delete_asset(asset_id):
        if asset_id in assets:
            del assets[asset_id]
            save_assets()
            return '', 204
        else:
            abort(404, "Asset not found")
