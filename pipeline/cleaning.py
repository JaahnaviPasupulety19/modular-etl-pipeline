def handle_missing(df):
    return df.ffill()

def remove_duplicates(df):
    return df.drop_duplicates()