import yfinance as yf
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class MarketDataFetcher:
    """
    Fetch and process market data for portfolio analysis
    """
    
    def __init__(self, period: str = "1y"):
        """
        Initialize data fetcher
        
        Args:
            period: Data period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        """
        self.period = period
        
    def fetch_price_data(self, tickers: List[str]) -> pd.DataFrame:
        """
        Fetch historical price data for given tickers
        
        Args:
            tickers: List of ticker symbols
            
        Returns:
            DataFrame with adjusted close prices
        """
        try:
            # Add benchmark if not already included
            all_tickers = list(set(tickers + ["SPY"]))  # SPY as default benchmark
            
            # Fetch data
            data = yf.download(all_tickers, period=self.period, group_by='ticker', auto_adjust=True, progress=False)
            
            # Extract adjusted close prices
            if len(all_tickers) == 1:
                prices = data[['Close']].copy()
                prices.columns = all_tickers
            else:
                prices = pd.DataFrame()
                for ticker in all_tickers:
                    try:
                        if isinstance(data.columns, pd.MultiIndex):
                            prices[ticker] = data[(ticker, 'Close')]
                        else:
                            prices[ticker] = data['Close']
                    except KeyError:
                        print(f"Warning: Could not fetch data for {ticker}")
                        continue
            
            # Remove any columns with all NaN values
            prices = prices.dropna(axis=1, how='all')
            
            # Forward fill missing values and then drop remaining NaN
            prices = prices.fillna(method='ffill').dropna()
            
            return prices
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
    
    def calculate_returns(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate daily returns from price data
        
        Args:
            prices: DataFrame with price data
            
        Returns:
            DataFrame with daily returns
        """
        return prices.pct_change().dropna()
    
    def validate_tickers(self, tickers: List[str]) -> Dict[str, bool]:
        """
        Validate if tickers exist and have data
        
        Args:
            tickers: List of ticker symbols to validate
            
        Returns:
            Dictionary mapping ticker to validation status
        """
        validation_results = {}
        
        for ticker in tickers:
            try:
                # Try to fetch just 1 day of data to validate
                data = yf.download(ticker, period="5d", progress=False)
                validation_results[ticker] = not data.empty
            except:
                validation_results[ticker] = False
                
        return validation_results
    
    def get_ticker_info(self, ticker: str) -> Dict:
        """
        Get basic information about a ticker
        
        Args:
            ticker: Ticker symbol
            
        Returns:
            Dictionary with ticker information
        """
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            return {
                "name": info.get("longName", ticker),
                "sector": info.get("sector", "Unknown"),
                "industry": info.get("industry", "Unknown"),
                "market_cap": info.get("marketCap", 0),
                "currency": info.get("currency", "USD")
            }
        except:
            return {
                "name": ticker,
                "sector": "Unknown",
                "industry": "Unknown", 
                "market_cap": 0,
                "currency": "USD"
            }
    
    def fetch_portfolio_data(self, portfolio: Dict[str, float]) -> tuple:
        """
        Fetch all necessary data for portfolio analysis
        
        Args:
            portfolio: Dictionary mapping ticker to weight
            
        Returns:
            Tuple of (prices_df, returns_df, ticker_info)
        """
        tickers = list(portfolio.keys())
        
        # Validate tickers
        validation = self.validate_tickers(tickers)
        valid_tickers = [t for t, v in validation.items() if v]
        
        if not valid_tickers:
            raise ValueError("No valid tickers found in portfolio")
        
        # Fetch price data
        prices = self.fetch_price_data(valid_tickers)
        
        if prices.empty:
            raise ValueError("No price data could be fetched")
        
        # Calculate returns
        returns = self.calculate_returns(prices)
        
        # Get ticker information
        ticker_info = {}
        for ticker in valid_tickers:
            ticker_info[ticker] = self.get_ticker_info(ticker)
        
        return prices, returns, ticker_info