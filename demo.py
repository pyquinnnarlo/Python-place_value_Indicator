# A number place value checker Program.
def place_value(location):

    location.split


    place_holder = {
        0 :'Unit', 
        1 :'Tens', 
        2 :'Hunderds', 
        3 :'Thousand'}

    if location[0]:
        try:
            print(location[0], "is in the {} place".format(place_holder[0]), "|", location, "\n")
            print(location[1], "is in the {} place".format(place_holder[1]), "|", location, "\n")
            print(location[2], "is in the {} place".format(place_holder[2]), "|", location, "\n")
            print(location[3], "is in the {} place".format(place_holder[3]), "|", location, "\n")

        except IndexError: # handling number out of range errors
            print("[+] Program counts up to Thousand places")


def main(): # calling the above function (place_value)

    # pass the number you want to check below.
    place_value("4") # counting unit place
    place_value("45") # counting tens place

    place_value("045") # counting hunderds places

    place_value("4051") # counting thousand places


main()




