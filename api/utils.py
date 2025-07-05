import os
from pathlib import Path

def get_safe_path(path_str):
    """
    Validate and return a safe path object.
    
    Args:
        path_str (str): The path string to validate
        
    Returns:
        Path or None: The validated Path object or None if invalid
    """
    try:
        # Create Path object
        path = Path(path_str)
        
        # Check if path exists and is a directory
        if not path.exists():
            return None
        
        return path
    except Exception:
        return None

def format_size(size_bytes):
    """
    Format file size in bytes to human-readable format.
    
    Args:
        size_bytes (int): File size in bytes
        
    Returns:
        str: Formatted file size
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024
        i += 1
    
    return f"{size_bytes:.2f} {size_names[i]}"

def get_file_icon(extension):
    """
    Get an appropriate icon character for a file based on its extension.
    
    Args:
        extension (str): File extension
        
    Returns:
        str: Icon character
    """
    extension = extension.lower() if extension else ""
    
    # Text and code files
    if extension in ['.txt', '.md', '.csv', '.json', '.xml']:
        return "📄"
    elif extension in ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp']:
        return "📝"
    
    # Document files
    elif extension in ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']:
        return "📊"
    
    # Image files
    elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']:
        return "🖼️"
    
    # Audio/video files
    elif extension in ['.mp3', '.wav', '.ogg', '.mp4', '.avi', '.mov']:
        return "🎵"
    
    # Archive files
    elif extension in ['.zip', '.rar', '.tar', '.gz', '.7z']:
        return "📦"
    
    # Default
    return "📄"
