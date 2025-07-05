from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from directory_scanner import scan_directory
from utils import get_safe_path

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the API endpoint for scanning a directory
@app.route('/api/scan', methods=['GET'])
def scan_directory_endpoint():
    """
    Scans a directory and returns its structure as JSON.
    Accepts 'path' and 'depth' as query parameters.
    """
    # Get directory path from query parameters
    directory_path = request.args.get('path', '')
    
    # Get depth limit from query parameters, default to 3
    try:
        depth_limit = int(request.args.get('depth', 3))
    except ValueError:
        return jsonify({"error": "Invalid depth parameter. Must be an integer."}), 400

    # Use current working directory if no path is provided
    if not directory_path:
        directory_path = os.getcwd()

    # Validate the path
    safe_path = get_safe_path(directory_path)
    if not safe_path:
        return jsonify({"error": "Invalid or unsafe directory path"}), 400

    try:
        # Scan the directory
        dir_data = scan_directory(safe_path, depth_limit)
        
        # Return the directory data as JSON
        return jsonify(dir_data)
        
    except Exception as e:
        return jsonify({"error": f"Error scanning directory: {str(e)}"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001) # Using a different port to avoid conflict with React dev server
