

class Keyword:
    def __init__(self, row_key, dataframe):
        self.row_key = row_key
        self.data = dataframe
    
class Filter:
    def __init__(self, keyword, targets, dataframe):
        self.keyword = keyword
        self.targets = targets
        self.data = dataframe
    
    def filter(self):
        filtered_df = self.data[self.data[self.keyword].isin(self.targets)]
        filtered_df = filtered_df.drop(columns=['reg_quotes', 'stock_distr', 'stock_isin_id'])
        
        return self.data
    
class FilterDataframes:
    def __init__(self):
        self.stock_id = None
        self.row_keys = []
    
    def create_keyword_class(self, keyword, dataframe):
        columns = dataframe.columns
        attributes = {col: 
            property(
                lambda self, col=col: 
                    self.data[self.data[keyword] == self.row_key][col].tolist()) 
            for col in columns
        }
        
        keyword_class = type('KeywordClass', (Keyword,), attributes)
        
        return keyword_class

    def by_stock_id(self, dataframe, stock_ids):
        if dataframe.empty or not stock_ids:
            return None
        
        filtered_df = Filter('stock_id', stock_ids, dataframe)
        filtered_df = filtered_df.filter()

        keyword_classes = {}

        for stock_id in stock_ids:
            keyword_class = self.create_keyword_class('stock_id', filtered_df[filtered_df['stock_id'] == stock_id])
            keyword_instance = keyword_class(row_key=stock_id, dataframe=filtered_df)
            keyword_classes[stock_id] = keyword_instance

        return keyword_classes

    def by_market_type(self, dataframe, market_types):
        if dataframe.empty or not market_types:
            return None

        filtered_df = Filter('market_type', market_types, dataframe)
        filtered_df = filtered_df.filter()

        keyword_classes = {}

        for market_t in market_types:
            keyword_class = self.create_keyword_class('market_type', filtered_df[filtered_df['market_type'] == market_t])
            keyword_instance = keyword_class(row_key=market_t, dataframe=filtered_df)
            keyword_classes[market_t] = keyword_instance

        return keyword_classes
