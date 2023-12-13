from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://xbdmp6x0vav96bk95r65:pscale_pw_VzJG0inxzUOtJC3mORE20Kph8r6J3huw9dC5l22RlhY@aws.connect.psdb.cloud/players?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": r"C:\Users\chris\Downloads\cacert-2023-08-22.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from list_players"))
  print(result.all())