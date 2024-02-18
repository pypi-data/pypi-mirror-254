import os
import glob
import tomllib
import pandas as pd
from pathlib import Path
from .models import MetaData


# class Keyword:
#     def __init__(self, row_key, dataframe):
#         self.row_key = row_key
#         self.data = dataframe
    
class Filter:
    def __init__(self, keyword, targets, dataframe):
        self.keyword = keyword
        self.targets = targets
        self.data = dataframe
    
    def filter(self):
        filtered_df = self.data[self.data[self.keyword].isin(self.targets)]
        filtered_df = filtered_df.drop(columns=['reg_quotes', 'stock_distr', 'stock_isin_id'])
        
        return filtered_df

class FileReader:
    def file_reader_txt(path, stocks = None):
        def read_txt(file, stocks, metadata):
            try:
                df = pd.read_fwf(file, names=list(metadata.keys()), widths=list(metadata.values()), header=None, encoding='latin-1')[1:-1]
                
                if stocks:
                    filtered_df = Filter('stock_id', stocks, df)
                    df = filtered_df.filter()
            
            except Exception as error:
                raise Exception(f'Error reading file: {file}. \n Error: {error}')
            
            return df
        
        def process_df(df, metadata):
            def process_columns(column, df, metadata):
                date_format = '%Y%m%d'
                
                if column in metadata.corrections['format']:
                    df[column] = df[column].fillna(-1).astype(int)
                    
                if 'bdi_id' == column:
                    df[column] = df[column].apply(lambda bdi_id: metadata.bdi_id.get(str(bdi_id), None))
                
                # if 'market_type' == column:
                #     df[column] = df[column].apply(lambda m_type: metadata.markets.get(str(m_type), None))
                
                if 'corr_ind' in column:
                    df[column] = df[column].apply(lambda indopc: metadata.indopc.get(str(indopc), None))
                    
                # if 'stock_specif' == column:
                #     df[column] = df[column].apply(lambda stock_s: metadata.stock_specif[str(stock_s)])
                
                if column.endswith('price') or 'volume' in column:
                    df[column] = df[column] / 100
                
                if 'maturity_date' == column:
                    df[column] = df[column].astype(int).astype(str)
                    
                    df[column] = pd.to_datetime(df[column], format=date_format, errors='coerce')
                
                if column.endswith('date'):
                    df[column] = pd.to_datetime(df[column], format=date_format)
            
            list(map(lambda column: process_columns(column, df, metadata), df.columns.values))
            
            return df
        
        files = glob.glob(path)
        
        if not files:
            raise Exception('No files to read.')
        
        try:
            data = tomllib.loads(Path(os.path.dirname(os.path.abspath(__file__))+'/metadata.toml').read_text(encoding='utf 8'))
            metadata = MetaData(data)
            
        except Exception as error:
            raise Exception(f'Error reading metadata. \n Error: {error}')
        
        dfs = list(map(lambda file: read_txt(file, stocks, metadata.metadata), files))

        dfs_processed = list(map(lambda df: process_df(df, metadata), dfs))

        return pd.concat(dfs_processed, axis=0)
    