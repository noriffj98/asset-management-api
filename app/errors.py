from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def handle_invalid_data(error):
        response = jsonify({"error": "Invalid data", "message": error.description or "The input data is invalid."})
        response.status_code = 400
        return response

    @app.errorhandler(404)
    def handle_not_found(error):
        response = jsonify({"error": "Not found", "message": error.description or "The requested resource was not found."})
        response.status_code = 404
        return response

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."})
        response.status_code = 500
        return response
