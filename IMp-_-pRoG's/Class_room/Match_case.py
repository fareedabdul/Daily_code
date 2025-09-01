###############################################################################################################

# print("GREETINGS SIR/MADAM \n SELECT 1 FOR URDU \nSELECT 2 FOR hindi \nSELECT 1 FOR english \n")
# select = int(input("Enter the number for language:"))

# match select:
#     case 1:
#         print(f"you have selected {select} and the language is URDU")
#     case 2:
#         print(f"you have selected {select} and the language is hindi")
#     case 3:
#         print(f"you have selected {select} and the language is english")
#     case _:
#         print("please enter a valid number")

##################################################################################################################

color = input("Enter the color to validate you: ").lower()

match color:
    case "red":
        print("please Stop")
    case "yellow":
        print("Be ready to drive")
    case "green":
        print("You can drive ")
