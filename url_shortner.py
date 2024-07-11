import pyshorteners



url = "https://www.bing.com/search?pglt=41&q=gpt&cvid=90e64b19c1d4462facb071e2c3cea5bb&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgyNDE1ajBqMagCCLACAQ&FORM=ANNTA1&PC=U531"
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print("Short URL:", short_url)

