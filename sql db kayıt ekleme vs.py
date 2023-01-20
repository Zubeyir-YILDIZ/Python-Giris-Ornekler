import mysql.connector

"""
def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(host="",user="",password="",database="")
    cursor=connection.cursor()   
    
    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kayıt numarası: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata',err)
    finally:
        connection.close()
        print('bağlantı kapandı.')
"""

def insertProducts(list):
    connection=mysql.connector.connect(host="",user="",password="",database="")
    cursor=connection.cursor()   
    
    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values=list
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kayıt numarası: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata',err)
    finally:
        connection.close()
        print('bağlantı kapandı.')

list=[]
while True:

    name=input('Ürün adı: ')
    price=float(input('Ürün fiyatı: '))
    imageUrl=input('Ürün resmi: ')
    description=input('Ürün açıklaması: ')

    list.append((name,price,imageUrl,description))

    devammi=input('devam etmek için(e)/çıkmak için(h)tuşlayınız')
    if devammi.lower()=='h':
        print('kaydediliyor...')
        insertProducts(list)
        break

#insertProduct(name,price,imageUrl,description)

