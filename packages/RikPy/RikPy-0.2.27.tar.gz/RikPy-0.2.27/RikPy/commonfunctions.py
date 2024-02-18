import requests
import os

def download_file_local(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def delete_local_file(file_name):
    try:
        # Check if file exists
        if os.path.exists(file_name):
            # Delete the file
            os.remove(file_name)
            return f"File '{file_name}' has been deleted."
        else:
            return f"File '{file_name}' does not exist."

    except Exception as e:
        return f"An error occurred while deleting the file: {e}"