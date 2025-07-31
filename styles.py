"""
Custom styling for RiskNarrator to create a professional, non-Streamlit appearance
"""

def get_custom_css():
    """Return custom CSS to override Streamlit styling"""
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    .stAppViewContainer > .main .block-container {padding-top: 2rem;}
    .stAppViewContainer > .main {background-color: #f8fafc;}
    
    /* Custom root variables - RiskNarrator Red Branding */
    :root {
        --primary-color: #dc2626;
        --primary-hover: #b91c1c;
        --primary-light: #fecaca;
        --secondary-color: #64748b;
        --success-color: #059669;
        --warning-color: #d97706;
        --error-color: #dc2626;
        --bg-primary: #ffffff;
        --bg-secondary: #fef7f7;
        --bg-tertiary: #fee2e2;
        --text-primary: #1e293b;
        --text-secondary: #64748b;
        --border-color: #fecaca;
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        --border-radius: 8px;
    }
    
    /* Reset all Streamlit fonts */
    .stApp * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif !important;
    }
    
    /* Ensure Material Icons font is available for icons */
    [data-testid="stIconMaterial"],
    .st-emotion-cache-pd6qx2,
    .ejhh0er0 {
        font-family: 'Material Icons' !important;
        font-weight: normal !important;
        font-style: normal !important;
        font-size: 24px !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        display: inline-block !important;
        white-space: nowrap !important;
        word-wrap: normal !important;
        direction: ltr !important;
        -webkit-font-feature-settings: 'liga' !important;
        -webkit-font-smoothing: antialiased !important;
    }
    
    /* Main container styling */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
        background-color: var(--bg-secondary);
    }
    
    /* Custom header */
    .custom-header {
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
        color: white;
        padding: 2rem 3rem;
        margin: -2rem -3rem 3rem -3rem;
        border-radius: 0 0 16px 16px;
        box-shadow: var(--shadow-lg);
    }
    
    .custom-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(45deg, #ffffff, #e0e7ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .custom-header p {
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-weight: 400;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: var(--bg-primary);
        border-right: 2px solid var(--border-color);
        padding: 2rem 1rem;
    }

    /* Professional sidebar toggle button styling */
    button[data-testid="collapsedControl"] {
        background: linear-gradient(135deg, var(--bg-primary), #f8fafc) !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 8px !important;
        width: 40px !important;
        height: 40px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
        cursor: pointer !important;
        position: fixed !important;
        top: 1rem !important;
        left: 1rem !important;
        z-index: 1000 !important;
    }
    
    button[data-testid="collapsedControl"]:hover {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-hover)) !important;
        border-color: var(--primary-color) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3) !important;
    }
    
    button[data-testid="collapsedControl"]:active {
        transform: translateY(0) !important;
        box-shadow: 0 2px 4px rgba(220, 38, 38, 0.2) !important;
    }
    
    /* Style the Material Icon inside the button */
    button[data-testid="collapsedControl"] [data-testid="stIconMaterial"] {
        color: var(--text-secondary) !important;
        font-size: 20px !important;
        transition: color 0.3s ease !important;
    }
    
    button[data-testid="collapsedControl"]:hover [data-testid="stIconMaterial"] {
        color: white !important;
    }
    
    /* Ensure proper positioning and accessibility */
    button[data-testid="collapsedControl"]:focus {
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.3) !important;
    }

    /* Fix sidebar content styling */
    .sidebar .element-container {
        background-color: var(--bg-primary);
        border-radius: var(--border-radius);
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-sm);
    }
    
    .css-1rs6os:hover {
        background-color: var(--bg-tertiary) !important;
        border-color: var(--primary-color) !important;
        color: var(--primary-color) !important;
    }
    
    /* Custom metric cards */
    .metric-card {
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-md);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
        border-color: var(--primary-color);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), #ef4444);
    }
    
    .metric-title {
        font-size: 0.875rem;
        font-weight: 500;
        color: var(--text-secondary);
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.025em;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0;
    }
    
    .metric-positive {
        color: var(--success-color);
    }
    
    .metric-negative {
        color: var(--error-color);
    }
    
    .metric-neutral {
        color: var(--primary-color);
    }
    
    /* Custom section styling */
    .custom-section {
        background: var(--bg-primary);
        border-radius: var(--border-radius);
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-md);
    }
    
    .section-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid var(--border-color);
    }
    
    .section-icon {
        font-size: 1.5rem;
        margin-right: 0.75rem;
        color: var(--primary-color);
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin: 0;
    }
    
    /* AI report styling */
    .ai-report {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border: 2px solid var(--primary-color);
        border-radius: var(--border-radius);
        padding: 2rem;
        margin: 2rem 0;
        position: relative;
        box-shadow: var(--shadow-lg);
        line-height: 1.6;
    }
    
    .ai-report::before {
        content: '🤖';
        position: absolute;
        top: -12px;
        left: 20px;
        background: var(--primary-color);
        color: white;
        padding: 8px 12px;
        border-radius: 20px;
        font-size: 1rem;
    }
    
    /* AI report typography */
    .ai-report h1,
    .ai-report h2,
    .ai-report h3,
    .ai-report h4,
    .ai-report h5,
    .ai-report h6 {
        color: var(--primary-color) !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
        font-weight: 600 !important;
        line-height: 1.3 !important;
    }
    
    .ai-report h1 {
        font-size: 1.875rem !important;
        margin-top: 0 !important;
    }
    
    .ai-report h2 {
        font-size: 1.5rem !important;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.5rem;
    }
    
    .ai-report h3 {
        font-size: 1.25rem !important;
    }
    
    .ai-report p {
        margin: 1rem 0 !important;
        color: var(--text-primary) !important;
        line-height: 1.6 !important;
    }
    
    .ai-report strong {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    /* Fix list styling in AI report */
    .ai-report ul,
    .ai-report ol {
        margin: 1rem 0 !important;
        padding-left: 2rem !important;
        color: var(--text-primary) !important;
    }
    
    .ai-report li {
        margin: 0.5rem 0 !important;
        color: var(--text-primary) !important;
        line-height: 1.6 !important;
        display: list-item !important;
        list-style-position: outside !important;
    }
    
    .ai-report li::marker {
        color: var(--primary-color) !important;
    }
    
    .ai-report li p {
        display: inline !important;
        margin: 0 !important;
    }
    
    .ai-report li strong {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    
    /* Blockquotes in AI report */
    .ai-report blockquote {
        border-left: 4px solid var(--primary-color);
        padding-left: 1rem;
        margin: 1rem 0;
        color: var(--text-secondary) !important;
        font-style: italic;
        background: rgba(37, 99, 235, 0.05);
        padding: 1rem;
        border-radius: 4px;
    }
    
    /* Code blocks in AI report */
    .ai-report code {
        background: var(--bg-tertiary);
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-family: 'Monaco', 'Consolas', monospace;
        font-size: 0.875rem;
    }
    
    .ai-report pre {
        background: var(--bg-tertiary);
        padding: 1rem;
        border-radius: var(--border-radius);
        overflow-x: auto;
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-hover));
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 2rem;
        font-weight: 500;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-md);
        text-transform: uppercase;
        letter-spacing: 0.025em;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
        background: linear-gradient(135deg, var(--primary-hover), #991b1b);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 2px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--bg-primary);
        color: var(--text-primary);
        font-size: 1rem;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgb(220 38 38 / 0.1);
        outline: none;
    }
    
    /* File uploader styling */
    .stFileUploader > div {
        border: 2px dashed var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--bg-primary);
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div:hover {
        border-color: var(--primary-color);
        background-color: #fef2f2;
    }
    
    /* Chart container styling */
    .plot-container {
        background: var(--bg-primary);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-md);
        margin: 1rem 0;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        font-weight: 500;
        color: var(--text-primary);
    }
    
    .streamlit-expanderContent {
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-top: none;
        border-radius: 0 0 var(--border-radius) var(--border-radius);
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background-color: #ecfdf5;
        border: 1px solid #10b981;
        border-radius: var(--border-radius);
        color: #047857;
    }
    
    .stError {
        background-color: #fef2f2;
        border: 1px solid #ef4444;
        border-radius: var(--border-radius);
        color: #dc2626;
    }
    
    .stWarning {
        background-color: #fffbeb;
        border: 1px solid #f59e0b;
        border-radius: var(--border-radius);
        color: #d97706;
    }
    
    .stInfo {
        background-color: #eff6ff;
        border: 1px solid #3b82f6;
        border-radius: var(--border-radius);
        color: var(--primary-color);
    }
    
    /* Welcome section styling */
    .welcome-section {
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
        color: white;
        padding: 3rem;
        border-radius: var(--border-radius);
        margin: 2rem 0;
        box-shadow: var(--shadow-lg);
    }
    
    .welcome-section h2 {
        color: white !important;
        margin-top: 0;
        font-weight: 600;
    }
    
    .welcome-section h3 {
        color: #fecaca !important;
        font-weight: 500;
        margin-bottom: 1rem !important;
    }
    
    .welcome-section h4 {
        color: #fecaca !important;
        font-weight: 500;
        margin: 0 0 1rem 0 !important;
    }
    
    .welcome-section ul li {
        margin: 0.5rem 0;
        color: #f1f5f9 !important;
        padding: 0.25rem 0;
    }
    
    .welcome-section p {
        color: white !important;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .welcome-section strong {
        color: white !important;
        font-weight: 600;
    }
    
    /* Ensure flexbox works properly in Streamlit */
    .welcome-section [style*="display: flex"] {
        display: flex !important;
    }
    
    .welcome-section [style*="flex-wrap: wrap"] {
        flex-wrap: wrap !important;
    }
    
    /* Footer styling */
    .custom-footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 1px solid var(--border-color);
        color: var(--text-secondary);
        font-size: 0.875rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }
        
        .custom-header {
            margin: -1rem -1rem 2rem -1rem;
            padding: 1.5rem;
        }
        
        .custom-header h1 {
            font-size: 2rem;
        }
        
        .metric-card {
            padding: 1rem;
        }
        
        .metric-value {
            font-size: 1.5rem;
        }
    }
    
    /* Loading spinner styling */
    .stSpinner > div {
        border-color: var(--primary-color) transparent transparent transparent;
    }
    
    /* Dataframe styling */
    .dataframe {
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--shadow-sm);
    }
    
    .dataframe th {
        background-color: var(--bg-tertiary);
        color: var(--text-primary);
        font-weight: 600;
        padding: 1rem;
        border-bottom: 2px solid var(--border-color);
    }
    
    .dataframe td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid var(--border-color);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: var(--bg-primary);
        border-radius: var(--border-radius);
        padding: 4px;
        border: 1px solid var(--border-color);
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: calc(var(--border-radius) - 4px);
        padding: 12px 24px;
        font-weight: 500;
        color: var(--text-secondary);
        border: none;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color);
        color: white;
        box-shadow: var(--shadow-sm);
    }
    </style>
    """

def get_custom_header():
    """Return custom header HTML"""
    return """
    <div class="custom-header">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="width: 48px; height: 48px; border-radius: 8px; background: rgba(255,255,255,0.15); 
                        display: flex; align-items: center; justify-content: center; font-size: 24px;">
                🛡️
            </div>
            <div>
                <h1 style="margin: 0;">RiskNarrator</h1>
                <p style="margin: 0.5rem 0 0 0;">Professional AI-Powered Portfolio Risk Analysis</p>
            </div>
        </div>
    </div>
    """

def get_welcome_section():
    """Return welcome section HTML"""
    return """
    <div class="welcome-section">
        <h2>🚀 Welcome to RiskNarrator</h2>
        <p style="font-size: 1.1rem; margin-bottom: 2rem;">
            Transform complex portfolio risk metrics into clear, actionable insights using advanced AI technology.
        </p>
        
        <div style="display: flex; flex-wrap: wrap; gap: 2rem; margin-top: 2rem;">
            <div style="flex: 1; min-width: 300px;">
                <h3>📊 How to Get Started</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin: 0.5rem 0;">📈 Enter your portfolio holdings</li>
                    <li style="margin: 0.5rem 0;">⏱️ Select analysis timeframe</li>
                    <li style="margin: 0.5rem 0;">🔍 Generate comprehensive risk metrics</li>
                    <li style="margin: 0.5rem 0;">🤖 Get AI-powered insights</li>
                    <li style="margin: 0.5rem 0;">📥 Export professional reports</li>
                </ul>
            </div>
            
            <div style="flex: 1; min-width: 300px;">
                <h3>⚡ Key Features</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin: 0.5rem 0;">🎯 Advanced risk calculations</li>
                    <li style="margin: 0.5rem 0;">📊 Interactive visualizations</li>
                    <li style="margin: 0.5rem 0;">🤖 Natural language reports</li>
                    <li style="margin: 0.5rem 0;">💼 Professional export formats</li>
                    <li style="margin: 0.5rem 0;">🔄 Real-time market data</li>
                </ul>
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">
            <h4 style="margin: 0 0 1rem 0; color: #fecaca;">💡 Sample Portfolio to Try:</h4>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem; text-align: center;">
                <div style="flex: 1; min-width: 100px;"><strong>AAPL</strong><br>40%</div>
                <div style="flex: 1; min-width: 100px;"><strong>SPY</strong><br>35%</div>
                <div style="flex: 1; min-width: 100px;"><strong>BTC-USD</strong><br>25%</div>
            </div>
        </div>
    </div>
    """

def get_custom_footer():
    """Return custom footer HTML"""
    return """
    <div class="custom-footer">
        <p>Built with ❤️ using Python, Streamlit, and Google Gemini AI</p>
        <p>© 2025 RiskNarrator - Professional Portfolio Risk Analysis</p>
    </div>
    """