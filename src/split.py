from sklearn import train_test_split
import pandas as pd


def simple_split (features_df, train, test, val):

    if val == 0:
        train_df = df.sample(frac = train)
        
        # Creating dataframe with
        # rest of the 50% values
        test_df = df.drop(train.index)
        
        print("\nTraining DataFrame:")
        print(train)
        
        print("\nTesting DataFrame:")
        print(rest_part_50)


        # Creating a dataframe with 50%
# values of original dataframe
part_50 = df.sample(frac = 0.5)
 
# Creating dataframe with
# rest of the 50% values
rest_part_50 = df.drop(part_50.index)
 
print("\n50% of the given DataFrame:")
print(part_50)
 
print("\nrest 50% of the given DataFrame:")
print(rest_part_50)