import requests

#API to Get review statistics given a list of ISBN
def main():
        
    #KEY="NxHR0wNCivzIEefBextQ"(you cannot represent keys)
    #res = requests.get("https://www.goodreads.com/book/review_counts.json?isbns=1594489505&key=NxHR0wNCivzIEefBextQ")
        res = requests.get("https://www.goodreads.com/book/review_counts.json",params={"isbns":1594489505,"key":"NxHR0wNCivzIEefBextQ"})
        a=print(res.json())
