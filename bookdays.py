mode = int(input("Hello. Insert the desired operation: 0 for default values, 1 for a custom one.\n"))
if mode == int(0):
    pages = int(input("Insert the number of pages of your book:\n"))
    threedays = '{:.0f}'.format(pages/3)
    sevendays = '{:.0f}'.format(pages/7)
    tendays = '{:.0f}'.format(pages/10)
    print("To finish your book in:\n")
    print("Three days: You will need to read",threedays,"pages per day.")
    print("Seven days:",sevendays,"pages per day.")
    print("Ten days:",tendays,"pages per day.\n")
elif mode == int(1): 
    pages = int(input("Insert the number of pages of your book:\n"))
    days = int(input("Inset the number of days you want to read:\n"))
    ppd = '{:.0f}'.format(pages/days)
    print("To finish your book in", days,"days, you will need to read",ppd,"pages per day.")
else:
    print("You didn't put a valid value :c")

