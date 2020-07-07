import pandas as pd
import numpy as np

table_name_list = ['Class_Info', 'Mileage_Result']

def load_data_pd(file_name, print_data = False):
    df = pd.read_csv(file_name, names = range(20), sep = '\t')
    
    groups = df[0].isin(table_name_list).cumsum()
    tables = {g.iloc[0, 0] : g.iloc[1:] for k, g in df.groupby(groups)}

    Class_Info = tables['Class_Info']
    Class_Info = Class_Info.rename(columns=Class_Info.iloc[0])
    Class_Info = Class_Info.drop(Class_Info.index[0])
    Class_Info.reset_index(drop = True, inplace = True)
    Class_Info.index += 1
    Class_Info.dropna(axis = 1, how = 'all', inplace = True)

    Mileage_Result = tables['Mileage_Result']
    Mileage_Result = Mileage_Result.rename(columns=Mileage_Result.iloc[0])
    Mileage_Result = Mileage_Result.drop(Mileage_Result.index[0])
    Mileage_Result.reset_index(drop = True, inplace = True)
    Mileage_Result.index += 1
    Mileage_Result.dropna(axis = 1, how = 'all', inplace = True)
    
    mask1 = (Mileage_Result['전공자여부'] == 'N (N)')
    Mileage_Result.loc[mask1, '전공자여부'] = 0
    
    mask2 = ((Mileage_Result['전공자여부'] == 'Y (N)') | (Mileage_Result['전공자여부'] == 'Y (Y)'))
    Mileage_Result.loc[mask2, '전공자여부'] = 1
    
    mask3 = Mileage_Result[Mileage_Result['순위'] == '0'].index
    Mileage_Result.drop(mask3, inplace = True)
    
    mask4 = (Mileage_Result['수강여부'] == 'O')
    Mileage_Result.loc[mask4, '수강여부'] = 1
    
    mask5 = (Mileage_Result['수강여부'] == 'X')
    Mileage_Result.loc[mask5, '수강여부'] = 0
    
    
    
    
    Mileage_Result.drop(['졸업신청', '초수강여부', '비고', '순위'], axis=1, inplace = True)
    
    Mileage_Result = Mileage_Result.apply(pd.to_numeric)