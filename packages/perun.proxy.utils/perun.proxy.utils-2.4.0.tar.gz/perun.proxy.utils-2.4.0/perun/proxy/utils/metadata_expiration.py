import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    url = sys.argv[1]
    html = urlopen(url).read()
    closest_expiration = BeautifulSoup(html, "html.parser")

    if float(closest_expiration.text) >= 24:
        print("0 metadata_expiration - OK (" + closest_expiration.text + ")")
        return 0
    elif float(closest_expiration.text) >= 12:
        print("1 metadata_expiration - WARNING (" + closest_expiration.text + ")")
        return 1
    else:
        print("2 metadata_expiration - CRITICAL (" + closest_expiration.text + ")")
        return 2


if __name__ == "__main__":
    sys.exit(main())
