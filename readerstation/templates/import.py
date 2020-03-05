import csv

def main():
    f=open("books.csv")
    reader=csv.reader(f)

    for isbn,title,author,year  in reader:
        db.execute("CREATE TABLE users (isbn, title,author,year)")
        db.commit()
        

