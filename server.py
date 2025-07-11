from mcp.server.fastmcp import FastMCP
from finance_crew import run_financial_analysis

# create FastMCP instance
mcp = FastMCP("financial-analyst")

@mcp.tool()
def analyze_stock(query: str) -> str:
    """
    Analyzes stock market data based on the query and generates executable Python code for analysis and visualization.
    Returns a formatted Python script ready for execution.
    
    The query is a string that must contain the stock symbol (e.g., TSLA, AAPL, NVDA, etc.), 
    timeframe (e.g., 1d, 1mo, 1y), and action to perform (e.g., plot, analyze, compare).

    Example queries:
    - "Show me Tesla's stock performance over the last 3 months"
    - "Compare Apple and Microsoft stocks for the past year"
    - "Analyze the trading volume of Amazon stock for the last month"

    Args:
        query (str): The query to analyze the stock market data.
    
    Returns:
        str: A nicely formatted python code as a string.
    """
    try:
        result = run_financial_analysis(query)
        return result
    except Exception as e:
        return f"Error: {e}"
    

@mcp.tool()
def save_code(code: str) -> str:
    """
    Expects a nicely formatted, working and executable python code as input in form of a string. 
    Save the given code to a file stock_analysis.py, make sure the code is a valid python file, nicely formatted and ready to execute.

    Args:
        code (str): The nicely formatted, working and executable python code as string.
    
    Returns:
        str: A message indicating the code was saved successfully.
    """
    try:
        with open('stock_analysis.py', 'w') as f:
            f.write(code)
        return "Code saved to stock_analysis.py"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def run_code_and_show_plot() -> str:
    """
    Run the code in stock_analysis.py and generate the plot
    """
    with open('stock_analysis.py', 'r') as f:
        exec(f.read())

# Run the server locally
if __name__ == "__main__":
    mcp.run(transport='stdio')




# from mcp.server.fastmcp import FastMCP
# from finance_crew import run_financial_analysis

# from pydantic import BaseModel
# from mcp.server.fastmcp import FastMCP
# from finance_crew import run_financial_analysis
# import matplotlib.pyplot as plt

# print("💡 Server file loaded.")  # Debug print

# mcp = FastMCP("financial-analyst")

# # Define input schemas
# class QueryInput(BaseModel):
#     query: str

# class CodeInput(BaseModel):
#     code: str

# @mcp.tool()
# def analyze_stock(input: QueryInput) -> str:
#     print("📈 analyze_stock called with:", input.query)
#     try:
#         result = run_financial_analysis(input.query)
#         return result
#     except Exception as e:
#         print("❌ Error in analyze_stock:", e)
#         return f"Error: {e}"

# @mcp.tool()
# def save_code(input: CodeInput) -> str:
#     print("💾 save_code called.")
#     try:
#         with open('stock_analysis.py', 'w') as f:
#             f.write(input.code)
#         return "Code saved to stock_analysis.py"
#     except Exception as e:
#         print("❌ Error in save_code:", e)
#         return f"Error: {e}"

# @mcp.tool()
# def run_code_and_show_plot() -> str:
#     print("📊 run_code_and_show_plot called.")
#     try:
#         exec(open('stock_analysis.py').read(), {"plt": plt})
#         return "Plot displayed successfully."
#     except Exception as e:
#         print("❌ Error in plot:", e)
#         return f"Error: {e}"

# # Run the server
# if __name__ == "__main__":
#     print("🚀 Starting MCP server...")
#     mcp.run(transport="stdio")
  