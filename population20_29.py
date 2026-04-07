import pandas as pd

def cleaned_pop_2020_2029():

    pop_20_29_df = pd.read_csv('population-2020-2029.csv')
    

    # pop_20_29_df.info()
    # print("=="*20)

    #Rename column
    pop_20_29_df.rename(columns={'Time':'Year','PopMale':'Male','PopFemale':'Female'},inplace=True)

    #print(pop_20_29_df['AgeGrp'].unique())
    pop_20_29_df = pop_20_29_df[pop_20_29_df['AgeGrp'] != 'NO DATA']

    ##replace values 
    pop_20_29_df.replace({'AgeGrp':{'05. Sep':'4-9','Okt 14':'10-14','905. Sep9':'95-99','100+':'100-104'}},inplace=True)
    #print(pop_20_29_df['AgeGrp'].unique())


    #Change Datatype
    pop_20_29_df['LocID'] = pop_20_29_df['LocID'].astype(int)
    pop_20_29_df['Year'] = pop_20_29_df['Year'].astype(int)
    pop_20_29_df['Male'] = pop_20_29_df['Male'].astype(float)
    pop_20_29_df['Female'] = pop_20_29_df['Female'].astype(float)


    #print(pop_20_29_df.describe())

    # Drop unnecessary columns
    pop_20_29_df.drop(columns=['AgeGrpStart','AgeGrpSpan','PopTotal'],inplace=True)
    
    return pop_20_29_df  # Return the cleaned DataFrame

  # Keep the function as it is, then at the very bottom:

if __name__ == "__main__":
    # This code only runs when you run population20_29.py directly
    clean_df2 = cleaned_pop_2020_2029()
    print(clean_df2) 
    clean_df2.to_csv('pop_2020_2029_cleanfile.csv', index=False)