import os
import zipfile
import io

def zip_not_same(zipobj1 : zipfile.ZipFile, zipobj2 : zipfile.ZipFile):
    """
    Compares the contents of two zip files. Takes two zipfile.ZipFile objects as 
    parameters and returns True if the contents are not the same, and False 
    otherwise.
    """
    traversed1 = set()
        
    for filename in zipobj1.namelist():
        traversed1.add(filename)

        if filename not in zipobj2.namelist():
            return True

        if zipobj1.getinfo(filename).file_size != zipobj2.getinfo(filename).file_size:
            return True

    if traversed1 != set(zipobj2.namelist()):
        return True
        
    return False

def make_zip(folder : str, exclusions : list = [], targetPath : str = None):
    """
    Create a zip file from the given folder, excluding specific files and folders.
    
    Args:
        folder (str): The path to the folder to be zipped.
        exclusions (list, optional): List of files and folders to be excluded from the zip. Default is [].
        targetPath (str, optional): The path where the zip file will be saved. If None, returns the zip file as bytes. Default is None.
        
    Returns:
        io.BytesIO or None: If targetPath is None, returns the zip file as bytes. If targetPath is provided and the zip file is successfully created, returns None.
    """
    if targetPath is not None and os.path.isdir(targetPath):
        foldername = os.path.basename(folder)
        targetPath = os.path.join(targetPath, foldername+".zip")                          
        
    zipBytes = io.BytesIO()
    zipObj = zipfile.ZipFile(zipBytes, 'w')
    
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # exclude files start with _ and folder with __
            if filename.startswith("_") or os.path.basename(folderName).startswith("__"):
                continue
            
            # check exclusion
            basename = os.path.basename(folderName)
            if basename in exclusions:
                continue
            
            filePath = os.path.join(folderName, filename)
            if any(x in filePath for x in exclusions):
                continue
            
            archiveName = os.path.relpath(filePath,folder)

            zipObj.write(filePath, archiveName)        
    
    if targetPath is None:
        return zipBytes
    
    if os.path.exists(targetPath):
        
        with zipfile.ZipFile(targetPath) as zipObj2:
            if not zip_not_same(zipObj, zipObj2):
                zipObj.close()
                return None

        os.remove(targetPath)
        
    zipObj.close()
    with open(targetPath, 'wb') as f:
        f.write(zipBytes.getvalue())
    
    return zipBytes
    
def extract_zip(zipobj : zipfile.ZipFile, folder : str):
    """
    Extracts all the contents of a zip file to a specified folder.

    Args:
        zipobj (zipfile.ZipFile): The zip file object to extract from.
        folder (str): The path to the folder where the contents will be extracted.

    Returns:
        None
    """
    if isinstance(zipobj, bytes):
        zipobj = zipfile.ZipFile(io.BytesIO(zipobj))
    
    zipobj.extractall(folder)