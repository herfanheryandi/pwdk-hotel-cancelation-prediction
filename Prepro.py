import pandas as pd

class Prepro:
    def __init__(self):

        pass

    def fit(self, X, y=None):

        return self

    def transform(self, X):
        def check_weekday_weekend(date):
            if date.weekday() < 5:
                return "Weekday"
            else:
                return "Weekend"
        def arrival_month(date):
            if "January" in date:
                return date.replace("January", "01")
            elif "February" in date:
                return date.replace("February", "02")
            elif "March" in date:
                return date.replace("March", "03")
            elif "April" in date:
                return date.replace("April", "04")
            elif "May" in date:
                return date.replace("May", "05")
            elif "June" in date:
                return date.replace("June", "06")
            elif "July" in date:
                return date.replace("July", "07")
            elif "August" in date:
                return date.replace("August", "08")
            elif "September" in date:
                return date.replace("September", "09")
            elif "October" in date:
                return date.replace("October", "10")
            elif "November" in date:
                return date.replace("November", "11")
            elif "December" in date:
                return date.replace("December", "12")
        X['arrival_date'] = X['arrival_date_year'].map(str) + "-" + X['arrival_date_month'].map(str) + "-" + X['arrival_date_day_of_month'].map(str)
        X['arrival_date'] = X['arrival_date'].apply(arrival_month)
        X['arrival_date'] = pd.to_datetime(X['arrival_date'])
        X["arrival_day_type"] = X['arrival_date'].apply(check_weekday_weekend)
        X['is_same_room']=X.apply(lambda x: 1 if x['reserved_room_type'] == x['assigned_room_type'] else 0, axis=1)
        X['agent'] = X['agent'].astype(str)
        return X

    def fit_transform(self, X, y=None):

        return self.fit(X, y).transform(X)
    