from yahoo_fin.stock_info import get_data


def get_data_x(ticker: str, start_date: str = None, end_date: str = None, interval: str = '1d'):
    data = get_data(ticker=ticker, start_date=start_date, end_date=end_date, interval=interval, index_as_date = True)
    return data
