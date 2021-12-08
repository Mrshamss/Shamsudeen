import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'payment_system',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Login(
        ID INT NOT NULL AUTO_INCREMENT,
        user_name VARCHAR(255),
        Email VARCHAR(255),
        PRIMARY KEY(ID)
        
    )
    """
)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Student(
        ID INT NOT NULL AUTO_INCREMENT,
        First_Name VARCHAR(255),
        Last_Name VARCHAR(255),
        Department VARCHAR(255),
        Phone_no INT,
        Age INT,
        Email VARCHAR(255),
        PRIMARY KEY(ID)
    ) 
    """  
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS School(
        ID INT NOT NULL,
        School_Name VARCHAR(255),
        Department VARCHAR(255),
        UNIQUE (Student_ID),
        Phone_no INT,
        Date INT,
        Time INT,
        UNIQUE (Reciept),
        Email VARCHAR(255),
        PRIMARY KEY(ID)
        
    ) 
    """  
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Make_Payment(
        ID INT NOT NULL AUTO_INCREMENT,
        Student_Name VARCHAR(255),
        Student_ID VARCHAR(255),
        Reciept_No VARCHAR(255),
        Department VARCHAR(255),
        Amount VARCHAR(255),
        Phone_no INT,
        Data INT,
        Email VARCHAR(255),
        UNIQUE (Reciept_No),
        UNIQUE (Student_ID),
        PRIMARY KEY(ID)
    ) 
    """  
)

