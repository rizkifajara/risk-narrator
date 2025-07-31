import google.generativeai as genai
import json
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class RiskReportGenerator:
    """
    Generate natural language risk reports using Google Gemini
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the report generator
        
        Args:
            api_key: Google API key (if None, will try to load from environment)
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        
        if not self.api_key:
            raise ValueError("Google API key not found. Please set GOOGLE_API_KEY environment variable.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
    def _create_system_prompt(self) -> str:
        """Create the system prompt for risk analysis"""
        return """You are a quantitative financial analyst with expertise in portfolio risk management. 

Your task is to analyze portfolio risk metrics and generate a comprehensive, professional risk assessment report. 

Your analysis should be:
- Accessible to investors with intermediate financial knowledge
- Technically accurate and based on quantitative metrics
- Actionable with specific recommendations
- Professional in tone while remaining clear and understandable

Structure your response with:
1. **Executive Risk Summary** (2-3 sentences overview)
2. **Key Risk Metrics Analysis** (interpret the main metrics)
3. **Portfolio Composition Assessment** (analyze diversification and concentration)
4. **Risk Optimization Recommendations** (specific actionable advice)
5. **Market Context** (how the portfolio relates to broader markets)

Focus on practical insights that help investors understand and manage their portfolio risk."""

    def _create_analysis_prompt(self, risk_data: Dict) -> str:
        """Create the analysis prompt with risk data"""
        current_date = risk_data.get("market_context", {}).get("analysis_date", "Today")
        
        return f"""Please analyze this portfolio risk data and provide a comprehensive risk assessment.

**IMPORTANT**: Today's date is {current_date}. Use this current date in your report header and throughout your analysis.

**Portfolio Risk Metrics:**
{json.dumps(risk_data, indent=2)}

Generate a professional risk assessment report following the structure outlined in your instructions. 
- Use the current date ({current_date}) in your report
- Be specific in your recommendations and explain the implications of each metric in practical terms
- Reference current market conditions and recent timeframe for the analysis"""

    def generate_risk_report(self, risk_data: Dict) -> str:
        """
        Generate a natural language risk report
        
        Args:
            risk_data: Dictionary containing portfolio risk metrics
            
        Returns:
            Generated risk report as string
        """
        try:
            # Create the conversation with system prompt and analysis request
            system_prompt = self._create_system_prompt()
            analysis_prompt = self._create_analysis_prompt(risk_data)
            
            # Combine prompts for Gemini
            full_prompt = f"{system_prompt}\n\n{analysis_prompt}"
            
            # Generate response
            response = self.model.generate_content(full_prompt)
            
            if response.text:
                return response.text
            else:
                return "Unable to generate risk report. Please try again."
                
        except Exception as e:
            return f"Error generating report: {str(e)}"
    
    def generate_executive_summary(self, risk_data: Dict) -> str:
        """
        Generate a brief executive summary of portfolio risks
        
        Args:
            risk_data: Dictionary containing portfolio risk metrics
            
        Returns:
            Brief executive summary
        """
        try:
            prompt = f"""Based on this portfolio data, provide a 2-3 sentence executive summary of the key risks:
            
{json.dumps(risk_data['portfolio_metrics'], indent=2)}

Focus only on the most critical risk factors and overall risk level. Be concise and direct."""

            response = self.model.generate_content(prompt)
            return response.text if response.text else "Unable to generate summary."
            
        except Exception as e:
            return f"Error generating summary: {str(e)}"
    
    def generate_recommendations(self, risk_data: Dict) -> str:
        """
        Generate specific portfolio optimization recommendations
        
        Args:
            risk_data: Dictionary containing portfolio risk metrics
            
        Returns:
            Specific recommendations for portfolio improvement
        """
        try:
            prompt = f"""Based on this portfolio analysis, provide 3-5 specific, actionable recommendations for risk optimization:

Portfolio Data:
{json.dumps(risk_data, indent=2)}

Format as a numbered list. Each recommendation should be specific and implementable. Focus on:
- Diversification improvements
- Risk reduction strategies  
- Asset allocation adjustments
- Specific asset additions/reductions"""

            response = self.model.generate_content(prompt)
            return response.text if response.text else "Unable to generate recommendations."
            
        except Exception as e:
            return f"Error generating recommendations: {str(e)}"