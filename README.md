# Directory Structure Visualizer

A Streamlit web application that visualizes folder directory structures as interactive D3.js force-directed graphs.

![image](https://github.com/user-attachments/assets/166203f8-f722-479c-b2a2-5c73565d7882)



## Features

- **Interactive Visualization**: View your directory structure as an interactive force-directed graph
- **Dark Mode Interface**: Clean, modern dark theme for comfortable viewing
- **File Type Categorization**: Files are color-coded by type for easy identification
- **Detailed Information**: Hover over nodes to see detailed file/folder information
- **Customizable Depth**: Control how deep the directory scanning goes
- **Connection Highlighting**: Click on nodes to highlight their connections
- **Progress Indicators**: Visual feedback during directory scanning and processing


![image](https://github.com/user-attachments/assets/08b28439-2347-42d1-8b3d-ba3be4c7c43c)

## Installation

### Prerequisites

- Python 3.7 or higher
- Git (for cloning the repository)

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/directory-visualizer.git
   cd directory-visualizer
   ```

2. **Set up a virtual environment (recommended)**

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install directly:

   ```bash
   pip install streamlit
   ```

4. **Run the application**

   ```bash
   streamlit run app.py
   ```

5. **Open in your browser**

   The application should automatically open in your default web browser. If not, navigate to:
   
   ```
   http://localhost:8501
   ```


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
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── app.py                # Main Streamlit application
├── directory_scanner.py  # Directory scanning functionality
├── graph_visualization.py # D3.js visualization code
├── utils.py              # Utility functions
└── README.md             # This documentation
```


### Extending Functionality

To add more features:

1. **File type categorization**: Extend the `get_file_type_group` function in `directory_scanner.py`
2. **Additional statistics**: Modify the `calculate_directory_stats` function in `app.py`
3. **UI improvements**: Add more Streamlit components in `app.py`

## License

This project is open-source and available under the MIT License.
