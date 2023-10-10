import pyshorteners

def shorten_url(url):
    try:
        # Initialize the URL shortener
        s = pyshorteners.Shortener()

        # Shorten the URL
        short_url = s.tinyurl.short(url)

        return short_url

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Sample URL
sample_url = "https://www.example.com"

# Shorten the sample URL
shortened_url = shorten_url(sample_url)

# Print the sample URL and its shortened version
print("Original URL:", sample_url)
print("Shortened URL:", shortened_url)
