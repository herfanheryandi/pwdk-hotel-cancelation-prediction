class Remove:
    def __init__(self, columns_to_remove=None):

        self.columns_to_remove = columns_to_remove if columns_to_remove is not None else []

    def fit(self, X, y=None):

        if isinstance(X, pd.DataFrame):
            self.columns_to_remove = [col for col in self.columns_to_remove if col in X.columns]
        return self

    def transform(self, X,y=None):

        return X.drop(columns=self.columns_to_remove, errors='ignore')

    def fit_transform(self, X, y=None):

        return self.fit(X, y).transform(X)