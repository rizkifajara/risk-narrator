import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import json

# Import our custom modules
from risk_calculator import PortfolioRiskCalculator
from data_fetcher import MarketDataFetcher
from llm_integration import RiskReportGenerator
from styles import get_custom_css, get_custom_header, get_welcome_section, get_custom_footer

# Page configuration
st.set_page_config(
    page_title="RiskNarrator - Professional Portfolio Analysis",
    page_icon="favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
st.markdown(get_custom_css(), unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'portfolio_analyzed' not in st.session_state:
        st.session_state.portfolio_analyzed = False
    if 'risk_data' not in st.session_state:
        st.session_state.risk_data = None
    if 'returns_data' not in st.session_state:
        st.session_state.returns_data = None
    if 'prices_data' not in st.session_state:
        st.session_state.prices_data = None

def create_portfolio_input():
    """Create portfolio input interface"""
    st.sidebar.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.sidebar.markdown("### 📊 Portfolio Configuration")
    
    # Input method selection
    input_method = st.sidebar.radio(
        "Choose input method:",
        ["Manual Entry", "CSV Upload"]
    )
    
    portfolio = {}
    
    if input_method == "Manual Entry":
        st.sidebar.subheader("Enter Portfolio Holdings")
        
        # Number of assets
        num_assets = st.sidebar.number_input("Number of assets:", min_value=1, max_value=20, value=3)
        
        total_weight = 0
        for i in range(num_assets):
            col1, col2 = st.sidebar.columns(2)
            with col1:
                ticker = st.text_input(f"Ticker {i+1}:", key=f"ticker_{i}", placeholder="e.g., AAPL")
            with col2:
                weight = st.number_input(f"Weight % {i+1}:", min_value=0.0, max_value=100.0, value=0.0, key=f"weight_{i}")
            
            if ticker and weight > 0:
                portfolio[ticker.upper()] = weight / 100
                total_weight += weight
        
        # Show total weight
        if total_weight > 0:
            st.sidebar.write(f"Total Weight: {total_weight:.1f}%")
            if abs(total_weight - 100) > 0.1:
                st.sidebar.warning("⚠️ Weights should sum to 100%")
    
    else:  # CSV Upload
        st.sidebar.subheader("Upload Portfolio CSV")
        uploaded_file = st.sidebar.file_uploader(
            "Choose CSV file",
            type="csv",
            help="CSV should have columns: ticker, weight (as percentage)"
        )
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                if 'ticker' in df.columns and 'weight' in df.columns:
                    for _, row in df.iterrows():
                        ticker = str(row['ticker']).upper()
                        weight = float(row['weight']) / 100
                        portfolio[ticker] = weight
                    st.sidebar.success(f"✅ Loaded {len(portfolio)} assets")
                else:
                    st.sidebar.error("CSV must have 'ticker' and 'weight' columns")
            except Exception as e:
                st.sidebar.error(f"Error reading CSV: {str(e)}")
    
    # Analysis period
    st.sidebar.markdown("### ⏱️ Analysis Period")
    period = st.sidebar.selectbox(
        "Select time period:",
        ["1y", "2y", "3y", "5y"],
        help="Historical data period for analysis"
    )
    
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    return portfolio, period

def analyze_portfolio(portfolio, period):
    """Analyze portfolio and generate risk metrics"""
    if not portfolio:
        return None, None, None
    
    try:
        with st.spinner("Fetching market data..."):
            # Fetch data
            fetcher = MarketDataFetcher(period=period)
            prices, returns, ticker_info = fetcher.fetch_portfolio_data(portfolio)
            
            if returns.empty:
                st.error("Could not fetch data for any assets in portfolio")
                return None, None, None
        
        with st.spinner("Calculating risk metrics..."):
            # Calculate risk metrics
            calculator = PortfolioRiskCalculator(returns, portfolio)
            risk_data = calculator.get_risk_metrics()
            
        return risk_data, returns, prices
        
    except Exception as e:
        st.error(f"Error analyzing portfolio: {str(e)}")
        return None, None, None

def display_risk_metrics(risk_data):
    """Display risk metrics in a formatted way"""
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.markdown('''
    <div class="section-header">
        <span class="section-icon">📈</span>
        <h2 class="section-title">Portfolio Risk Metrics</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    metrics = risk_data["portfolio_metrics"]
    
    # Create columns for metrics
    col1, col2, col3 = st.columns(3)
    
    def create_metric_card(title, value, metric_type="neutral"):
        return f'''
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value metric-{metric_type}">{value}</div>
        </div>
        '''
    
    with col1:
        st.markdown(create_metric_card("Volatility", metrics["volatility"], "negative"), unsafe_allow_html=True)
        st.markdown(create_metric_card("Value at Risk (95%)", metrics["value_at_risk"], "negative"), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("Sharpe Ratio", metrics["sharpe_ratio"], "positive"), unsafe_allow_html=True)
        st.markdown(create_metric_card("Expected Shortfall", metrics["expected_shortfall"], "negative"), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("Beta", metrics["beta"], "neutral"), unsafe_allow_html=True)
        st.markdown(create_metric_card("Max Drawdown", metrics["max_drawdown"], "negative"), unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_visualizations(risk_data, returns_data, prices_data):
    """Create portfolio visualizations"""
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.markdown('''
    <div class="section-header">
        <span class="section-icon">📊</span>
        <h2 class="section-title">Portfolio Visualizations</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    # Portfolio allocation pie chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.markdown("#### Asset Allocation")
        weights_data = risk_data["asset_weights"]
        
        # Convert percentage strings back to floats for plotting
        weights_for_plot = {k: float(v.strip('%')) for k, v in weights_data.items()}
        
        fig_pie = px.pie(
            values=list(weights_for_plot.values()), 
            names=list(weights_for_plot.keys()),
            title="Portfolio Allocation",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_layout(
            font=dict(family="Inter", size=12),
            title_font_size=16,
            showlegend=True,
            height=400
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.markdown("#### Correlation Heatmap")
        if returns_data is not None and len(returns_data.columns) > 1:
            corr_matrix = returns_data.corr()
            
            fig_heatmap = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto",
                title="Asset Correlation Matrix",
                color_continuous_scale="RdBu_r"
            )
            fig_heatmap.update_layout(
                font=dict(family="Inter", size=12),
                title_font_size=16,
                height=400
            )
            st.plotly_chart(fig_heatmap, use_container_width=True)
        else:
            st.info("Correlation heatmap requires multiple assets")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Portfolio performance chart
    if prices_data is not None:
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        st.markdown("#### Portfolio Performance")
        
        # Calculate portfolio value over time
        portfolio_weights = {k: float(v.strip('%'))/100 for k, v in risk_data["asset_weights"].items()}
        
        # Normalize prices to start at 100
        normalized_prices = prices_data / prices_data.iloc[0] * 100
        
        # Calculate portfolio performance
        portfolio_performance = pd.Series(0, index=normalized_prices.index)
        for asset, weight in portfolio_weights.items():
            if asset in normalized_prices.columns:
                portfolio_performance += normalized_prices[asset] * weight
        
        fig_performance = go.Figure()
        fig_performance.add_trace(go.Scatter(
            x=portfolio_performance.index,
            y=portfolio_performance,
            mode='lines',
            name='Portfolio',
            line=dict(color='blue', width=2)
        ))
        
        # Add individual assets
        for asset in portfolio_weights.keys():
            if asset in normalized_prices.columns:
                fig_performance.add_trace(go.Scatter(
                    x=normalized_prices.index,
                    y=normalized_prices[asset],
                    mode='lines',
                    name=asset,
                    opacity=0.7
                ))
        
        fig_performance.update_layout(
            title="Portfolio vs Individual Assets Performance (Normalized to 100)",
            xaxis_title="Date",
            yaxis_title="Normalized Value",
            hovermode='x unified',
            font=dict(family="Inter", size=12),
            title_font_size=16,
            height=500,
            template="plotly_white"
        )
        
        st.plotly_chart(fig_performance, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def generate_ai_report(risk_data):
    """Generate AI-powered risk report"""
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.markdown('''
    <div class="section-header">
        <span class="section-icon">🤖</span>
        <h2 class="section-title">AI Risk Analysis Report</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    try:
        # Try to initialize with environment variable
        generator = RiskReportGenerator()
        
        with st.spinner("Generating AI risk analysis..."):
            report = generator.generate_risk_report(risk_data)
            
        # Display the AI report in a styled container
        st.markdown('<div class="ai-report">', unsafe_allow_html=True)
        st.markdown(report, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Generate recommendations in an expander
        with st.expander("💡 Detailed Recommendations", expanded=False):
            with st.spinner("Generating personalized recommendations..."):
                recommendations = generator.generate_recommendations(risk_data)
                st.markdown(recommendations)
                
        # Generate executive summary in an expander  
        with st.expander("📋 Executive Summary", expanded=False):
            with st.spinner("Generating executive summary..."):
                summary = generator.generate_executive_summary(risk_data)
                st.markdown(summary)
                
    except ValueError as e:
        # API key not found in environment
        st.warning("🔑 Google API Key Required")
        st.info("""
        **To enable AI-powered analysis:**
        1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Add it to your `.env` file: `GOOGLE_API_KEY=your_key_here`
        3. Restart the application
        
        Alternatively, enter your API key below for this session:
        """)
        
        # Fallback to manual input
        google_api_key = st.text_input(
            "Google API Key (session only):",
            type="password",
            help="This will only be used for the current session"
        )
        
        if google_api_key:
            try:
                with st.spinner("Generating AI risk analysis..."):
                    generator = RiskReportGenerator(api_key=google_api_key)
                    report = generator.generate_risk_report(risk_data)
                    
                # Display the AI report in a styled container
                st.markdown('<div class="ai-report">', unsafe_allow_html=True)
                st.markdown(report, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Generate recommendations
                with st.expander("💡 Detailed Recommendations", expanded=False):
                    recommendations = generator.generate_recommendations(risk_data)
                    st.markdown(recommendations)
                    
            except Exception as e:
                st.error(f"Error generating AI report: {str(e)}")
                
    except Exception as e:
        st.error(f"Error initializing AI service: {str(e)}")
        st.info("Please check your Google API key configuration.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def export_report(risk_data):
    """Export functionality for reports"""
    st.markdown('<div class="custom-section">', unsafe_allow_html=True)
    st.markdown('''
    <div class="section-header">
        <span class="section-icon">📥</span>
        <h2 class="section-title">Export Report</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Export JSON"):
            json_data = json.dumps(risk_data, indent=2)
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name=f"portfolio_risk_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
    
    with col2:
        if st.button("📊 Export CSV"):
            # Create a simple CSV with key metrics
            metrics_df = pd.DataFrame([risk_data["portfolio_metrics"]])
            csv_data = metrics_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=f"portfolio_metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    
    with col3:
        st.info("PDF export coming soon!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Custom header
    st.markdown(get_custom_header(), unsafe_allow_html=True)
    
    # Portfolio input
    portfolio, period = create_portfolio_input()
    
    # Analyze button
    if st.sidebar.button("🔍 Analyze Portfolio", type="primary", use_container_width=True):
        if portfolio:
            risk_data, returns_data, prices_data = analyze_portfolio(portfolio, period)
            if risk_data:
                st.session_state.portfolio_analyzed = True
                st.session_state.risk_data = risk_data
                st.session_state.returns_data = returns_data
                st.session_state.prices_data = prices_data
                st.success("✅ Portfolio analysis completed!")
        else:
            st.sidebar.warning("⚠️ Please enter a valid portfolio")
    
    # Display results if analysis completed
    if st.session_state.portfolio_analyzed and st.session_state.risk_data:
        # Display metrics
        display_risk_metrics(st.session_state.risk_data)
        
        # Create visualizations
        create_visualizations(
            st.session_state.risk_data, 
            st.session_state.returns_data, 
            st.session_state.prices_data
        )
        
        # Generate AI report
        generate_ai_report(st.session_state.risk_data)
        
        # Export functionality
        export_report(st.session_state.risk_data)
    
    else:
        # Welcome section - using Streamlit columns instead of HTML divs
        st.markdown("""
        <div class="welcome-section">
            <h2>🚀 Welcome to RiskNarrator</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">
                Transform complex portfolio risk metrics into clear, actionable insights using advanced AI technology.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Use Streamlit columns for better compatibility
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); 
                        color: white; padding: 2rem; border-radius: 8px; margin: 1rem 0; height: 100%;">
                <h3 style="color: #fecaca !important; margin-top: 0;">📊 How to Get Started</h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">📈 Enter your portfolio holdings</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">⏱️ Select analysis timeframe</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">🔍 Generate comprehensive risk metrics</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">🤖 Get AI-powered insights</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">📥 Export professional reports</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); 
                        color: white; padding: 2rem; border-radius: 8px; margin: 1rem 0; height: 100%;">
                <h3 style="color: #fecaca !important; margin-top: 0;">⚡ Key Features</h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">🎯 Advanced risk calculations</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">📊 Interactive visualizations</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">🤖 Natural language reports</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">💼 Professional export formats</li>
                    <li style="margin: 0.75rem 0; color: #f1f5f9;">🔄 Real-time market data</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Sample portfolio section using Streamlit columns
        st.markdown("""
        <div style="background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); 
                    color: white; padding: 2rem; border-radius: 8px; margin: 2rem 0;">
            <h4 style="margin: 0 0 1.5rem 0; color: #fecaca; text-align: center;">💡 Sample Portfolio to Try:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Sample portfolio using three columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); 
                        color: white; padding: 1.5rem; border-radius: 8px; text-align: center; margin-top: -1rem;">
                <strong style="font-size: 1.2rem;">AAPL</strong><br>
                <span style="font-size: 1.5rem; font-weight: bold;">40%</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); 
                        color: white; padding: 1.5rem; border-radius: 8px; text-align: center; margin-top: -1rem;">
                <strong style="font-size: 1.2rem;">SPY</strong><br>
                <span style="font-size: 1.5rem; font-weight: bold;">35%</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); 
                        color: white; padding: 1.5rem; border-radius: 8px; text-align: center; margin-top: -1rem;">
                <strong style="font-size: 1.2rem;">BTC-USD</strong><br>
                <span style="font-size: 1.5rem; font-weight: bold;">25%</span>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown(get_custom_footer(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()