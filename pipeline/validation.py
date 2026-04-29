# def validate_columns(df, required_cols):
#     missing = [col for col in required_cols if col not in df.columns]
#     if missing:
#         raise ValueError(f"Missing columns: {missing}")
#     return True



def validate_columns(df, required_cols):
    if not required_cols:
        return True

    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return True


def validate_nulls(df, cols):
    null_cols = [col for col in cols if df[col].isnull().sum() > 0]
    if null_cols:
        raise ValueError(f"Null values found in columns: {null_cols}")

    return True