import os
from pathlib import Path
import stat

def scan_directory(directory_path, max_depth=3):
    """
    Scan a directory and build a hierarchical data structure suitable for D3.js visualization.
    
    Args:
        directory_path (str): Path to the directory to scan
        max_depth (int): Maximum depth to scan
        
    Returns:
        dict: Hierarchical data structure representing the directory
    """
    directory_path = Path(directory_path)
    
    def process_path(path, current_depth=0):
        """Process a single path and its children recursively."""
        # Stop if max depth is reached
        if current_depth > max_depth:
            return None
        
        path_name = path.name or str(path)
        
        # Handle file
        if path.is_file():
            try:
                size = path.stat().st_size
                modified_time = path.stat().st_mtime
                return {
                    "name": path_name,
                    "path": str(path),
                    "type": "file",
                    "size": size,
                    "modified": modified_time,
                    "extension": path.suffix.lower() if path.suffix else ""
                }
            except (FileNotFoundError, PermissionError):
                # Handle case where file might be inaccessible
                return {
                    "name": path_name,
                    "path": str(path),
                    "type": "file",
                    "error": "Access error"
                }
        
        # Handle directory
        elif path.is_dir():
            try:
                children = []
                
                # Get all children but skip hidden files/folders unless it's the root
                for child in sorted(path.iterdir()):
                    # Skip hidden files/folders (starting with .) except at root level
                    if current_depth > 0 and child.name.startswith('.'):
                        continue
                    
                    # Process the child path
                    child_node = process_path(child, current_depth + 1)
                    if child_node:
                        children.append(child_node)
                
                return {
                    "name": path_name,
                    "path": str(path),
                    "type": "folder",
                    "children": children
                }
            except (PermissionError, FileNotFoundError):
                # Handle case where directory might be inaccessible
                return {
                    "name": path_name,
                    "path": str(path),
                    "type": "folder",
                    "error": "Access error",
                    "children": []
                }
        
        # Skip other types of files (symlinks, etc.)
        return None
    
    # Start processing from the root directory
    result = process_path(directory_path)
    return result

def get_file_type_group(extension):
    """Categorize file by its extension for better visualization."""
    extension = extension.lower()
    
    code_extensions = {'.py', '.js', '.html', '.css', '.java', '.c', '.cpp', 
                      '.h', '.cs', '.php', '.rb', '.go', '.ts', '.swift'}
    
    document_extensions = {'.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', 
                          '.ppt', '.pptx', '.md', '.csv', '.json', '.xml'}
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', 
                       '.tiff', '.ico', '.webp'}
    
    if extension in code_extensions:
        return 'code'
    elif extension in document_extensions:
        return 'document'
    elif extension in image_extensions:
        return 'image'
    else:
        return 'other'
