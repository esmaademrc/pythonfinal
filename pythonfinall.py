import pypyodbc
db = pypyodbc.connect(
    'Driver={SQL server};'
    'Database=yemeklistesi;' 
    'Trusted_connection=True;'
    )
imlec=db.cursor()
imlec.execute('SELECT*FROM yemeklistesi')
def veriekle():
    imlec.execute("insert into tarif values('yemek_adı','yemek_tarifi')")
    imlec.commit()
    veriekle()
    kullanicilar=imlec.fetchall()


    for i in kullanicilar:
        print(i)
        db.close()
