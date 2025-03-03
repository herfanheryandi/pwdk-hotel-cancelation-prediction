from sklearn.base import BaseEstimator, TransformerMixin

class MissingValueImputer(BaseEstimator, TransformerMixin):
    def __init__(self, numerical_columns, categorical_columns):
        self.numerical_columns = numerical_columns
        self.categorical_columns = categorical_columns
        self.medians = {}
    
    def fit(self, X, y=None):
        # Calculate medians for numerical columns
        for col in self.numerical_columns:
            self.medians[col] = X[col].median()
    
    def transform(self, X):
        X = X.copy()  # Avoid modifying the original DataFrame
        
        # Impute numerical columns
        for col in self.numerical_columns:
            X.fillna({col: self.medians[col]},inplace=True)
        # Impute categorical columns
        for col in self.categorical_columns:
            X.fillna({col: 'unknown'},inplace=True)
        
        return X

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)