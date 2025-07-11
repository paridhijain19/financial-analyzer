import requests
import yfinance as yf
import pandas as pd

def test_network():
    print("🔍 Testing network connectivity...")
    
    # Test 1: Basic HTTP request
    try:
        response = requests.get('https://httpbin.org/get', timeout=10)
        print(f"✅ Basic HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Basic HTTP failed: {e}")
    
    # Test 2: Yahoo Finance directly
    try:
        response = requests.get('https://finance.yahoo.com', timeout=10)
        print(f"✅ Yahoo Finance: {response.status_code}")
    except Exception as e:
        print(f"❌ Yahoo Finance failed: {e}")
    
    # Test 3: YFinance with custom session
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        ticker = yf.Ticker('AAPL', session=session)
        data = ticker.history(period='5d')
        print(f"✅ YFinance with custom session: {len(data)} rows")
    except Exception as e:
        print(f"❌ YFinance failed: {e}")
    
    # Test 4: Alternative data source
    try:
        # Using a free API that doesn't require keys
        url = "https://api.coincap.io/v2/assets/bitcoin"  # Just to test connectivity
        response = requests.get(url, timeout=10)
        print(f"✅ Alternative API: {response.status_code}")
    except Exception as e:
        print(f"❌ Alternative API failed: {e}")

if __name__ == "__main__":
    test_network()