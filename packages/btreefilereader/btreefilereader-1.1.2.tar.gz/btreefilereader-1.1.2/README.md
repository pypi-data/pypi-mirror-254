# btreefilereader

BTreeFileReader is a Python library for reading txt files containing all Brazil financial market data. The txt files are available on the B3 S.A. website.

This README contains two main sections, the first dedicated to users and the second dedicated to developers who want to contribute to the project.


## Users:

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install btreefilereader.

```bash
pip install btreefilereader
```

### Usage

#### 1. Reading txt file
---

To reader the txt file just need to call the `file_reader_txt()` funcion, set the path appropriately and filters, where:

  > path: is the path where your txt files are

  > stocks: is a list of Brazilian stock codes

 * **If just one file:**

    ```python
    from btreefilereader.core.reader_txt import FileReader
    
    df = FileReader.file_reader_txt(path='/path/to/file/file.txt', stocks=['STOCK_ID3', 'STOCK_ID11'])
    ```
  
  * **If more than one:**
  
    ```python
    from btreefilereader.core.reader_txt import FileReader
    
    df = FileReader.file_reader_txt(path='/path/to/file/*', stocks=['STOCK_ID3', 'STOCK_ID11'])
    ```
  
  The `df` object is a concatenated dataframe if there is more than one file to read.


  ## **Stocks id example:**
  
  #### The IBrX 100, at the moment this document is being written:

    ibrx_jan = ['RRRP3', 'ALOS3', 'ALPA4', 'ABEV3', 'ARZZ3', 'ASAI3', 'AURE3', 'AZUL4', 'B3SA3', 'BBSE3', 'BBDC3', 'BBDC4', 'BRAP4', 'BBAS3', 'BRKM5', 'BRFS3', 'BPAC11', 'CRFB3', 'BHIA3', 'CCRO3', 'CMIG4', 'CIEL3', 'COGN3', 'CSMG3', 'CPLE6', 'CSAN3', 'CPFE3', 'CMIN3', 'CVCB3', 'CYRE3', 'DXCO3', 'DIRR3', 'ECOR3', 'ELET3', 'ELET6', 'EMBR3', 'ENGI11', 'ENEV3', 'EGIE3', 'EQTL3', 'EZTC3', 'FLRY3', 'GGBR4', 'GOAU4', 'GOLL4', 'GMAT3', 'NTCO3', 'SOMA3', 'HAPV3', 'HYPE3', 'IGTI11', 'IRBR3', 'ITSA4', 'ITUB4', 'JBSS3', 'KLBN11', 'RENT3', 'LREN3', 'LWSA3', 'MDIA3', 'MGLU3', 'POMO4', 'MRFG3', 'BEEF3', 'MOVI3', 'MRVE3', 'MULT3', 'PCAR3', 'PETR3', 'PETR4', 'RECV3', 'PRIO3', 'PETZ3', 'PSSA3', 'RADL3', 'RAIZ4', 'RDOR3', 'RAIL3', 'SBSP3', 'SANB11', 'STBP3', 'SMTO3', 'CSNA3', 'SLCE3', 'SMFT3', 'SUZB3', 'TAEE11', 'VIVT3', 'TEND3', 'TIMS3', 'TOTS3', 'TRPL4', 'UGPA3', 'USIM5', 'VALE3', 'VAMO3', 'VBBR3', 'VIVA3', 'WEGE3', 'YDUQ3'] 

---

### **Terminal**

           trading_date        bdi_id     stock_id  market_type    company  ... price_or_amount  price_or_amount_corr_ind maturity_date  stock_quotation  price_or_amount_points
    2        2022-01-03  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    3        2022-01-03  Standard Lot   STOCK_ID11           10  STOCKCOMP  ...             0.0                      None           NaT                1                     0.0
    2354     2022-01-19  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    2355     2022-01-19  Standard Lot   STOCK_ID11           10  STOCKCOMP  ...             0.0                      None           NaT                1                     0.0
    2422     2022-02-21  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    ...             ...           ...      ...          ...        ...  ...             ...                       ...           ...              ...                     ...
    226531   2019-12-20  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    227529   2019-12-23  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    228591   2019-12-26  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    229612   2019-12-27  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0
    230830   2019-12-30  Standard Lot    STOCK_ID3           10  STOCK S/A  ...             0.0                      None           NaT                1                     0.0

    [601 rows x 23 columns]


## For Devs:


## License

[MIT](https://choosealicense.com/licenses/mit/)