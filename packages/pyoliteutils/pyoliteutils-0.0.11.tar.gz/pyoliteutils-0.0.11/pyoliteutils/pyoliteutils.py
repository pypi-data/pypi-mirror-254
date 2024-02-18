from js import fetch
from os.path import exists
 
async def load_file_into_in_mem_filesystem(url, fn=None):
    """Load a file from a URL into an in-memory filesystem."""
     
    # Create a filename if required
    fn = fn if fn is not None else url.split("/")[-1]
     
    # Fetch file from URL
    res = await fetch(url)
     
    # Buffer it
    buffer = await res.arrayBuffer()
     
    # Write file to in-memory file system
    open(fn, "wb").write(bytes(buffer.valueOf().to_py()))
 
    return fn

async def get_file_from_url(url, fn=None, force=False):
    """Load a file from a URL into an in-memory filesystem cacheing so we don't overload the server."""
     
    # Create a filename if required
    fn = fn if fn is not None else url.split("/")[-1]
    
    if not exists(fn) or force:
        # Fetch file from URL
        res = await fetch(url)
        
        # Buffer it
        buffer = await res.arrayBuffer()
        
        # Write file to in-memory file system
        open(fn, "wb").write(bytes(buffer.valueOf().to_py()))
 
    return fn