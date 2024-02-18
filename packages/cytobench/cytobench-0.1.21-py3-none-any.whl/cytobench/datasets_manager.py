
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
    counts = scipy.io.mmread(f"{directory}/{dataset}-counts.mtx").tocsr()

    # Load the list data from the comma separated text file
    genes = pd.read_csv(f"{directory}/{dataset}-genes.csv", header=None).squeeze("columns").tolist()

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

    local_dir = os.path.join(script_dir, 'cytobench-datasets')
    os.makedirs(local_dir, exist_ok=True)

    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '-genes.csv')
    # download_file(genes_file, local_path)
    m.download_url(genes_file, dest_path=local_dir)
    
    print("Downloading metadata file...")

    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '-metadata.csv')
    # download_file(metadata_file, local_path)
    m.download_url(metadata_file, dest_path=local_dir)
    
    print("Downloading counts file...")

    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '-counts.mtx')
    # download_file(counts_file, local_path)
    m.download_url(counts_file, dest_path=local_dir)

    print('Unpacking files...')

    local_path = os.path.join(script_dir, 'cytobench-datasets')

    counts, genes, metadata = load_data(local_path, dataset)

    # store the dataset files as joblib object for future use
    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '.joblib')
    joblib.dump((counts, genes, metadata), local_path)

    print("Download complete.")

    return counts, genes, metadata



# dummy functions
datasets = ['tabula-muris-simple-droplet-v1']

# dataset splits: != 3m, != 18, != 24m
dataset_splits = [
    [
        '24-M-60', '18-F-50', '18-F-51', '18-M-52', '18-M-53', 
        '21-F-54', '21-F-55', '24-M-58', '24-M-59', '24-M-61',
        '1-M-63', '30-M-2', '30-M-3', '30-M-4', '30-M-5', '1-M-62'
    ],
    [
        '24-M-60', '21-F-54', '21-F-55', '24-M-58', '24-M-59', 
        '24-M-61', '1-M-63', '30-M-2', '30-M-3', '30-M-4',
        '30-M-5', '1-M-62', '3-M-8', '3-M-9', '3-M-8/9', 
        '3-F-56', '3-F-57', '3-M-5/6', '3-M-7/8'
    ],
    [
        '18-F-50', '18-F-51', '18-M-52', '18-M-53', '21-F-54', 
        '21-F-55', '1-M-63', '30-M-2', '30-M-3', '30-M-4',
        '30-M-5', '1-M-62', '3-M-8', '3-M-9', '3-M-8/9', 
        '3-F-56', '3-F-57', '3-M-5/6', '3-M-7/8'
    ]
]


def load_dataset(dataset, split = 0, internal = True):
    
    assert split < len(dataset_splits), "the selected dataset doesn't have that many splits"
    assert internal in [True, False], "distribution parameter should be a boolean"
    assert dataset in datasets, "unrecognized dataset name"
    
    local_path = os.path.join(script_dir, 'cytobench-datasets', dataset + '.joblib')
    
    if not os.path.exists(local_path):
        reads, genes, metadata = download_dataset(dataset)

    else:
        reads, genes, metadata = joblib.load(local_path)
    
    # mask patients from current split or the complement according to internal_data
    mask = metadata['mouse.id'].isin(dataset_splits[split]) == internal
    
    # reads are stored in compressed sparse row format;
    # convert to normal numpy array before returning
    return reads[mask].toarray(), genes, metadata[mask]