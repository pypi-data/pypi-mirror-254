from datetime import datetime
from functools import cache, lru_cache
from typing import TypedDict
import requests
import parse
from ..extra.dictionary import ERROR, getDeep
from ..extra.log import logger

baseurl= "https://raw.githubusercontent.com/{url}"

class GitMeta(TypedDict):
    branch : str
    filename : str
    filedir : str
    repo : str
    
_gitraw_parse = "{repo}/main/{filedir}/{filename}"

@cache
def extract_meta_from_gitraw(url : str, baseUrl = _gitraw_parse) -> GitMeta:
    """
    This function extracts metadata from a gitraw URL.

    Args:
        url (str): The gitraw URL to extract metadata from.
        baseUrl: The base URL for parsing the gitraw URL (default is _gitraw_parse).
    
    Returns:
        GitMeta: The extracted Git metadata.
    """
    parsed = parse.parse(baseUrl, url)
    return GitMeta(
        repo = parsed["repo"],
        branch = _gitraw_parse.split("/")[1],
        filename = parsed["filename"],
        filedir = parsed["filedir"]
    )
    
@cache
def gitraw_strip_filename(url : str):
    """
    Decorator that caches the result of the function based on its arguments.
    
    Parameters:
    url (str): The URL from which to extract metadata.
    
    Returns:
    str: The concatenated repo, branch, and filedir from the extracted metadata.
    """
    meta = extract_meta_from_gitraw(url)
    return meta["repo"] + "/" + meta["branch"] + "/" + meta["filedir"]

@cache
def gitraw_strip_filepath(url : str):
    meta = extract_meta_from_gitraw(url)
    return meta["repo"] + "/" + meta["branch"]
    
@cache
def git_has_file(url : str):
    url = baseurl.format(url=url)
    res = requests.head(url)
    if res.status_code == 404:
        return False
    return True
    
def download_github_raw_content(url : str):
    """
    Downloads the raw content from the given GitHub URL.

    Args:
        url (str): The URL of the content to be downloaded.

    Returns:
        bytes: The raw content downloaded from the specified URL.
    """
    logger.debug(f"Downloading {url}")
    url = baseurl.format(url=url)
    res = requests.get(url)
    # if 404
    if res.status_code == 404:
        raise RuntimeError("File not found on github")
    
    return res.content

last_commit_api_url = "https://api.github.com/repos/{id}/commits?path={filename}&limit=1"

@lru_cache(maxsize=64)
def git_last_commit_date(id, filename):
    """
    A function to retrieve the last commit date for a given id and filename using the last_commit_api_url.
    
    Args:
        id: The identifier for the commit.
        filename: The name of the file.
        
    Returns:
        The date of the last commit as a datetime object, or None if there was an error.
    """
    logger.debug(f"Getting last commit date for {id}/{filename}")
    r = requests.get(last_commit_api_url.format(id=id, filename=filename))
    try:
        rjson = r.json()
    except Exception:
        return None

    datestr = getDeep(rjson, 0, "commit", "committer", "date")
    if datestr is ERROR:
        return None
    
    dateobj = datetime.strptime(datestr, "%Y-%m-%dT%H:%M:%SZ")

    return dateobj

@lru_cache(maxsize=64)
def git_last_commit_sha(id, filename):
    """
    Get the last commit SHA for the given ID and filename.

    Args:
        id (any): The ID for the commit.
        filename (str): The name of the file.

    Returns:
        The last commit SHA if successful, otherwise None.
    """
    logger.debug(f"Getting last commit sha for {id}/{filename}")
    r = requests.get(last_commit_api_url.format(id=id, filename=filename))
    try:
        rjson = r.json()
    except Exception:
        return None

    return getDeep(rjson, 0, "sha")