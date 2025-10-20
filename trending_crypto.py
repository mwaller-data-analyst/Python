#This code uses the Coingecko API to plot the top 10 trending crtypto coins over the past 24 hours.
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_trending_cryptos():
    # CoinGecko API endpoint for trending coins
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data from CoinGecko API")
        return None
    
    data = response.json()
    coins = data['coins']
    
    # Extract relevant data
    crypto_data = []
    for coin in coins[:10]:  # Limit to top 10 trending coins
        item = coin['item']
        crypto_data.append({
            'Name': item['name'],
            'Symbol': item['symbol'],
            'Price (USD)': item['data']['price'],
            'Price Change (24h)': item['data']['price_change_percentage_24h']['usd']
        })
    
    # Create DataFrame
    df = pd.DataFrame(crypto_data)
    return df

def plot_trending_cryptos(df):
    # Create a bar chart for price change percentage
    plt.figure(figsize=(12, 6))
    plt.bar(df['Name'], df['Price Change (24h)'], color='black')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('24h Price Change (%)')
    plt.title('Top 10 Trending Cryptocurrencies - 24h Price Change')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    # Fetch trending cryptocurrencies
    df = fetch_trending_cryptos()
    
    if df is not None:
        # Display the data
        print("\nTop 10 Trending Cryptocurrencies (", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "):")
        print(df[['Name', 'Symbol', 'Price (USD)', 'Price Change (24h)']])
        
        # Plot the data
        plot_trending_cryptos(df)

if __name__ == "__main__":
    main()