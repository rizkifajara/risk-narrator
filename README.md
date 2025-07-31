# RiskNarrator 🛡️

**Professional AI-Powered Portfolio Risk Analysis**

RiskNarrator is a sophisticated web application that transforms complex portfolio risk metrics into clear, actionable insights using advanced AI technology. Built with Streamlit and powered by Google Gemini AI, it provides comprehensive portfolio risk analysis with professional visualizations and natural language reports.

## ✨ Features

### 📊 Core Analytics
- **Advanced Risk Calculations**: Volatility, Sharpe ratio, Value at Risk (VaR), Expected Shortfall, Beta, and Maximum Drawdown
- **Portfolio Optimization**: Comprehensive risk-return analysis with benchmark comparisons
- **Interactive Visualizations**: Dynamic charts, correlation heatmaps, and performance tracking
- **Historical Analysis**: Multiple timeframe analysis (1-5 years) with real-time market data

### 🤖 AI-Powered Insights
- **Natural Language Reports**: AI-generated risk analysis in plain English
- **Personalized Recommendations**: Tailored investment advice based on portfolio composition
- **Executive Summaries**: Concise overviews for stakeholder presentations
- **Risk Interpretation**: Complex metrics explained in accessible language

### 💼 Professional Features
- **Multiple Input Methods**: Manual entry or CSV upload for portfolio data
- **Export Capabilities**: JSON and CSV export for further analysis
- **Professional UI**: Custom-designed interface with red branding theme
- **Real-time Data**: Integration with Yahoo Finance for current market data

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google API key for Gemini AI (optional, for AI features)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd risk-narrator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional, for AI features)
   ```bash
   # Create a .env file in the project root
   echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
   ```
   
   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 📋 Usage

### Portfolio Input Methods

#### Manual Entry
1. Select "Manual Entry" in the sidebar
2. Specify the number of assets (1-20)
3. Enter ticker symbols (e.g., AAPL, SPY, BTC-USD)
4. Set allocation percentages (must sum to 100%)

#### CSV Upload
1. Select "CSV Upload" in the sidebar
2. Prepare a CSV file with columns: `ticker`, `weight`
3. Example CSV format:
   ```csv
   ticker,weight
   AAPL,40
   SPY,35
   BTC-USD,25
   ```
4. Upload the file using the file uploader

### Analysis Options
- **Time Period**: Choose from 1, 2, 3, or 5-year analysis periods
- **Benchmark**: Default comparison against SPY (S&P 500)

### Sample Portfolio
Try the application with this sample portfolio:
- **AAPL**: 40% (Apple Inc.)
- **SPY**: 35% (S&P 500 ETF)
- **BTC-USD**: 25% (Bitcoin)

## 📊 Risk Metrics Explained

### Volatility
Measures the degree of variation in portfolio returns. Higher volatility indicates greater price fluctuations and risk.

### Sharpe Ratio
Risk-adjusted return metric. Higher values indicate better risk-adjusted performance (>1.0 is generally considered good).

### Value at Risk (VaR)
Maximum expected loss over a given time period at a 95% confidence level.

### Expected Shortfall
Average loss expected beyond the VaR threshold, providing insight into tail risks.

### Beta
Measure of portfolio sensitivity to market movements (Beta = 1 means portfolio moves with market).

### Maximum Drawdown
Largest peak-to-trough decline during the analysis period, indicating worst-case scenario losses.

## 🤖 AI Features

The AI analysis requires a Google API key and provides:
- **Risk Profile Summary**: Plain-language explanation of your portfolio's risk characteristics
- **Detailed Recommendations**: Specific suggestions for portfolio optimization
- **Market Context**: How your portfolio compares to market benchmarks
- **Actionable Insights**: Concrete steps to improve risk-adjusted returns

## 🏗️ Architecture

### Project Structure
```
risk-narrator/
├── app.py                 # Main Streamlit application
├── risk_calculator.py     # Portfolio risk calculation engine
├── data_fetcher.py       # Market data retrieval via Yahoo Finance
├── llm_integration.py    # Google Gemini AI integration
├── styles.py            # Custom CSS styling and UI components
├── requirements.txt     # Python dependencies
├── favicon.ico         # Application favicon
├── logo.png           # RiskNarrator logo
└── README.md          # This documentation
```

### Core Components

#### `PortfolioRiskCalculator`
- Calculates comprehensive risk metrics
- Handles portfolio-level analysis
- Provides statistical computations

#### `MarketDataFetcher`
- Retrieves real-time market data via Yahoo Finance
- Handles multiple asset types (stocks, ETFs, crypto)
- Data validation and error handling

#### `RiskReportGenerator`
- Google Gemini AI integration
- Natural language report generation
- Personalized recommendations engine

#### Custom Styling System
- Professional red-themed design
- Material Icons integration
- Responsive layout optimization
- Streamlit UI overrides

## 🔧 Configuration

### Environment Variables
```bash
# Google AI API Key (optional)
GOOGLE_API_KEY=your_api_key_here
```

### Supported Asset Types
- **Stocks**: Any ticker available on Yahoo Finance (e.g., AAPL, MSFT, GOOGL)
- **ETFs**: Exchange-traded funds (e.g., SPY, QQQ, VTI)
- **Crypto**: Major cryptocurrencies (e.g., BTC-USD, ETH-USD)
- **International**: Global markets with appropriate suffixes

## 🔒 API Keys and Security

### Google Gemini AI Setup
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add to `.env` file or enter during runtime
4. API key is used only for AI report generation

### Data Privacy
- No portfolio data is stored permanently
- All calculations performed locally
- API calls to Google Gemini are for analysis only
- Market data retrieved from public Yahoo Finance API

## 🛠️ Development

### Dependencies
```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
yfinance>=0.2.18
plotly>=5.15.0
google-generativeai>=0.3.0
scipy>=1.11.0
python-dotenv>=1.0.0
```

### Running in Development Mode
```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
streamlit run app.py --server.runOnSave true

# Run with custom port
streamlit run app.py --server.port 8502
```

### Custom Styling
The application uses a comprehensive custom CSS system in `styles.py`:
- Professional red branding theme
- Material Design components
- Responsive layouts
- Custom metric cards and visualizations

## 📈 Performance Considerations

### Data Fetching
- Market data cached during session
- Efficient API calls to Yahoo Finance
- Error handling for unavailable tickers

### AI Processing
- Optional AI features (works without API key)
- Streaming responses for better UX
- Fallback modes for API failures

### UI Optimization
- Custom CSS for improved performance
- Optimized chart rendering
- Responsive design for all screen sizes

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Install dependencies: `pip install -r requirements.txt`
4. Make your changes
5. Test thoroughly
6. Submit a pull request

### Code Style
- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Add docstrings for all functions
- Maintain consistent commenting

## 🆘 Troubleshooting

### Common Issues


#### Yahoo Finance data not loading
- Check internet connection
- Verify ticker symbols are correct
- Try different time periods

#### AI features not working
- Verify Google API key is set correctly
- Check API key permissions
- Ensure sufficient API quota


### Support
For issues and questions:
1. Check this README
2. Review error messages carefully
3. Verify all dependencies are installed
4. Check environment variable configuration

## 🎯 Roadmap

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ using Python, Streamlit, and Google Gemini AI**

© 2025 RiskNarrator - Professional Portfolio Risk Analysis