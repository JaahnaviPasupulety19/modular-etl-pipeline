# from sklearn.preprocessing import StandardScaler

# def scale_data(df, columns=None):
#     scaler = StandardScaler()

#     # Auto-detect numeric columns if not provided
#     if columns is None:
#         columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

#     df[columns] = scaler.fit_transform(df[columns])
#     return df

# ==========================================================
# from sklearn.preprocessing import StandardScaler

# def scale_data(df, columns):
#     if not columns:
#         return df

#     valid_cols = [col for col in columns if col in df.columns]

#     if not valid_cols:
#         return df  # nothing to scale

#     scaler = StandardScaler()
#     df[valid_cols] = scaler.fit_transform(df[valid_cols])

#     return df


from sklearn.preprocessing import StandardScaler

def scale_data(df, columns=None):
    # If no columns provided → auto-detect numeric
    if not columns:
        columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    valid_cols = [col for col in columns if col in df.columns]

    if not valid_cols:
        return df

    scaler = StandardScaler()
    df[valid_cols] = scaler.fit_transform(df[valid_cols])

    return df