from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://hm52yv6yipogno23us92:pscale_pw_eZrNqk72z7SRQSKusEsbdJU0xcfJ9l2cnxNRtCXWQfl@aws.connect.psdb.cloud/players?charset=utf8mb4"

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