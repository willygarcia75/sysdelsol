from flask import Flask
import mysql.connector


from app import create_app,db

app = create_app()
app.app_context().push()


if __name__ == "__main__":
    print("Hola lhñlhkgkghg")
 #   app.run(debug=True, host = "0.0.0.0", port=5000)