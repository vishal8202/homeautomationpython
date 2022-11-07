while True:
    print("""Select from the menu
            1. add values
            2. view all values
            3. search with dates
            4. exit \n""")
    choice =int(input(f"enter your choice : "))
    if choice==1:
        print("Add values selected")
    elif choice==2:
        print("view all values selected")
    elif choice==3:
        print("search values with date selected" )
    
    elif(choice==4):
        break
    