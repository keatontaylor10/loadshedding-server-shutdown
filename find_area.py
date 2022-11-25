import app_requests
def main():
    print("Welcome to Setup!")
    areacode = input("Please type the name of your area: ")

    areas = app_requests.areaSearch(areacode)["areas"]
    for area in areas:
        print(area)


if __name__ == '__main__':
    main()