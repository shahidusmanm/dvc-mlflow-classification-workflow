import pandas as pd
import os 
import config

def blind_holdout (features_df):
    
    if not os.path.exists('feature_store'):
        os.makedirs('feature_store')

    blind_holdout_df = features_df.sample(frac = 0.15)
    features_df = features_df.drop(blind_holdout_df.index)
    blind_holdout_df.to_csv("feature_store/blind_holdout.csv", index = False)
    print("\n15% of the data has been stored as the Blind Holdout. It is available in the /src/feature_store folder.")
    
    return features_df


def simple_split (features_df, train_ratio):

    features_df = blind_holdout (features_df)
    train_df = features_df.sample(frac = train_ratio)
    test_df = features_df.drop(train_df.index)
    train_df.to_csv("feature_store/train.csv", index = False)
    test_df.to_csv("feature_store/test.csv", index = False)

    return train_df, test_df

#Main Execution
df = pd.read_csv(config.root_dir + 'data/features/features.csv')
simple_split(df, config.train_ratio)