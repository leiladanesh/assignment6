
from typing import TextIO
from pyfiglet import Figlet
import qrcode
product=[]
PORODUCTS=[]   

f = Figlet(font='standard')
print (f.renderText('top store '))


def show_list():
    for i in range(len(PORODUCTS)):
        print( PORODUCTS[i]['id'],'\t',PORODUCTS[i]['name'],'\t',PORODUCTS[i]['price'],'\t',PORODUCTS[i]['count'],'\t')  


def show_nemu():
    print ('1- add product')
    print ( '2- edit product')
    print ('3- delete product')
    print ('4- search poroduct')
    print ('5- buy prodoct')
    print ( '6- qr code product')
    print ( '7- show list')
    print ( '8- exit')

def lode():
    print('loding....')
    f = open('databeas.txt','r')
    rows = f.read().split('\n') 
    
    for i in range(len(rows)):
        info = rows[i].split(',')
        PORODUCTS.append({'id':int(info[0]),'name':info[1],'price':float(info[2]),'count':int(info[3])})
    f.close()    
    print('program is ready to use')


def add_product():
    id = int(input('pleas enter id :'))
    name = input('pleas enter name :')
    price = float(input('pleas enter price: '))
    count = int(input('pleas enter count :'))
    PORODUCTS.append({'id':id , 'name': name , 'price':price, 'count':count})
    print('add product is successfully')

def show_edit_menu():
    print( '1- name ')
    print( '2- price ')
    print( '3- count ')
    print( '4- exit')

def edit_product():
    id = int(input('pleas Enter product id:'))
    for i in range(len(PORODUCTS)):
        if PORODUCTS[i]['id'] == id:
            while True:
                show_edit_menu()
                choice = int(input('pleas Enter edit product '))
                if choice == 1:
                    PORODUCTS[i]['name'] = iput('please Enter new name :')
                elif choice == 2:
                    PORODUCTS[i]['price'] = float(input('pleas Enter new price ;'))
                elif choice == 3:
                    PORODUCTS[i]['count'] = int(input('please Enter new count')) 
                elif choice == 4:
                    break
                else:
                    print('value eroor')      

def delet_product():
    id = int(input(' pleas Enter remove id : '))
    for i in range(len(PORODUCTS)):

        if PORODUCTS[i]['id'] == id:
            PORODUCTS.pop(i)
            print('product remov ')
            break

def search_product():
    word = input('pleas enter name or id :')
    for i in range(len(PORODUCTS)):
        if PORODUCTS[i]['name'] == word or str(PORODUCTS[i]['id'])== word:
            print(PORODUCTS[i])
            break
        else:
            print('there is not find ')    

def buy_product():
    basket = []

    while True:
        id = int(input('pleas Enter product id :'))
        for i in range(len(PORODUCTS)):
            if PORODUCTS[i]['id'] == id:
                count = int(input('pleas enter count: '))
                if PORODUCTS[i]['count'] >= count:
                    basket.append({'name':PORODUCTS[i]['name'],
                                  'price':PORODUCTS[i]['price'],
                                  'cont':count})
                    PORODUCTS[i]['count'] -= count
                    print('product added basket successfuly ')  
                else:
                    print('not exist')
                    print('we have ,',PORODUCTS[i]['count'],'from this product') 
        choice = input ('do you want to continue ? (Y/N)')
        if choice == 'N' or 'n':
            break
    print(basket)
#     total_price = 0
#     for i in range(len(basket)):
#        # total_price += basket[i]['price']* basket[i]['count']
#    # print('total price is: ',total_price)
#     print('thanks')
# 
def qrcodee():
    id = input('Enter id of product: ')
    f=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            img = qrcode.make(PRODUCTS[i])
            img.save('qrcode.png')
            f=1
    if f == 0:
        print('Input wrong id!')


def save_exit():

    f =open('databeas.txt','w')

    for i in range(len(PORODUCTS)):
        row = str(PORODUCTS[i]['id']) + ',' + PORODUCTS[i]['name']+','+ str(PORODUCTS[i]['price']) + ',' + str(PORODUCTS[i]['count'])
        f.write(str(row))
        if i< len(PORODUCTS)-1:
            f.write('\n')

    f.close() 
    exit()
    print('your change save well ')  


lode()

while True:
    show_nemu()

    choice = int(input('pleas choose a number:'))
    if choice == 1:
        add_product()
    if choice == 2:
        edit_product()
    if choice == 3:
        delet_product()        
    if choice == 4:
        search_product()
    if choice == 5:
        buy_product()
    if choice == 6:
        pass
    if choice == 7: 
        show_list()
    if choice == 8:
        save_exit()    
          

