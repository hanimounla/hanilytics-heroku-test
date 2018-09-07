import sqlite3
from sqlite3 import Error
import os
 

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database = os.path.join(BASE_DIR, 'hanilyticsDB.sqlite3')
# create a database connection
conn = create_connection(database)

def get_table_names():
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_data_from_table(table_name):
    cur = conn.cursor()
    cur.execute("SELECT * from " + table_name)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_all_articles():
    cur = conn.cursor()
    cur.execute("SELECT * from articles")
    rows = cur.fetchall()
    return rows

def get_latest_articles(limit):
    cur = conn.cursor()
    query = "SELECT a.id, a.title, a.url_title, a.text, a.date, a.image, c.name as category_name \
             FROM articles a inner join categories c \
             on a.category_id = c.id  ORDER BY a.ID DESC LIMIT %s"%limit
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def delete_all_articles():
    cur = conn.cursor()
    cur.execute("delete from articles ")
    conn.commit()
    cur.close()
 
def get_article(article_id):
    cur = conn.cursor()
    query = "select title, text, date from articles where id = %s"%article_id
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def main():
 
   
    with conn:
        # get_table_names(conn)
        # print("categories : ")
        # get_data_from_table(conn,"categories")
        # print ("articles :")
        # get_data_from_table(conn,"articles")
        print(get_all_articles())
        # print(test())
        # print(get_article(1))
        # delete_all_articles()
        # print("1. Query task by priority:")
        # select_task_by_priority(conn,1)
 
        # print("2. Query all tasks")
        # select_all_tasks(conn)
 
if __name__ == '__main__':
    main()