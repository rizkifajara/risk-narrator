import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from scipy import stats
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class PortfolioRiskCalculator:
    """
    Calculate comprehensive risk metrics for a portfolio
    """
    
    def __init__(self, returns_data: pd.DataFrame, weights: Dict[str, float], benchmark_ticker: str = "SPY"):
        """
        Initialize the risk calculator
        
        Args:
            returns_data: DataFrame with asset returns (columns=tickers, index=dates)
            weights: Dictionary mapping ticker to portfolio weight
            benchmark_ticker: Benchmark for beta calculation
        """
        self.returns_data = returns_data
        self.weights = weights
        self.benchmark_ticker = benchmark_ticker
        self.portfolio_returns = self._calculate_portfolio_returns()
        
    def _calculate_portfolio_returns(self) -> pd.Series:
        """Calculate portfolio returns based on weights"""
        weighted_returns = pd.Series(0, index=self.returns_data.index)
        
        for ticker, weight in self.weights.items():
            if ticker in self.returns_data.columns:
                weighted_returns += self.returns_data[ticker] * weight
                
        return weighted_returns
    
    def calculate_volatility(self, annualize: bool = True) -> float:
        """Calculate portfolio volatility"""
        vol = self.portfolio_returns.std()
        if annualize:
            vol *= np.sqrt(252)  # Annualize assuming 252 trading days
        return vol
    
    def calculate_sharpe_ratio(self, risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio"""
        excess_return = self.portfolio_returns.mean() * 252 - risk_free_rate
        volatility = self.calculate_volatility()
        return excess_return / volatility if volatility != 0 else 0
    
    def calculate_var(self, confidence_level: float = 0.05) -> float:
        """Calculate Value at Risk (VaR)"""
        return np.percentile(self.portfolio_returns, confidence_level * 100)
    
    def calculate_expected_shortfall(self, confidence_level: float = 0.05) -> float:
        """Calculate Expected Shortfall (Conditional VaR)"""
        var = self.calculate_var(confidence_level)
        return self.portfolio_returns[self.portfolio_returns <= var].mean()
    
    def calculate_beta(self) -> float:
        """Calculate portfolio beta relative to benchmark"""
        if self.benchmark_ticker not in self.returns_data.columns:
            return 1.0  # Default to market beta if benchmark not available
            
        benchmark_returns = self.returns_data[self.benchmark_ticker]
        
        # Remove NaN values
        clean_data = pd.DataFrame({
            'portfolio': self.portfolio_returns,
            'benchmark': benchmark_returns
        }).dropna()
        
        if len(clean_data) < 10:  # Need sufficient data points
            return 1.0
            
        covariance = clean_data['portfolio'].cov(clean_data['benchmark'])
        benchmark_variance = clean_data['benchmark'].var()
        
        return covariance / benchmark_variance if benchmark_variance != 0 else 1.0
    
    def calculate_max_drawdown(self) -> float:
        """Calculate maximum drawdown"""
        cumulative_returns = (1 + self.portfolio_returns).cumprod()
        rolling_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - rolling_max) / rolling_max
        return drawdown.min()
    
    def calculate_correlation_matrix(self) -> pd.DataFrame:
        """Calculate correlation matrix for all assets"""
        return self.returns_data.corr()
    
    def get_risk_metrics(self) -> Dict:
        """Get all risk metrics as a dictionary"""
        correlation_matrix = self.calculate_correlation_matrix()
        
        # Get top correlations (excluding self-correlations)
        correlations = {}
        assets = list(self.weights.keys())
        for i, asset1 in enumerate(assets):
            for asset2 in assets[i+1:]:
                if asset1 in correlation_matrix.columns and asset2 in correlation_matrix.columns:
                    corr_val = correlation_matrix.loc[asset1, asset2]
                    correlations[f"{asset1}-{asset2}"] = round(corr_val, 3)
        
        return {
            "portfolio_metrics": {
                "volatility": f"{self.calculate_volatility():.1%}",
                "beta": f"{self.calculate_beta():.2f}",
                "sharpe_ratio": f"{self.calculate_sharpe_ratio():.2f}",
                "value_at_risk": f"{self.calculate_var():.1%}",
                "expected_shortfall": f"{self.calculate_expected_shortfall():.1%}",
                "max_drawdown": f"{self.calculate_max_drawdown():.1%}"
            },
            "asset_composition": list(self.weights.keys()),
            "asset_weights": {k: f"{v:.1%}" for k, v in self.weights.items()},
            "correlation_matrix": correlations,
            "market_context": {
                "benchmark_comparison": self.benchmark_ticker,
                "time_period": f"{len(self.portfolio_returns)} trading days",
                "data_start": str(self.returns_data.index[0].date()),
                "data_end": str(self.returns_data.index[-1].date()),
                "analysis_date": datetime.now().strftime("%B %d, %Y"),
                "current_year": datetime.now().year
            }
        }