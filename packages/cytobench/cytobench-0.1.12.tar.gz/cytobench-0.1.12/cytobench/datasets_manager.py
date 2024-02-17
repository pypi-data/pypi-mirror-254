
import os
import requests
import pandas as pd
import numpy as np
import joblib
import scipy
from mega import Mega

script_dir = os.path.dirname(__file__)

def download_file(url, local_filename):
    
    # Ensure the local directory exists
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)
    
    # Stream download to handle large files
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename


def load_data(directory, dataset):
    
    # Load the sparse matrix and convert it back to a Numpy array
    counts = scipy.io.mmread(f"{directory}/{dataset}-counts.mtx")

    # Load the list data from the comma separated text file
    genes = pd.read_csv(f"{directory}/{dataset}-genes.csv", header=None, squeeze=True).tolist()

    # Load the Pandas DataFrame from the CSV file
    metadata = pd.read_csv(f"{directory}/{dataset}-metadata.csv")

    return counts, genes, metadata


def download_dataset(dataset):

    assert dataset in ['tabula-muris-simple-droplet-v1'], 'dataset not found'

    mega = Mega()
    m = mega.login()

    genes_file = "https://mega.nz/file/Y0VCHTiL#-6RMTZh9ZWO4GkGJlEGl5hyyNDsHONSayN9aJ_cpl5I"
    metadata_file = "https://mega.nz/file/99d2WIwK#pXOP4j3REic1xhwe9Ms5ODpgO1BKrDwrwzDEaamrbcQ"
    counts_file = "https://mega.nz/file/1psUySSD#YQVpUULCXP605gW-RGt1SCbkpA18RwRK1rCN7PehNvs"

    print("Downloading genes file...")

    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '-genes.txt')
    # download_file(genes_file, local_path)
    file = m.download_url(genes_file)
    m.download(file, local_path)
    
    print("Downloading metadata file...")

    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '-metadata.csv')
    # download_file(metadata_file, local_path)
    file = m.download_url(metadata_file)
    m.download(file, local_path)
    
    print("Downloading counts file...")

    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '-counts.mtx')
    # download_file(counts_file, local_path)
    file = m.download_url(counts_file)
    m.download(file, local_path)

    print('Unpacking files...')

    local_path = os.path.join(script_dir, 'cytobench-datasets')

    counts, genes, metadata = load_data(local_path, dataset)

    # store the dataset files as joblib object for future use
    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '.joblib')
    joblib.dump((counts, genes, metadata), local_path)

    print("Download complete.")

    return counts, genes, metadata