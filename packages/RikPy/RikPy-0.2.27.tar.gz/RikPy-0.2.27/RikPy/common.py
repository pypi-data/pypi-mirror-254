from urllib.parse import urlparse
import os
import requests
import logging


def trial_function():
    print("Hey it's woooorking!")

def extract_file_extension(file_url):
    # Parse the URL to handle both formats
    parsed_url = urlparse(file_url)

    # Split the path component to get the filename
    filename = os.path.basename(parsed_url.path)

    # Split the filename to get the file extension
    _, file_extension = os.path.splitext(filename)

    # Clean up any query parameters that might be part of the extension
    file_extension = file_extension.split('?')[0]

    return file_extension

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

def download_image(image_url, local_file_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(local_file_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

    return