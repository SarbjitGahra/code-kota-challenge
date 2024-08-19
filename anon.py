import pandas as pd 

# I will be using factorize to anonymise the data  
def gnumeric_func (data, columns):
  data[columns] = data[columns].apply(lambda x: pd.factorize(x)[0])
  return data


# tested on a 2gb file
def main():
    df = pd.read_csv('input_data_faker.csv')
    column_list = ['first_name', 'last_name', 'address']
    # anonymise data
    df_data = gnumeric_func(df, column_list)


    # anonymise column names
    cols = {
    col: f"col{i + 1}" if col != "date_of_birth" else col
    for i, col in enumerate(df.columns)
        }

    out_df = df_data.rename(columns=cols)
    
    out_df.to_csv('output_data.csv')
if __name__ =='__main__':
    main()