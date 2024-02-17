import yaml
import joblib
import scipy.sparse

from validation_functions import CoverageEstimator, Discriminator, score_model

import os
script_dir = os.path.dirname(__file__)

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
    
    path = os.path.join(script_dir, 'datasets', dataset + '.joblib')
    
    reads, genes, metadata = joblib.load(path)
    
    # mask patients from current split or the complement according to internal_data
    mask = metadata['mouse.id'].isin(dataset_splits[split]) == internal
    
    # reads are stored in compressed sparse row format;
    # convert to normal numpy array before returning
    return reads[mask].toarray(), genes, metadata[mask]


def load_validator(dataset, split = 0, internal = True):
    
    assert split < len(dataset_splits), "the selected dataset doesn't have that many splits"
    assert internal in [True, False], "internal_data should be a boolean"
    assert dataset in datasets, "unrecognized dataset name"
    
    path = os.path.join(script_dir, 'validators', f'{dataset}-{split}-{internal}.joblib')
    
    return joblib.load(path)

