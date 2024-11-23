#function to turn xlsx to csv
def xlsx_to_csv(file_path, new_name):
    import pandas as pd
    data_xls = pd.read_excel(file_path, index_col=None)
    data_xls.to_csv(new_name, encoding='utf-8')
