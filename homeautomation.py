import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password='',database = 'homeautomationdb')

mycursor = mydb.cursor()
while True:
    print("""Select from the menu
            1. add values
            2. view all values
            3. search with dates
            4. exit \n""")
    choice =int(input(f"enter your choice : "))
    if choice==1:
        print("Add values selected")
        temperature = input("Enther the temperature: ")
        humidity = input("Enter the humidity: ")
        moisture = input("Enter the moisture: ")
        sql = "INSERT INTO `sensorvalues`(`temperature`, `humidity`, `moisture`, `date`) VALUES (%s,%s,%s,now())"
        data = (temperature,humidity,moisture)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data Inserted Successfully")
    elif choice==2:
        print("view all values selected")
        sql = "SELECT `temperature`, `humidity`, `moisture`, `date` FROM `sensorvalues` "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        
    elif choice==3:
        print("search values with date selected")
        

    
    elif(choice==4):
        break