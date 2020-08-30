import requests
def title():
    print("*****************************")
    print("* Website headers analyzer  *")
    print("*        written by         *")
    print("*       Azan Shahid         *")
    print("*   github.com/azan121468   *")
    print("*****************************")
def main():
    title()
    try:
        website = input("Enter website : ") or "https://www.google.com"
        r = requests.get(website)
        for i in r.headers:
            print(f"{i} : {r.headers[i]}")
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
        print("URL should look like")
        print("http://www.example.com")
if __name__=="__main__":
    main()
