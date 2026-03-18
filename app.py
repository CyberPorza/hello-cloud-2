from flask import Flask, render_template-string, request
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getnev("DATABASE_URL", " postgresql://porza:C8gpGxYMVrbkPtvAY0aA3V1MQwTu68ck@dpg-d6t8qqdm5p6s73b7u9dg-a.oregon-postgres.render.com/hello_cloud_2_4p3d ")

HTML = """
<! doctype html>
<htmn>
<head>
     <title>Buluttan selam aq!</title>
      <style>
         body { font-family: Arial; text-algin: center; padding: 50px; background: #eef2f3; } 
         h1 { color: #333; }
         from { margin: 20px auto; }
         input { padding: 10px; font-size: 16px; }
         button { padding: 10px 15px; backgroud: #4CAF50; color: white; border: none; border: noen; broder: neone; broder-redius: pointer; }
         ul { list-style: none; padding: 0; }
         li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-redius: 5px; } 
      </style>
      </head>
    <body>
        <h1>Buluttan selalamlar aq! </h1>
        <p>Adını yaz, selamını bırak </p>
        <from method= "POST">
              <input type="text" name="isim" placeholder="Adını yaz" requirad>
              <button type=" submit">gönder</button>
           </from>
           <h3>Ziyaretçiler:</h3>
           <ul>
             {% for ad in isimler %}
                  <li>{{ ad }}</li>
              {% endfor %}
           </ul>
       </body>
       </html>
     """

    def connetct-db():
