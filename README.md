# Directory Structure Visualizer

A Streamlit web application that visualizes folder directory structures as interactive D3.js force-directed graphs.

![image](https://github.com/user-attachments/assets/2af61d85-3693-4397-873f-4ba8756b8b2d)



## Features

- **Interactive Visualization**: View your directory structure as an interactive force-directed graph
- **File Type Categorization**: Files are color-coded by type for easy identification
- **Detailed Information**: Hover over nodes to see detailed file/folder information
- **Customizable Depth**: Control how deep the directory scanning goes
- **Progress Indicators**: Visual feedback during directory scanning and processing


![image](https://github.com/user-attachments/assets/b684b343-52e4-4af0-8266-6ab37c423070)


## Installation

### Prerequisites

- Python 3.7 or higher
- Git (for cloning the repository)

### Quick Start
## Installation

This project consists of two parts: a Flask-based backend (`api/`) and a Next.js-based frontend (`frontend/`).

---

### Backend (Flask API)

1. Navigate to the backend directory:

   ```bash
   cd api
   ```

2. Create a virtual environment and activate it:

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required Python dependencies:

   ```bash
   pip install flask flask-cors
   ```

4. Start the Flask development server:

   ```bash
   python api.py
   ```

---

### Frontend (Next.js App)

1. Open a new terminal and navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

3. Start the Next.js development server:

   ```bash
   npm run dev
   ```

4. Open your browser and navigate to:

   ```
   http://localhost:3000
   ```

---

### Notes

- Make sure the backend is running before accessing the frontend to ensure API requests succeed.
- Adjust CORS settings in `api.py` if deploying on a different domain.
- You can modify the directory scanning logic in `api/directory_scanner.py` and the graph rendering in `frontend/src/app/components/ForceGraph.tsx`.


## Usage

1. **Select a directory to visualize**
   - Choose between entering a custom directory path or using the current working directory
   - Adjust the maximum directory scanning depth using the slider

2. **Click "Visualize Directory"**
   - Wait for the directory to be scanned and processed
   - The visualization will appear in the main area

3. **Interact with the visualization**
   - Drag nodes to rearrange the graph
   - Hover over nodes to see file/folder details
   - Click on nodes to highlight connections
   - Use the scroll wheel to zoom in/out
   - Drag the background to pan around
   - Adjust the link strength using the slider
   - Click "Reset View" to reset the visualization

## File Structure

```
directory-visualizer/
├── api/                     # Flask backend
│   ├── __pycache__/
│   ├── api.py               # Flask app and API endpoints
│   ├── directory_scanner.py # Recursive directory scanning
│   └── utils.py             # Helper functions
│
├── frontend/                # Next.js frontend
│   ├── .next/               # Build output
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   └── app/
│   │       ├── favicon.ico
│   │       ├── globals.css
│   │       ├── layout.tsx
│   │       ├── page.tsx            # Homepage logic
│   │       └── components/
│   │           └── ForceGraph.tsx  # D3 visualization
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.ts
│   └── README.md
│
├── .gitignore
├── INSTALL.md
├── uv.lock

```
### Future work
- GPU Accelerated visualizations using WebGL

### Extending Functionality

To add more features:

1. **File type categorization**: Extend the `get_file_type_group` function in `directory_scanner.py`
2. **Additional statistics**: Modify the `calculate_directory_stats` function in `app.py`
3. **UI improvements**: Add more Streamlit components in `app.py`

## License

This project is open-source and available under the MIT License.
