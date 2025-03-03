from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class RareLabelTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns, threshold=0.01):

        self.columns = columns
        self.threshold = threshold

    def fit(self, X, y=None):

        if not isinstance(X, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        
        self.nonrare_labels_ = {}
        
        for column in self.columns:
            if column in X.columns:
                value_counts = X[column].value_counts(normalize=True)
                nonrare_labels = value_counts[value_counts >= self.threshold].index
                self.nonrare_labels_[column] = nonrare_labels
        
        return self

    def transform(self, X):

        if not isinstance(X, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        
        X_transformed = X.copy()
        
        for column in self.columns:
            if column in X_transformed.columns:
                nonrare_labels = self.nonrare_labels_.get(column, [])
                X_transformed[column] = X_transformed[column].apply(lambda x: 'Other' if x not in nonrare_labels else x)
        
        return X_transformed

    def fit_transform(self, X, y=None):

        self.fit(X)
        return self.transform(X)