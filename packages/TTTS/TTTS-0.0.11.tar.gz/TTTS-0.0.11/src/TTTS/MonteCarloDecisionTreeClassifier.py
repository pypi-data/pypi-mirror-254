from sklearn.tree import DecisionTreeClassifier
from sklearn.utils.validation import check_is_fitted
import numpy as np
from sklearn.tree import _tree

class MonteCarloDecisionTreeClassifier(DecisionTreeClassifier):
    def __init__(self, prob_type='depth', n_simulations=10,criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0):
        
        super().__init__(criterion='gini', splitter='best', max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, min_weight_fraction_leaf=min_weight_fraction_leaf, max_features=max_features, random_state=random_state, max_leaf_nodes=max_leaf_nodes, min_impurity_decrease=min_impurity_decrease, class_weight=class_weight, ccp_alpha=ccp_alpha)
        if prob_type not in ['fixed', 'depth', 'certainty', 'agreement', 'distance', 'confidence']:
            raise ValueError('Invalid prob_type')
        self.prob_type = prob_type
        self.n_simulations = n_simulations
   
    def get_depth_based_probability(self, depth):
        return min(0.05 * depth, 0.2)

    def get_certainty_based_probability(self, node_id):
        node_values = self.tree_.value[node_id].flatten()
        total = np.sum(node_values)
        distribution = node_values / total
        max_certainty = np.max(distribution)
        p = 1 - max_certainty
        return min(p, 0.5)
    
    def get_agreement_based_probability(self, node_id):
        node_values = self.tree_.value[node_id].flatten()
        majority_class_ratio = np.max(node_values) / np.sum(node_values)
        p = 1 - majority_class_ratio
        return min(p, 0.5)
    
    def get_distance_based_probability(self, node_id, sample):
        feature_index = self.tree_.feature[node_id]
        distance = abs(sample[feature_index] - self.tree_.threshold[node_id])
        max_distance = np.max(abs(self.tree_.threshold))
        p = 0.1-min((distance/max_distance),0.1)
        return min(p, 0.5)

    def get_confidence_based_probability(self, X, node_id, sample):
        feature_index = self.tree_.feature[node_id]
        if feature_index == _tree.TREE_UNDEFINED:
            return 0
        
        feature_values = X[:, feature_index]
        avg = np.mean(feature_values)
        std = np.std(feature_values)
        
        distance = abs(sample[feature_index] - avg)
        p = max(0.1 - (distance / (std + 1e-9)), 0)
        return p

    
    def get_bayes_based_probability(self, node_id, sample):
        if self.tree_.children_left[node_id] == _tree.TREE_LEAF or self.tree_.children_right[node_id] == _tree.TREE_LEAF:
            # Can't calculate Bayesian probability at the leaf node.
            return 0
        
        parent_samples = self.tree_.n_node_samples[node_id]
        left_child_samples = self.tree_.n_node_samples[self.tree_.children_left[node_id]]
        right_child_samples = self.tree_.n_node_samples[self.tree_.children_right[node_id]]
        
        # P(child)
        p_child = left_child_samples / parent_samples if sample[self.tree_.feature[node_id]] <= self.tree_.threshold[node_id] else right_child_samples / parent_samples
        # P(parent)
        p_parent = 1  # As we are already at the parent
        # P(child | parent) can be assumed to be proportional to how well-distributed the child is
        p_child_given_parent = 0.5  # for the sake of simplicity
        
        # P(parent | child) using Bayes' theorem
        p_parent_given_child = p_child_given_parent * p_parent / p_child
        return p_parent_given_child
    
    def traverse_tree(self, node, sample, X, depth=0):
        if self.prob_type == 'fixed':
            p = 0.05
        elif self.prob_type == 'depth':
            p = self.get_depth_based_probability(depth)
        elif self.prob_type == 'certainty':
            p = self.get_certainty_based_probability(node)
        elif self.prob_type == 'agreement':
            p = self.get_agreement_based_probability(node)
        elif self.prob_type == 'distance':
            p = self.get_distance_based_probability(node, sample)
        elif self.prob_type == 'confidence':
            p = self.get_confidence_based_probability(X, node, sample)
        elif self.prob_type == 'bayes':
            p = self.get_bayes_based_probability(node, sample)
        else:
            raise ValueError('Invalid prob_type')

        if self.tree_.feature[node] != _tree.TREE_UNDEFINED:
            # internal node
            if sample[self.tree_.feature[node]] <= self.tree_.threshold[node]:
                # go to the left child with high probability
                if np.random.rand() > p:
                    return self.traverse_tree(self.tree_.children_left[node], sample, X, depth + 1)
                else:
                    return self.traverse_tree(self.tree_.children_right[node], sample, X, depth + 1)
            else:
                # go to the right child with high probability
                if np.random.rand() > p:
                    return self.traverse_tree(self.tree_.children_right[node], sample, X, depth + 1)
                else:
                    return self.traverse_tree(self.tree_.children_left[node], sample, X, depth + 1)
        else:
            # leaf
            return self.tree_.value[node]

    def predict_proba(self, X, n_simulations=None):
        if n_simulations is None:
            n_simulations = self.n_simulations
        
        check_is_fitted(self)
        X = super()._validate_X_predict(X, check_input=True)

        proba = []
        for x in X:
            simulation_results = [self.traverse_tree(0, x, X).ravel() for _ in range(n_simulations)]
            simulation_results = [arr/arr.sum() for arr in simulation_results]
            mean_proba = np.mean(simulation_results, axis=0)
            proba.append(mean_proba)

        return np.array(proba)

