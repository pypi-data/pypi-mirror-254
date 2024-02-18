from functools import lru_cache
import hashlib
import io

def get_hash(filebytes : bytes):
    """
    Generate the SHA-256 hash of the input file bytes.

    Args:
        filebytes (bytes): The input file bytes or io.BytesIO object.

    Returns:
        str: The SHA-256 hash of the input file bytes as a hexadecimal string.
    """
    if isinstance(filebytes, io.BytesIO):
        filebytes = filebytes.getvalue()
    
    return hashlib.sha256(filebytes).hexdigest()

@lru_cache(maxsize=8)
def check_hash(content : bytes, hash : str):
    """
    Check if the hash of the given content matches the provided hash.

    Parameters:
    content (bytes): The content to calculate the hash for.
    hash (str): The hash to compare against.

    Returns:
    bool: True if the hash matches, False otherwise.
    """
    return get_hash(content) == hash