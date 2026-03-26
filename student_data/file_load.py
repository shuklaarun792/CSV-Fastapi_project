import pandas as pd
import numpy as np

def file_load():
    try:

        df=pd.read_csv(r"C:\Users\DELL\Downloads\students_complete.csv")


        df["gpa"].fillna(df['gpa'].mean(),inplace=True)
        df=df.replace({np.nan:None})
        return df.to_dict(orient="records")
    except Exception as e:
        print(e)
        return []