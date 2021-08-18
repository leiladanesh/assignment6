
from enum import Flag
from pyfiglet import Figlet
import qrcode

list_product=[]


f = Figlet(font='standard')
print (f.renderText('top stor '))


def show_nemu():
    print ('1- add product')
    print ( '2- edit product')
    print ('3- delete product')
    print ('4- search poroduct')
    print ('5- buy prodoct')
    print ( '6- qr code product')
    print ( '7- show list')
    print ( '8- exit')

def database():
    d_f = open('databeas.txt','r')
    data = d_f.read()
    data = data.strip()
    return data

def lode():
    file = open('databeas.txt', 'r')
    data = file.read()
    product_list = data.split('\n')

    for i in range(len(product_list)):
        info_product = product_list[i].split(',')
        kala= {}
        kala['id']= info_product [0]
        kala['name']= info_product [1]
        kala['price']= info_product [2]
        kala['count']= info_product [3]
        list_product.append(kala)
       
    
def show_list():
    for i in range(len(list_product)):
        print(list_product[i])

def add_product():
    n= int(input('add product ='))
    add_dict ={}
    for i in range(n):
        print('product',(i+1))
        id = input('id product: ')
        name =input('name product: ')
        price =input('price product: ')
        count = input('count product: ')
        add_dict['id ']= id
        add_dict['name']= name
        add_dict['price']=price
        add_dict['count ']= count
        list_product.append(add_dict)
        print(name, (i+1),'added ')
        

def save():
    d_f = open('databeas.txt','w')
    for i in range(len(list_product)):
        save_dict = list_product[i]
        id = save_dict['id']
        name=save_dict['name']
        price= save_dict['price']
        count= save_dict['count']
        d_f.write('%s,%s,%s,%s\n'%(id,name,price,count))

    d_f.close()
    print('changes saved :')   

def edit():
    print ('number of product :', len (list_product))
    while True:
        p = int( input(' product \'s number: '))
        if 0 < p <= len(list_product):
            break
        else:
            print('bbbbbb')
            continue
    k -= 1
    id =  list_product[k]['id']
    name = list_product[k]['name']
    price = list_product[k]['price']
    count = list_product[k]['count']
    print('ID: %s - NAME: %s - PRICE: %s - COUNT: %s'%(id,name,price,count))
    while True:
        print('1.edit id - 2.edit name - 3.edit price - 4. edit count -5 .exit editor ')
        x= int(input('select option: '))
        if x == 1:
            new_id = input('new id =')
            list_product[k]['id'] = new_id
        elif x == 2:
            new_name = input('new name = ')
            list_product[k]['name']= new_name  
        elif x == 3:
            new_price = input('new price =')
            list_product[k]['price'] = new_price
        elif x == 4:
            new_count = input('new count ')
            list_product[k]['count']= new_count
        elif x == 5:
            print('exit')
            break
        else:
            print('pleas chose a corrent number:')
            continue
    print(' new list')
    show_list()    

def search():
    s = input('pleas Enter name product :') 
    Flag= 0

    for i in range(len(list_product)):
        if s.upper().strip () == list_product[i]['name'].strip().upper():
            index = i
            Flag = 1
            break
    if Flag == 1:
        print(' find product') 
        print(list_product[index])
    else:
        print('this product is not find:')

def qr_code():

    while True:
        code = input('product \'s code:')  
        Flag = 0 
        for i in range(len(list_product)):
            if list_product[i]['id'] == code:
                Flag =1
                index = i
                break
            if Flag == 0:
                print('This product \'s id is not exist ')
                print ('EXIT QR code ...')
                break
            else:
                id= list_product[index]['id']
                name= list_product[index]['name']
                price= list_product[index]['price']
                count= list_product[index]['count'] 
                qr_code = id  +name +price +count
                img = qrcode.make(qr_code) 
                img.save(qrcode_address)
                print('product\'s QR Code is Ready :')
                break

def stor():
    while True:
        show_nemu()
        choice = int(input('pleas choose a number:'))

        if choice == 1:
            add_product()
        elif choice == 2:
            edit()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            search()
        elif choice == 5:
            show_list()
        elif choice == 6:
            buy() 
        elif choice == 7:
            qr_code()
        elif choice == 8:
            save()
            exit()
            break
        
        else:
            print('please choose a correct number ') 
            continue

#lode()
stor()                          
                    


       




        

        






show_nemu() 

