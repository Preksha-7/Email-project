import pickle

# Load the token.pickle file
with open('token.pickle', 'rb') as token_file:
    creds = pickle.load(token_file)

# Print the deserialized credentials
print("Token details:")
print(f"Token: {creds.token}")
print(f"Refresh Token: {creds.refresh_token}")
print(f"Token Expiry: {creds.expiry}")
print(f"Scopes: {creds.scopes}")
