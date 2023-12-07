import sqlite3

#import mysql.connector
from flask import g


def conect_to_Database():
  sql = sqlite3.connect("players.db")
  sql.row_factory = sqlite3.Row
  return sql

def get_database():
  if not hasattr(g, "players_db"):
    g.players_db = conect_to_Database()

  return g.players_db

""""mydb = mysql.connector.connect(
  host="localhost",
  user=input(""),
  password=input("")
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE users")"""

