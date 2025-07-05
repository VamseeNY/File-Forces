# Installation Guide for Directory Structure Visualizer

This document provides detailed installation instructions for the Directory Structure Visualizer application.

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.7 or higher
- **Disk Space**: Approximately 100MB for the application and dependencies
- **Memory**: Minimum 2GB RAM recommended

## Installation Methods

### Method 1: Using pip (Recommended)

1. **Ensure Python is installed**

   Check your Python version:
   ```bash
   python --version
   ```
   If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Streamlit**

   ```bash
   pip install streamlit
   ```

3. **Download the application**

   Clone the repository:
   ```bash
   git clone https://github.com/yourusername/directory-visualizer.git
   cd directory-visualizer
   ```

   Or download and extract the ZIP file from the repository.

4. **Run the application**

   ```bash
   streamlit run app.py
   ```

### Method 2: Using Conda

1. **Install Miniconda or Anaconda**

   Download from [conda.io](https://docs.conda.io/en/latest/miniconda.html) or [anaconda.com](https://www.anaconda.com/products/individual).

2. **Create a conda environment**

   ```bash
   conda create -n directory-viz python=3.9
   conda activate directory-viz
   ```

3. **Install Streamlit**

   ```bash
   pip install streamlit
   ```

4. **Download and run the application**

   ```bash
   git clone https://github.com/yourusername/directory-visualizer.git
   cd directory-visualizer
   streamlit run app.py
   ```

### Method 3: Docker Installation

1. **Install Docker**

   Follow the instructions at [docker.com](https://docs.docker.com/get-docker/).

2. **Build the Docker image**

   Create a `Dockerfile` in your project directory with:

   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY . .

   RUN pip install streamlit

   EXPOSE 8501

   ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

3. **Build and run the container**

   ```bash
   docker build -t directory-visualizer .
   docker run -p 8501:8501 directory-visualizer
   ```

4. **Access the application**

   Open your browser and go to `http://localhost:8501`

## Troubleshooting

### Common Issues

1. **Missing dependencies**

   If you encounter errors about missing packages, try installing them:
   
   ```bash
   pip install streamlit
   ```

2. **Port already in use**

   If port 8501 is already in use, you can specify a different port:
   
   ```bash
   streamlit run app.py -- --server.port 8502
   ```

3. **Permission errors on directory scanning**

   Ensure you have read permissions for the directories you want to scan.

### Getting Help

If you encounter issues not covered here:

1. Check the [GitHub repository issues](https://github.com/yourusername/directory-visualizer/issues)
2. Open a new issue with detailed information about your problem

## Updating the Application

To update to the latest version:

```bash
cd directory-visualizer
git pull
```

## Uninstallation

To uninstall:

1. **Remove the application directory**

   ```bash
   rm -rf directory-visualizer
   ```

2. **Optionally, uninstall Streamlit**

   ```bash
   pip uninstall streamlit
   ```

3. **If using conda, remove the environment**

   ```bash
   conda deactivate
   conda remove --name directory-viz --all
   ```