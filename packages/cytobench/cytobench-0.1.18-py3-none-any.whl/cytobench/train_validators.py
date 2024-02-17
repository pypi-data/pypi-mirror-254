# load required libraries
import numpy as np
import pandas as pd
import os

# loading configurations and storing validators in binary objects
import yaml
import joblib

from .validation_functions import Discriminator
from .datasets_manager import load_dataset

def generate_negative_samples(reads, n_synth, activation_threshold, percent_swap, self_swap = False):
    
    '''
    Given a set of original cells, returns a dataset (of size n_synth) of cells with their genes
    shuffled between samples; this should promote breaking correlations, whilst maintaining actually observed gene expression;
    some of the generated cells might (and will) be identical to actually real ones, especially on certain shuffling thresholds
    
    self_swap: if the reads should be swapped in the cell itself or from another one in the dataset
    '''
    
    activation_mask = reads >= activation_threshold

    bootstrap_cells = np.random.choice(len(reads), size = n_synth)

    new_reads = np.copy(reads[bootstrap_cells])
    
    for i in range(len(new_reads)):
        
        # pick target cell as self or among any in the dataset
        target_cell_i = bootstrap_cells[i] if self_swap else np.random.choice(len(reads))

        # select genes to swap
        active_genes_target = np.arange(activation_mask.shape[1])[ activation_mask[target_cell_i] ]

        active_genes_current = np.arange(activation_mask.shape[1])[ activation_mask[i] ]

        n_genes_swap = min(int(len(active_genes_current) * percent_swap), len(active_genes_target))

        active_genes_swap = np.random.choice(active_genes_target, size = n_genes_swap, replace = False)
        active_genes_current = np.random.choice(active_genes_current, size = n_genes_swap, replace = False)

        # remove counts on swapped genes
        new_reads[i][active_genes_current] = 0

        # copy active genes in the target cell
        new_reads[i][active_genes_swap] = reads[target_cell_i][active_genes_swap]
        
    # return the synthetic reads
    return new_reads

def cycle_generation(reads, p_cells_per_bootstrap = .2):
    
    # percentage of cells from reads to use at each iteration
    n_cells_per_bootstrap = int(len(reads) * p_cells_per_bootstrap)

    # genes threshold to mask on (>=)
    genes_thresholds = [0, .15, .3, .45]

    # possible percentages of selected genes to swap
    swap_percentages = [.05, .1, .2, .4]

    negative_samples = {}

    for self_swap in [True, False]:

        for activation_threshold in genes_thresholds:

            for percent_swap in swap_percentages:

                # print('Generating', (self_swap, activation_threshold, percent_swap))

                negative_samples[(self_swap, activation_threshold, percent_swap)] = generate_negative_samples(
                    reads, n_cells_per_bootstrap, activation_threshold, percent_swap, self_swap)
    
    # collect all together
    data = np.concatenate([ negative_samples[k] for k in negative_samples ])
    print('Total negative samples generated:', len(data))
    
    # add true reads
    data = np.concatenate((reads, data))
    y = np.array(np.arange(len(data)) < len(reads), dtype=int)
    
    # return randomized arrays
    random_order = np.random.choice(len(data), len(data), replace = False)

    return data[random_order], y[random_order]

def get_n_pairs(counts, perc_points = .01):
    
    '''
    input: pool of reads to pick from and n of pairs to return (in form of percentage)
    output: n pairs of counts, that can then be stored and used at evaluation time
    '''
    
    n_pairs = int(len(counts) * perc_points)
    
    pair_a = np.random.choice(len(counts), n_pairs, replace=False)
    pair_b = np.random.choice(np.arange(len(counts))[~np.isin(np.arange(len(counts)), pair_a)], n_pairs, replace=False)
    
    assert set(pair_a).intersection(pair_b) == set()
    
    return np.stack((counts[pair_a], counts[pair_b]), axis=1)

def get_training_masks(n_samples, train_p = .6, validation_p = .3, test_p = .1, seed = 42):
    
    # reset seed for consistent results
    np.random.seed(seed)

    # sample train test validation datasets in order to have them fixed through the project
    training_mask, validation_mask, test_mask = np.full(n_samples, False), np.full(n_samples, False), np.full(n_samples, False)

    training_mask[ np.random.choice(n_samples, int(n_samples*.6), replace=False) ] = True
    validation_mask[ np.random.choice(np.arange(n_samples)[~training_mask], int(n_samples*.3), replace=False) ] = True
    test_mask[ np.arange(n_samples)[~training_mask & ~validation_mask] ] = True
    
    # double check
    assert sum(training_mask) + sum(validation_mask) + sum(test_mask) == n_samples, "masks don't correspond to input numerosity"

    # return masks
    return training_mask, validation_mask, test_mask

def score_model(y_true, y_pred):
    
    true_mask = y_true == 1
    
    correct_true = np.sum(y_pred[true_mask] == 1) / sum(true_mask)
    correct_false = np.sum(y_pred[~true_mask] == 0) / sum(~true_mask)
    
    return correct_true, correct_false

def unsupervised_score(model, points_pairs, segment_length = 1, n_interpolations = 1000):
    
    scores = []

    for points_pair in points_pairs:
        
        middle_point = np.mean(points_pair, axis=0)

        # Calculate the direction vector and its half
        half_vector = .5 * segment_length * (points_pair[1] - points_pair[0])
        
        # Extend the start and end points
        validate_points = np.linspace(middle_point - half_vector, middle_point + half_vector, num=n_interpolations)
        predictions = model.predict(validate_points)
        
        # just score the model as percentage of 0 found
        scores.append(sum(predictions == 0) / n_interpolations)

    # return the mean value of all scores
    return np.mean(scores)

def print_model_score(model, x_validate, y_validate, pairs):
    
    # compute capacity of recognizing true positives
    correct_true, correct_false = score_model(y_validate, model.predict(x_validate))
    print('Validation score:', np.round(np.mean([correct_true, correct_false]), 2), np.round([correct_true, correct_false], 2))

    # compute capacity of rejecting synthetic data
    internal_score = unsupervised_score(model, pairs, segment_length = 1)
    external_score = unsupervised_score(model, pairs, segment_length = 10)

    print('Unsupervised score:', np.round(np.mean([internal_score, external_score]), 2), np.round([internal_score, external_score], 2))
    
    # the global score is computed averaging the true positive acceptance rate and synthetic negatives rejection power
    print('Global score:', np.round(np.mean([correct_true, np.mean([internal_score, external_score])]), 2))

    
'''
FIX: once the yaml files with the configurations will be implemented,
load the settings from there
'''

script_dir = os.path.dirname(__file__)

validators_dir = os.path.join(script_dir, 'cytobench-validators/')

# paper root directory for all reference files (load from yaml)
# validators_dir = 'validators/'

# dataset (get from python inputs)
dataset = 'tabula muris simple'

def train_validators(dataset):

    # splits (get from yaml)
    n_splits = 3

    # train models for all splits
    for split_i in range(n_splits):
        
        for internal_data in [True, False]:
            
            print(f'\nGenerating data for "{dataset}" dataset, split {split_i+1}, {"internal" if internal_data else "external"} distribution')
            
            X, genes, metadata = load_dataset(dataset, split_i, internal_data)
        
            training_mask, validation_mask, test_mask = get_training_masks(len(X))

            # generate negative samples to train the discriminator with
            x_train, y_train = cycle_generation(X[training_mask])
            x_validate, y_validate = cycle_generation(X[validation_mask])
            x_test, y_test = cycle_generation(X[test_mask])
            
            # collect pair of points for unsupervised validation of discriminator
            # training_pairs = get_n_pairs(X[training_mask])
            validation_pairs = get_n_pairs(X[validation_mask])
            testing_pairs = get_n_pairs(X[test_mask])
            
            print('Training discriminator...')
            
            # atm pos_weight is fixed by the negative samples ratio
            pos_weight = 6.4
            
            # train discriminator
            model = Discriminator(pos_weight_adj = pos_weight, max_estimators = 500, max_depth=4, pca_dim=16)
            model.fit(x_train, y_train, x_validate, y_validate)

            # print(f'Training completed, using {model.model.best_ntree_limit} trees')
            
            print('Scoring on validation set...')
            
            print_model_score(model, x_validate, y_validate, validation_pairs)
            
            print('Scoring on test set...')
            
            print_model_score(model, x_test, y_test, testing_pairs)

            model_path = f'{validators_dir}{dataset}-{split_i}-{internal_data}.joblib'
            
            os.makedirs(os.path.dirname(model_path), exist_ok=True)

            # store the model
            joblib.dump(model, model_path)