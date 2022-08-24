from sklearn import train_test_split
import pandas as pd

def blind_holdout (features_df):
    
    blind_holdout_df = features_df.sample(frac = 0.15)
    features_df = features_df.drop(blind_holdout_df.index)
    
    print("\n15% of the data has been stored as the Blind Holdout. It is available in the /data/features folder.")

    return features_df


def simple_split (features_df, train_ratio):

    features_df = blind_holdout (features_df)

    #Creating a train/test split
    train_df = features_df.sample(frac = train_ratio)
    
    # Creating dataframe with
    # rest of the 50% values
    test_df = features_df.drop(train_df.index)

    return train_df, test_df

