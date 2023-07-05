import sqlite3

# create connection object
conn = sqlite3.connect("DB_Idol_Kpop.db")
# create cursor to execute sql query
cursor = conn.cursor()

try:
    # sql query to create table
    
    sql_Createtable_Company = '''
        create table Company(
            Id_Company integer primary key autoincrement,
            Name_Company varchar(50)
        );
    '''
    
    sql_Createtable_Groups = '''
        create table Groups(
            Id_Group integer primary key autoincrement,
            Name_Groups varchar(50),
            Number_Of_Members integer,
            Founding date,
            Id_Company integer,
            foreign key (Id_Company) references Company(Id_Company)
        );
    '''
    
    sql_Createtable_Idol = '''
        create table Idol(
            Id_Idol integer primary key autoincrement,
            English_Name varchar(50),
            Gender varchar(10),
            Date_Of_Birth date,
            Height float,
            Nationality varchar(50),
            Id_Group integer,
            foreign key (Id_Group) references Groups(Id_Group)
        );
    '''
    
    sql_CreateTable_Songs = '''
        create table Songs(
            Id_Song integer primary key autoincrement,
            Name_Song varchar(50),
            Release_Date date,
            Album_Name varchar(50),
            Id_Group integer,
            foreign key (Id_Group) references Groups(Id_Group)
        );
    '''
    
    
    # # Create table Company
    # cursor.execute(sql_Createtable_Company)
    # # Create table Groups
    # cursor.execute(sql_Createtable_Groups)
    # # Create table idol
    # cursor.execute(sql_Createtable_Idol)
    # # Create table Songs
    # cursor.execute(sql_CreateTable_Songs)
    
    # commit changes
    conn.commit()
    
    # Notification
    # print("Table created successfully")
    
except Exception as e:
    print("Error: " , e)
    
finally:
    conn.close()