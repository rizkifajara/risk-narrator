#!/usr/bin/env python3
"""
Basic functionality test for RiskNarrator
Tests the core modules without requiring API keys
"""

import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_fetcher import MarketDataFetcher
from risk_calculator import PortfolioRiskCalculator

def test_data_fetching():
    """Test market data fetching functionality"""
    print("🔄 Testing market data fetching...")
    
    try:
        fetcher = MarketDataFetcher(period="6mo")
        
        # Test with a simple portfolio
        test_portfolio = {
            "AAPL": 0.5,
            "SPY": 0.5
        }
        
        prices, returns, ticker_info = fetcher.fetch_portfolio_data(test_portfolio)
        
        if not prices.empty and not returns.empty:
            print("✅ Data fetching successful!")
            print(f"   - Fetched {len(prices)} days of price data")
            print(f"   - Assets: {list(prices.columns)}")
            print(f"   - Date range: {prices.index[0].date()} to {prices.index[-1].date()}")
            return prices, returns
        else:
            print("❌ Data fetching failed - empty data")
            return None, None
            
    except Exception as e:
        print(f"❌ Data fetching failed: {str(e)}")
        return None, None

def test_risk_calculations(returns_data):
    """Test risk calculation functionality"""
    print("\n🔄 Testing risk calculations...")
    
    if returns_data is None:
        print("❌ Cannot test risk calculations - no data available")
        return None
    
    try:
        test_portfolio = {
            "AAPL": 0.5,
            "SPY": 0.5
        }
        
        calculator = PortfolioRiskCalculator(returns_data, test_portfolio)
        risk_metrics = calculator.get_risk_metrics()
        
        print("✅ Risk calculations successful!")
        print("   Portfolio Metrics:")
        for key, value in risk_metrics["portfolio_metrics"].items():
            print(f"   - {key.replace('_', ' ').title()}: {value}")
        
        return risk_metrics
        
    except Exception as e:
        print(f"❌ Risk calculations failed: {str(e)}")
        return None

def test_portfolio_validation():
    """Test portfolio input validation"""
    print("\n🔄 Testing portfolio validation...")
    
    try:
        fetcher = MarketDataFetcher()
        
        # Test valid tickers
        valid_tickers = ["AAPL", "SPY"]
        validation_results = fetcher.validate_tickers(valid_tickers)
        
        print("✅ Portfolio validation successful!")
        for ticker, is_valid in validation_results.items():
            status = "✅" if is_valid else "❌"
            print(f"   {status} {ticker}: {'Valid' if is_valid else 'Invalid'}")
        
        return validation_results
        
    except Exception as e:
        print(f"❌ Portfolio validation failed: {str(e)}")
        return None

def main():
    """Run all basic functionality tests"""
    print("🚀 RiskNarrator Basic Functionality Test")
    print("="*50)
    
    # Test data fetching
    prices_data, returns_data = test_data_fetching()
    
    # Test risk calculations
    risk_metrics = test_risk_calculations(returns_data)
    
    # Test validation
    validation_results = test_portfolio_validation()
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Summary:")
    
    tests_passed = 0
    total_tests = 3
    
    if prices_data is not None and returns_data is not None:
        print("✅ Data fetching: PASSED")
        tests_passed += 1
    else:
        print("❌ Data fetching: FAILED")
    
    if risk_metrics is not None:
        print("✅ Risk calculations: PASSED")
        tests_passed += 1
    else:
        print("❌ Risk calculations: FAILED")
    
    if validation_results is not None:
        print("✅ Portfolio validation: PASSED")
        tests_passed += 1
    else:
        print("❌ Portfolio validation: FAILED")
    
    print(f"\n🎯 Overall: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All basic functionality tests PASSED!")
        print("\n💡 Next steps:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Get Google API key: https://makersuite.google.com/app/apikey")
        print("   3. Create .env file with your API key")
        print("   4. Run the app: streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Check your internet connection and try again.")

if __name__ == "__main__":
    main()