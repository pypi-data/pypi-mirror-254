import datetime
from functools import lru_cache
import shutil
from sprinko.base.env import CacheEntry, caching_dir, caching
from sprinko.extra.git import (
    download_github_raw_content, extract_meta_from_gitraw, git_last_commit_sha
)
from sprinko.extra.log import logger
import os
from sprinko.extra.hashing import check_hash, get_hash
from sprinko.extra.zip import make_zip

def prune_cache():
    existing_checksums = [v["checksum"] for v in caching.values()]
    existing_files = os.listdir(caching_dir)

    obsolete_items = set(existing_files) - set(existing_checksums)
    
    for x in obsolete_items:
        logger.debug(f"removing {x}")
        os.remove(os.path.join(caching_dir, x))
        

def check_last_pull(path : str):
    """
    Check if the path is in the cache and determine if the cache needs to be updated.

    Args:
        path (str): The path to check in the cache.

    Returns:
        bool: True if the cache needs to be updated, False otherwise.
    """
    cache_entry = caching.get(path, None)
    
    if cache_entry is None:
        return True
    
    cache_entry : CacheEntry
    
    # if updatable set to None and file exists
    if (
        (updatableInterval := cache_entry.get("updatableInterval", None)) is None 
        and (checksum :=cache_entry.get("checksum", None)) is not None
    ):
        if os.path.exists(os.path.join(caching_dir, checksum)):
            logger.debug(f"permanent cache exists for {path}")
            return False
    
    # Determine if the cache needs to be updated
    last_pulled = cache_entry.get('lastPulled', None)
    if last_pulled is None:
        return True
    
    time_since_last_pull = datetime.datetime.now() - datetime.datetime.fromisoformat(last_pulled)
    return time_since_last_pull.total_seconds() > updatableInterval

def last_commited_sha(path : str):
    """
    Get the last committed SHA for the specified file path.

    Args:
        path (str): The file path for which to retrieve the last commit SHA.

    Returns:
        str: The last commit SHA for the specified file path.
    """
    pathmeta = extract_meta_from_gitraw(path)

    last_commit_sha : str = git_last_commit_sha(
        id = pathmeta["repo"],
        filename = pathmeta["filedir"] + "/" + pathmeta["filename"]
    )
    
    return last_commit_sha

def check_last_commit(path : str):
    """
    Check if the last commit for the given path has changed since the last check.
    
    Args:
        path (str): The path to the file or directory to be checked.
        
    Returns:
        bool: True if the last commit has changed, False otherwise.
    """
    cache_entry = caching.get(path, None)

    if cache_entry is None:
        return True

    last_committed = cache_entry.get('lastCommitted', None)
    if last_committed is None:
        return True

    last_commit_sha : str = last_commited_sha(path)
    
    return last_commit_sha != last_committed

def retrieve_cache_file(path : str):
    """
    Retrieve the cache file for the given path.

    Args:
        path (str): The path of the file to retrieve from the cache.

    Returns:
        bytes: The content of the file retrieved from the cache.
    
    Raises:
        Exception: If the file checksum does not match.
    """
    cache_entry = caching.get(path)
    checksum = cache_entry.get("checksum")
    with open(os.path.join(caching_dir, checksum), 'rb') as f:
        bytes = f.read()
        if not check_hash(bytes, checksum):
            raise Exception("File checksum mismatch")
        
        return bytes        
   
ONE_DAY = 24 * 60 * 60

def get_local_cache(
    path: str, updateCheckInterval: int = None, force : bool = False
):
    """
    Retrieves or updates the local cache for the given path.

    Args:
        path (str): The path to the cache.
        updateCheckInterval (int, optional): The interval for update checking.
        force (bool, optional): Whether to force update the cache.

    Returns:
        The retrieved or updated cache file.
    """
    path = os.path.abspath(path)
    
    # check need update
    if not force:
        needs_update = check_last_pull(path)
    else:
        logger.debug(f"force update for {path}")
        needs_update = True

    if not needs_update:
        logger.debug(f"cache for {path} is up to date")
        return retrieve_cache_file(path)

    path = os.path.abspath(path)
        
    target_is_folder = False
    # local file transfer
    if os.path.isdir(path) and os.path.exists(os.path.join(path, "bottle.zip")):
        path = os.path.join(path, "bottle.zip")
        pathbytes = open(path, 'rb').read()
    elif os.path.isdir(path):
        target_is_folder = True
        pathbytes = make_zip(path)
    else:
        with open(path, 'rb') as f:
            pathbytes = f.read()
    pathchecksum = get_hash(pathbytes)
    
    if target_is_folder:
        with open(os.path.join(caching_dir, pathchecksum), 'wb') as f:
            f.write(pathbytes.getvalue())
    else:
        shutil.copyfile(path, os.path.join(caching_dir, pathchecksum))
    
    
    entry = CacheEntry(
        checksum=pathchecksum,
        type="local",
        updatableInterval=updateCheckInterval,
        lastPulled=datetime.datetime.now().isoformat() if updateCheckInterval else None,
    )
    
    entry = {k : v for k, v in entry.items() if v is not None}
    caching[path] = entry
        
    return retrieve_cache_file(path)

def get_git_cache(path: str, updateCheckInterval: int = None, force : bool = False):
    """
    Function to get the cached content from the Git repository or retrieve the cache file if up to date.
    
    Args:
        path (str): The file path to check and retrieve from the cache.
        updateCheckInterval (int, optional): The interval for checking updates in seconds. Defaults to None.
        force (bool, optional): Flag to force update the cache. Defaults to False.
    
    Returns:
        bytes: The content of the cached file.
    """
    # Check if the file needs to be updated
    lastCommit = None
    
    if not force:
        needs_update = check_last_pull(path)
    else:
        logger.debug(f"force update for {path}")
        needs_update = True
    
    if not needs_update:
        logger.debug(f"cache for {path} is up to date")
        return retrieve_cache_file(path)
    
    lastCommit= check_last_commit(path)
    
    if not lastCommit:
        return retrieve_cache_file(path)
    
    # Fetch the file from Git repository
    content = download_github_raw_content(path)
    checksum = get_hash(content)
    # Save the content to a file in the caching directory
    cached_file_path = os.path.join(caching_dir, checksum)
    with open(cached_file_path, 'wb') as f:
        f.write(content)

    res = CacheEntry(
        checksum=checksum,
        type="gitraw",
        updatableInterval=updateCheckInterval,
        lastPulled=datetime.datetime.now().isoformat(),
        lastCommitted=last_commited_sha(path)
    )

    res = {k : v for k, v in res.items() if v is not None}
    
    caching[path] = res
    
    return retrieve_cache_file(path)
            
@lru_cache(maxsize=32)
def is_cached(path : str, checkExpired : bool = False):
    """
    check the specified path is cached
    """
    if path not in caching:
        return False
    
    if not os.path.exists(os.path.join(caching_dir, caching[path]["checksum"])):
        return False
    
    if (not checkExpired or caching[path]["updatableInterval"] is None) and caching[path]["lastPulled"] is not None:
        return True
    else:
        return False
    
    