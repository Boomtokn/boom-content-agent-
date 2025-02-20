import requests
import tweepy

# Boom Token Details
BOOM_BSC_ADDRESS = "0xcd6A51559254030cA30C2FB2cbdf5c492e8Caf9c"
DEXSCREENER_API = f"https://api.dexscreener.com/latest/dex/tokens/{BOOM_BSC_ADDRESS}"
BSC_API_KEY = "YOUR_BSCSCAN_API_KEY"
BSC_TX_API = f"https://api.bscscan.com/api?module=account&action=txlist&address={BOOM_BSC_ADDRESS}&apikey={BSC_API_KEY}"

# Twitter API Keys
TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"
TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "
