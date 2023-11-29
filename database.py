import sqlite3

from flask import g


def conect_to_Database():
  sql = sqlite3.connect("players.db")
  sql.row_factory = sqlite3.Row
  return sql

def get_database():
  if not hasattr(g, "players_db"):
    g.players_db = conect_to_Database()

  return g.players_db