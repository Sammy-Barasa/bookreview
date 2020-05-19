import requests

#API to Get review statistics given a list of ISBN
def main():
        
    
    #res = requests.get("https://www.goodreads.com/book/review_counts.json?isbns=1594489505&key=KEY")
        res = requests.get("https://www.goodreads.com/book/review_counts.json",params={"isbns":1594489505,"key":KEY})
        a=print(res.json())
