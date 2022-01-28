# I. Find the maximum value in a list

def maximun_value():
    the_list = [89, 93, 45, 20, 54, 93.4, 92, 39, 93]
    maximum = max(the_list)
    print("The maximum value in the list is", maximum)


maximun_value()


# II. Make each letter in a string lowercase
def lower_case():
    text = "WelcOME To MicroSOFT OFFICE, to contINUE, PURCHase the lATEST mIcrOSOft device"
    reviewed_text = text.casefold()
    print(reviewed_text)


lower_case()


# III. Sort a list of integers (using the inbuilt python method)
def list_sorting():
    integer_list = [89, 93, 45, 20, 54, 93.4, 92, 39, 93]
    # Sorting the list from lowest to highest
    integer_list.sort()
    print("The sorted list from lowest to highest is", integer_list)
    # Sorting in the reverse order
    integer_list.sort(reverse=True)
    print("The sorted list from highest to lowest is", integer_list)


list_sorting()
