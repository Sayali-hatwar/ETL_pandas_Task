import pandas as pd

def cleaned_pop_2030_2040():
    pop_30_40_df = pd.read_excel('population-2030-2040.xlsx',header=0)

    # rename
    pop_30_40_df.rename(columns={'Time':'Year','PopMale':'Male','PopFemale':'Female'},inplace=True)

    #drop null
    pop_30_40_df.dropna(inplace=True)

    #Check null if any
    # print(pop_30_40_df.isna().any())

    #check unique values
    #print(pop_30_40_df['AgeGrp'].unique())
    pop_30_40_df.replace({'100+':'100-104'},inplace=True)
    #print(pop_30_40_df['AgeGrp'].unique())


    # change datatype
    pop_30_40_df['LocID'] = pop_30_40_df['LocID'].astype(int)
    pop_30_40_df['Year'] = pop_30_40_df['Year'].astype(int)

    #replace male value
    #======================== Method1 ==========================

    #print(pop_30_40_df['Male'].sort_values())
    #4730 - ERROR_6.246
    # ivalue = pop_30_40_df[pop_30_40_df['Male'] == 'ERROR_6.246']
    # ivalue['Male'] = ivalue['PopTotal'] - ivalue['Female']
    # pop_30_40_df['Male'].loc[4730] == ivalue
    #======================== Method2 ==============================


    ivalue = pop_30_40_df['Male'] == 'ERROR_6.246'
    new_value = pop_30_40_df.loc[ivalue,'PopTotal'].astype(float) - pop_30_40_df.loc[ivalue,'Female'].astype(float)
    #print('new_value : ',new_value.values[0])

    pop_30_40_df.loc[ivalue,'Male'] = new_value.values[0].astype(str)

    pop_30_40_df['Male'] = pop_30_40_df['Male'].astype(float)

    # remove col
    pop_30_40_df.drop(columns=['AgeGrpStart','AgeGrpSpan','PopTotal'],inplace=True)

    # pop_30_40_df.info()

    print(pop_30_40_df)

    return pop_30_40_df



cleaned_pop_2030_2040()


#clean_pop_30_40.to_csv('pop_2030_2040_cleanfile.csv',index=False)







