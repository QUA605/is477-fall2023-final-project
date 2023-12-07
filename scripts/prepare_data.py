import hashlib
import requests
import os
import zipfile

# Set the target directory to be in the parent directory
target_dir = 'data'
os.makedirs(target_dir, exist_ok=True)

urls = [
    'https://archive.ics.uci.edu/static/public/186/wine+quality.zip'
]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]

        with open(os.path.join(target_dir, file_name), 'wb') as file:
            file.write(response.content)

        if file_name.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(target_dir, file_name), 'r') as zip_ref:
                zip_ref.extractall(target_dir)

        print(f'Successfully downloaded and saved: {file_name}')
    else:
        print(f'Failed to download: {url}')

file_hashes = {
    'winequality-red.csv': "4a402cf041b025d4566d954c3b9ba8635a3a8a01e039005d97d6a710278cf05e",
    'winequality-white.csv': "76c3f809815c17c07212622f776311faeb31e87610d52c26d87d6e361b169836",
    'winequality.names': "15d215e73b39105952380fd487e4ce1bf5a6b83a425abb285c2ec55193d3ca92",
}
for file_name, expected_hash in file_hashes.items():
    file_path = os.path.join(target_dir, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
            computed_hash = hashlib.sha256(content).hexdigest()

            if computed_hash == expected_hash:
                print(f'Hash match for {file_name}: File is valid.')
            else:
                print(f'Hash mismatch for {file_name}: File is corrupted.')
    else:
        print(f'{file_name} not found in the "data" folder.')