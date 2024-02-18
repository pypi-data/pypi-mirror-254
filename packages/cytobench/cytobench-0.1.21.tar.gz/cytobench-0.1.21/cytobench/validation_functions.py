import numpy as np

import scipy.spatial
import scipy.stats

import xgboost
import sklearn.decomposition

from sklearn.neighbors import NearestNeighbors


class CoverageEstimator:
    
    def __init__(self, reference_points):
        
        self.n_reference_points = len(reference_points)

        # create a NearestNeighbors classifier from the points
        self.reference_tree = NearestNeighbors(n_neighbors=1, n_jobs=-1, metric='cosine').fit(reference_points)
        
        # initiate reference ideal distribution for entropy comparison
        self.reference_entropy = scipy.stats.entropy(np.ones(self.n_reference_points))
            
    def bin_observations(self, sample_population):
        
        # convert a sample population to a distribution of neighbours
        _, indices = self.reference_tree.kneighbors(sample_population)

        return np.bincount(indices[:,0], minlength=self.n_reference_points).astype(float)
    
    def entropy_test(self, sample_population, invalid_points = 0, score_fraction = 1):
        
        # return 0 for edge case where valid population is 0
        if len(sample_population) == 0:
            return 0
        
        observed_counts = self.bin_observations(sample_population)
        
        if invalid_points > 0:
            observed_counts[np.argmax(observed_counts)] += invalid_points
            
        assert sum(observed_counts) == self.n_reference_points, 'sample population size must be equal to the number of reference points for the entropy to be stable'
        
        return scipy.stats.entropy(observed_counts) / self.reference_entropy * score_fraction
    

class Discriminator:
    def __init__(self, pos_weight_adj, max_depth = 3, max_estimators = 500, pca_dim=None):
        
        self.pos_weight_adj = pos_weight_adj
        self.max_estimators = max_estimators
        self.max_depth = max_depth
        self.pca_dim = pca_dim
        
        self.model = None
        self.pca = None

    def fit(self, x_train, y_train, x_validation, y_validation):
        if self.pca_dim:
            self.pca = sklearn.decomposition.PCA(n_components=self.pca_dim)
            self.pca.fit(x_train[y_train==1])
            
            x_train = self.pca.transform(x_train)
            x_validation = self.pca.transform(x_validation)
        
        self.model = xgboost.XGBClassifier(
            tree_method='hist', objective="binary:logistic",
            subsample= 0.7, colsample_bytree= 0.7,
            n_estimators=self.max_estimators, max_depth=self.max_depth,
            scale_pos_weight=self.pos_weight_adj,
            n_jobs=-1, early_stopping_rounds = 5
        )
        self.model.fit(
            x_train, y_train,
            eval_set=[(x_validation, y_validation)],
            verbose=False
        )

    def predict(self, X):
        if self.pca:
            X = self.pca.transform(X)
        
        return self.model.predict(X)


def score_model(
    sampling_fn, data_validator, environment_points, expand_n = 100, n_copies = 100, 
    plateau_after_n = 10, max_iterations = 1000, normalize_scores = True, score_every_n = 1):
    
    assert len(environment_points) >= expand_n * n_copies, 'insufficient number of points compared to replicates'

    # initialize coverage estimator
    points_subset = np.random.choice(len(environment_points), size = expand_n * n_copies, replace=False)
    coverage_estimator = CoverageEstimator(np.copy(environment_points[points_subset]))

    # initialize initial population for expansion
    points_subset = np.random.choice(len(environment_points), size = expand_n, replace=False)
    initial_points = np.copy(environment_points[points_subset])

    # consider n_copies copies for each point
    current_population = np.repeat(initial_points, repeats=n_copies, axis=0)

    # initiate cycle variables
    max_score, n_plateau = 0, 0

    # initialize stats 
    valid_points, scores = [], []

    # start sampling
    for n_iteration in range(max_iterations+1):

        # actually score the model only once every score_every_n epochs,
        # while keeping on sampling at every iteration
        # note: the first iteration will and should always be scored for the baseline
        if n_iteration % score_every_n == 0:

            # validate current population
            validity_mask = data_validator.predict(current_population) == 1

            # score population (always use entropy)
            population_score = coverage_estimator.entropy_test(current_population[validity_mask], invalid_points = sum(~validity_mask))

            # store stats
            valid_points.append(sum(validity_mask) / len(validity_mask))
            scores.append(population_score)

            # check for new high
            if population_score > max_score:
                max_score = population_score
                n_plateau = 0

            else:
                n_plateau += 1

            # interrupt in case of plateau
            if n_plateau > plateau_after_n:
                break

        # sample new population (and check that the function didn't drop any point)
        # note: the max value of reads should be 1, if it goes over 10 the function has become unstable and will likely reach inf,
        # therefore we just cap them artificially
        current_population = np.minimum(sampling_fn(current_population), 10)

        assert len(current_population) == len(validity_mask)

    # normalize scores in the range 0-1 if required
    if normalize_scores:
        starting_score = scores[0]
        scores = (np.array(scores) - starting_score) / (1-starting_score)
        
    # return score and valid points progression
    return scores, valid_points