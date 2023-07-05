import sqlite3
from beautifultable import BeautifulTable
import datetime
import warnings
warnings.filterwarnings("ignore")

# Format date
def validate_Date(date_string):
    formats = ["%Y-%m-%d", "%d-%m-%Y"]
    for format in formats:
        try:
            temp = datetime.datetime.strptime(date_string, format)
            return temp.strftime("%d-%m-%Y")
        except ValueError:
            pass
    return False


class Idol:
    def __init__(self, DB_Idol):
        self.conn = sqlite3.connect(DB_Idol)
        self.cursor = self.conn.cursor()

    # Show id_groups , name_groups of Groups table
    def show_all_groups(self):
        sql_select_all_groups = """
            select Id_Group , Name_Groups from Groups
        """
        self.cursor.execute(sql_select_all_groups)
        information_groups = self.cursor.fetchall()
        table = BeautifulTable()
        table.column_headers = ["Id Group", "Name Group"]
        for i in range(len(information_groups)):
            table.append_row(information_groups[i])
        print(table)

    # Enter the actor's information
    def Add_Idol(self, Number_Extra_Quantity_Idol):
        for i in range(Number_Extra_Quantity_Idol):
            English_Name = input("Enter Idol's English Name: ")

            Gender_Input = int(input("Enter Idol's Gender(0 - Male | 1 - Female): "))

            # validate Gender
            if Gender_Input == 0:
                Gender = "Male"
            elif Gender_Input == 1:
                Gender = "Female"
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!! Please double check the idol gender you just entered !!!!!!!!!!!!!!!!!!!!!!!!!")
                print("")
                break
            
            Date_Of_Birth = input(
                "Enter Idol's Date Of Birth: "
            )
            if validate_Date(Date_Of_Birth) == False:
                print(
                    "!!!!!!!!!!!!!!!!!!!!!!!!! Date is not in the correct format, please enter in the required format !!!!!!!!!!!!!!!!!!!!!!!!!"
                )
                print("")
                break
            else:
                formated_dateofbirth = validate_Date(Date_Of_Birth)

            Height = float(input("Enter Idol's Height: "))

            Nationality = input("Enter Idol's Nationality: ")

            Id_Group_Input = int(input("Enter the group's representative identifier: "))
            print("")
            
            # validate Id_Group
            sql_get_Id_Group = '''
                select * from Groups where Id_Group = {}
            '''.format(Id_Group_Input)
            self.cursor.execute(sql_get_Id_Group)
            record_IdGroup = self.cursor.fetchone()
            
            if record_IdGroup is None:
                print("!!!!!!!!!!!!!!!!!!!!!!!!! The ID of this group is currently unavailable, please check again !!!!!!!!!!!!!!!!!!!!!!!!!")
                print("")
                break
                
            else:
               Id_Group = Id_Group_Input
               
            sql_query_insert_idol = """
                insert into Idol(English_Name , Gender , Date_Of_Birth , Height , Nationality , Id_Group) values(? , ? , ? , ? , ? , ?)
            """
            values = (English_Name, Gender, formated_dateofbirth, Height, Nationality , Id_Group)
            
            self.cursor.execute(sql_query_insert_idol, values)
            self.conn.commit()
            print(
                "--------------------------------------- Actor info has been added successfully ---------------------------------------"
            )

    # Get information Idol
    def get_idol(self):
        sql_select_information_idol = '''
            select * from Idol
        '''
        self.cursor.execute(sql_select_information_idol)
        records_idol = self.cursor.fetchall()
        table_idol = BeautifulTable()
        table_idol.column_headers = ["Id" , "English Name" , "Gender" , "Date Of Birth" , "Height (Cm)" , "Nationality" , "Id Group"]
        table_idol.column_widths = 20
        for i in range(len(records_idol)):
            table_idol.append_row(records_idol[i])
        print("------------------------------------- Information of all existing Idols -------------------------------------")
        print(table_idol)
        print("")

    # Update
    def update_idol(self):
        number_of_update_idol = int(input("Enter the number of idols you want to update: "))
        for i in range(number_of_update_idol):
            id_idol_update = int(input("Enter the id of the idol to update: "))
            sql_validate_id_update = '''
                select * from Idol where Id_Idol = {}
            '''.format(id_idol_update)
            self.cursor.execute(sql_validate_id_update)
            record_id_idol = self.cursor.fetchone()
            if record_id_idol is None:
                print("!!!!!!!!!!!!!!!!!!!!!!!!! The ID of this Idol is currently unavailable, please check again !!!!!!!!!!!!!!!!!!!!!!!!!")
                print("")
                break
            else: 
                English_Name = input("Enter Idol's New English Name: ")

                Gender_Input = int(input("Enter Idol's New Gender(0 - Male | 1 - Female): "))

                # validate Gender
                if Gender_Input == 0:
                    Gender = "Male"
                elif Gender_Input == 1:
                    Gender = "Female"
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!! Please double check the idol gender you just entered !!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("")
                    break
                
                Date_Of_Birth = input(
                    "Enter Idol's New Date Of Birth: "
                )
                if validate_Date(Date_Of_Birth) == False:
                    print(
                        "!!!!!!!!!!!!!!!!!!!!!!!!! Date is not in the correct format, please enter in the required format !!!!!!!!!!!!!!!!!!!!!!!!!"
                    )
                    print("")
                    break
                else:
                    formated_dateofbirth = validate_Date(Date_Of_Birth)

                Height = float(input("Enter Idol's New Height: "))

                Nationality = input("Enter Idol's New Nationality: ")

                Id_Group_Input = int(input("Enter the group's New representative identifier: "))
                print("")
                
                # validate Id_Group
                sql_get_Id_Group = '''
                    select * from Groups where Id_Group = {}
                '''.format(Id_Group_Input)
                self.cursor.execute(sql_get_Id_Group)
                record_IdGroup = self.cursor.fetchone()
                
                if record_IdGroup is None:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!! The ID of this group is currently unavailable, please check again !!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("")
                    break
                else:
                    Id_Group = Id_Group_Input
                
                sql_query_insert_idol = """
                    update Idol set English_Name = ? , Gender = ? , Date_Of_Birth = ? , Height = ? , Nationality = ? , Id_Group = ? where Id_Idol = ?
                """
                values = (English_Name, Gender, formated_dateofbirth, Height, Nationality , Id_Group , id_idol_update)
                
                self.cursor.execute(sql_query_insert_idol, values)
                self.conn.commit()
                print(
                    "--------------------------------------- Actor info has been updated successfully ---------------------------------------"
                )
        
    # Delete
    def delete_idol(self):
        number_of_update_idol = int(input("Enter the number of idols you want to update: "))
        for i in range(number_of_update_idol):
            id_idol_delete = int(input("Enter the idol id you want to delete: "))
            sql_validate_id_update = '''
                select * from Idol where Id_Idol = {}
            '''.format(id_idol_delete)
            self.cursor.execute(sql_validate_id_update)
            record_id_idol = self.cursor.fetchone()
            if record_id_idol is None:
                print("!!!!!!!!!!!!!!!!!!!!!!!!! The ID of this Idol is currently unavailable, please check again !!!!!!!!!!!!!!!!!!!!!!!!!")
                print("")
                break
            else: 
                sql_delete_idol = '''
                    delete from Idol where Id_Idol = {}
                '''.format(id_idol_delete)
                self.cursor.execute(sql_delete_idol)
                self.conn.commit()
                print(
                    "--------------------------------------- Actor info has been deleted successfully ---------------------------------------"
                )
    
    # List descending by height of male idols
    def Sort_By_height_male(self):
        sql_get_idol_by_gender_male = '''
            select * from Idol where Gender = 'Male' order by Height desc
        '''
        self.cursor.execute(sql_get_idol_by_gender_male)
        records_idol = self.cursor.fetchall()
        table_idol = BeautifulTable()
        table_idol.column_headers = ["Id" , "English Name" , "Gender" , "Date Of Birth" , "Height (Cm)" , "Nationality" , "Id Group"]
        table_idol.column_widths = 20
        for i in range(len(records_idol)):
            table_idol.append_row(records_idol[i])
        print("---------------------------------- List descending by height of male idols ----------------------------------")
        print(table_idol)
        print("")
    
    # The list descending to the height of male idols
    def Sort_By_height_female(self):
        sql_get_idol_by_gender_male = '''
            select * from Idol where Gender = 'Female' order by Height desc
        '''
        self.cursor.execute(sql_get_idol_by_gender_male)
        records_idol = self.cursor.fetchall()
        table_idol = BeautifulTable()
        table_idol.column_headers = ["Id" , "English Name" , "Gender" , "Date Of Birth" , "Height (Cm)" , "Nationality" , "Id Group"]
        table_idol.column_widths = 20
        for i in range(len(records_idol)):
            table_idol.append_row(records_idol[i])
        print("---------------------------------- List descending by height of female idols ----------------------------------")
        print(table_idol)
        print("")
    
    # find by name of idol
    def find_idol_by_name(self):
        English_Name = input("Enter the name of the idol you want to find: ")
        print("")
        sql_find_idol_by_name = '''
            select * from Idol where English_Name like '%{}%'
        '''.format(English_Name)
        self.cursor.execute(sql_find_idol_by_name)
        record_idol_by_name = self.cursor.fetchall()
        if len(record_idol_by_name) == 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! There are no idols like the information you requested !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("")
        else:
            table_idol = BeautifulTable()
            table_idol.column_headers = ["Id" , "English Name" , "Gender" , "Date Of Birth" , "Height (Cm)" , "Nationality" , "Id Group"]
            table_idol.column_widths = 20
            for i in range(len(record_idol_by_name)):
                table_idol.append_row(record_idol_by_name[i])
            print("---------------------------------- List of idols you want to find ----------------------------------")
            print(table_idol)
            print("")

    def idol_in_the_same_group(self):
        group_name = input("Enter the name of the group you want to search for: ")
        sql_query = '''
            select English_Name , Name_Groups from Idol join Groups on Idol.Id_Group = Groups.Id_Group
            where Groups.Name_Groups like '%{}%'
        '''.format(group_name)
        
        self.cursor.execute(sql_query)
        record = self.cursor.fetchall()
        if len(record) == 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! There is no group named {} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(group_name))
            print("")
        else:
            table_idol = BeautifulTable()
            table_idol.column_headers = ["Idol's Name" , "Name Group"]
            table_idol.column_widths = 20
            for i in range(len(record)):
                table_idol.append_row(record[i])
            print("---------------------------------- List of idols you want to find ----------------------------------")
            print(table_idol)
            print("")
    
    # Close Connection
    def Close_Connection(self):
        self.conn.close()


# Main function
if __name__ == "__main__":
    db = Idol("DB_Idol_Kpop.db")
    while True:
        print("------------------------------------------------- MENU -------------------------------------------------")
        print("1. Add Idol")
        print("2. Update information of Idol")
        print("3. Delete information of Idol")
        print("4. Sort by descending height of male idols")
        print("5. Sort by descending height of female idols")
        print("6. Find by name of idol")
        print("7. Looking for idols in the same group")
        print("8. Show Idol's information")
        print("0. End Program")
        print("------------------------------------------------- END -------------------------------------------------")
        print("")
        choose = int(input("Enter your choose: "))
        print("")
        # Follow user selection
        try:
            # Add
            if choose == 1:
                print(
                    "--------------------------------- Information about existing music groups ---------------------------------"
                )
                db.show_all_groups()
                print("")
                number_of_extra_Idol = int(
                    input("Enter the quantity idol to be added: ")
                )
                db.Add_Idol(number_of_extra_Idol)
            
            # update idol's information   
            if choose == 2:
                db.get_idol()
                print("")
                db.update_idol()
            
            # delete idol
            if choose == 3:
                db.get_idol()
                print("")
                db.delete_idol()
            
            # Sort by descending height of male idols
            if choose == 4:
                db.Sort_By_height_male()
            
            # Sort by descending height of Female idols
            if choose == 5:
                db.Sort_By_height_female()
            
            # Find by name of idol
            if choose == 6:
                db.find_idol_by_name()
            
            if choose == 7:
                db.idol_in_the_same_group()
            
            # Get idol's information    
            if choose == 8:
                db.get_idol()
                
            # End Program
            if choose == 0:
                break

        except Exception as e:
            print("Error: ", e)

        finally:
            if choose == 0:
                db.Close_Connection()
