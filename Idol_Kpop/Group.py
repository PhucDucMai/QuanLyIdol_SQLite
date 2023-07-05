import sqlite3
from beautifultable import BeautifulTable

class Group:
    
    def __init__(self , db_file):
        self.conn = sqlite3.connect('DB_Idol_Kpop.db')
        self.cursor = self.conn.cursor()
        
    def show_groups(self):
        pass
    
    def add_group(self):
        pass
    
    def update_group(self):
        pass
    
    def delete_group(self):
        pass
    
    def find_group(self):
        pass
    
    
    
    