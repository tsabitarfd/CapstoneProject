import sys
import tabulate
import pyinputplus as pypi

def showitem(dict, title="\nSUPERMARKET WAREHOUSE\n"):
    #Menampilkan judul
    print(title)
    #Menampilkan dalam bentuk tabel
    data = list(listItem.values())[1:]
    header = listItem['Column']
    print(tabulate.tabulate(data, header, tablefmt="outline"))
    print("\n")

def additem():
    #Menampilkan menu add item
    while True:
        prompt = f'Add New Item\n'
        choiceUpdate = [' Add New Item',
                        'Main Menu']
        responsechoiceAdd = pypi.inputMenu(
            prompt=prompt, 
            choices=choiceUpdate, 
            numbered=True)
        #Pilihan Add Item
        if responsechoiceAdd == 'Add New Item':
            #Menambahkan barcode item
            while True:
                itemBarcode = pypi.inputInt(
                    prompt = 'Enter Barcode Item: ', 
                    min = 1001, 
                    max = 9999)
                #Cek barcode sudah ada atau belum pakai filter
                if itemBarcode in listItem.keys():
                    print('Barcode already exist.')
                    continue
                break
                #Menambahkan item type
            itemType = pypi.inputStr(
                prompt = 'Enter Item Type. (food/non food): ',
                applyFunc = lambda x: x.lower(),)
            #Menambahkan item
            itemName = pypi.inputStr(
                prompt = 'Enter Item Name: ',
                applyFunc = lambda x: x.capitalize(),
                blockRegexes = [r'[0-9]'])
            #Menambahkan price
            itemPrice = pypi.inputInt(
                prompt = 'Enter Item Price: ',)
            #Menambahkan Unit
            itemUnit = pypi.inputStr(
                prompt = 'Enter Item Unit (pcs/box/dz): ',
                applyFunc = lambda x: x.lower(),
                blockRegexes = [r'[0-9]'])
            #Menambhakan stock opname
            itemStock = pypi.inputInt(
                prompt = 'Enter Stock Item: ')
            #Menampilkan konfirmasi item sudah ditambhakan
            addUpdate = pypi.inputYesNo(
                prompt = 'Do you want to add items? (yes/no)')
            if addUpdate == 'yes':
                print('Item added successfully.')
                #Loop item dalam list item
                for key, value in listItem.copy().items():
                    #Penambahan item yang diinginkan dalam show item
                    if itemBarcode in list(listItem):
                        listItem[key][1] = itemType
                        listItem[key][2] = itemName
                        listItem[key][3] = itemUnit
                        listItem[key][4] = itemPrice
                        listItem[key][5] += itemStock
                    #Menambahkan item baru
                    else:
                        index = len(listItem) - 1
                        listItem.update(
                            {f'{itemBarcode}':
                            [itemBarcode,
                            itemType,
                            itemName,
                            itemUnit,
                            itemPrice,
                            itemStock]})
                showitem(listItem)
            else:
                break

            
            
    

def updateitem():
    #Tampilan menu update
    while True:
        prompt = f'Update Stock, Price, and Unit\n'
        choiceUpdate = ['Update Stock',
                        'Update Price',
                        'Update Unit',
                        'Main Menu']
        responsechoiceUpdate = pypi.inputMenu(prompt=prompt, choices=choiceUpdate, numbered=True)
    #Masukkan pilihan update stock item/no
        if responsechoiceUpdate == 'Update Stock':
            while True:
                itemBarcode = pypi.inputInt(
                    prompt = 'Enter Barcode Item: ',)
                #Cek barcode tidak ditemukan
                if itemBarcode not in listItem.keys():
                    print('Barcode does not exist.')
                    continue
                else:
                    #Menampilkan barcode yang ingin diupdate
                    header = listItem['Column']
                    data = [listItem[itemBarcode]]
                    print(tabulate.tabulate(data, header, tablefmt="outline"))
                    break
            updatestockItem = pypi.inputInt(prompt = 'Update item stock: ' )
            #Update stock item
            listItem[itemBarcode][5] += updatestockItem
            choiceUpdate = pypi.inputYesNo(
                prompt = 'Do you want to update stock items? (yes/no)')
            if choiceUpdate == 'yes':
                print('Stock item updated successfully')
                showitem(listItem)
            else:
                break

        elif responsechoiceUpdate == 'Update Price':
            #Pilihan mau update harga atau tidak
            while True:
                itemBarcode = pypi.inputInt(
                    prompt = 'Enter Barcode Item: ',)
                    #Cek barcode tidak ditemukan
                if itemBarcode not in listItem.keys():
                    print('Barcode does not exist.')
                    continue
                else:
                    #Menampilkan barcode yang ingin diupdate
                    header = listItem['Column']
                    data = [listItem[itemBarcode]]
                    print(tabulate.tabulate(data, header, tablefmt="outline"))
                    break
            updatePriceitem = pypi.inputInt(
                prompt = 'Update price item: ' )
                #Update stock item
            listItem[itemBarcode][4] = updatePriceitem
            choiceupdatePrice = pypi.inputYesNo(
                    prompt = 'Do you want to update price items? (yes/no)')
            if choiceupdatePrice == 'yes':    
                print('Price item updated successfully')
                showitem(listItem)
            else:
                break
        elif responsechoiceUpdate == 'Update Unit':
            #Pilihan mau update Unit atau tidak
            while True:
                itemBarcode = pypi.inputInt(
                    prompt = 'Enter Barcode Item: ',)
                    #Cek barcode tidak ditemukan
                if itemBarcode not in listItem.keys():
                    print('Barcode does not exist.')
                    continue
                else:
                    #Menampilkan barcode yang ingin diupdate
                    header = listItem['Column']
                    data = [listItem[itemBarcode]]
                    print(tabulate.tabulate(data, header, tablefmt="outline"))
                    break
            updateUnititem = pypi.inputStr(
                prompt = 'Update unit item (pcs/box/dz): ' )
                #Update stock item
            listItem[itemBarcode][3] = updateUnititem
            choiceupdateUnit = pypi.inputYesNo(
                    prompt = 'Do you want to update unit items? (yes/no)')
            if choiceupdateUnit == 'yes':    
                print('Unit item updated successfully')
                showitem(listItem)
            else:
                break
                
        #kembali ke menu utama
        else:
            break




def deleteitem():
    #Menu delete item
    while True:
        prompt = f'Delete Item\n'
        choiceDelete = ['Delete Item',
                        'Delete All Item',
                        'Main Menu']
        responechoiceDelete = pypi.inputMenu(
            prompt=prompt, 
            choices=choiceDelete, 
            numbered=True)
        #Masukkan pilihan delete
        if responechoiceDelete == 'Delete Item':
            #validasi barcode item yang ada
            while True:
                itemBarcode = pypi.inputInt(
                    prompt = 'Enter Barcode Item: ', 
                    min = 1001, 
                    max = 9999)
                #Cek barcode ada atau tidak (balik menu delete item)
                if itemBarcode in listItem.keys(): 
                    #Menampilkan barcode yang ingin dihapus
                    header = listItem['Column']
                    data = [listItem[itemBarcode]]
                    print(tabulate.tabulate(data, header, tablefmt="outline"))
                    #Delete item dengan barcode kalau yes dan barcode ada di list
                    deleteUpdate = pypi.inputYesNo(
                                prompt = 'Do you want to delete item? (yes/no)')
                    if deleteUpdate == 'yes':
                        del listItem[itemBarcode]
                        print('Item deleted successfully.')
                        break
                    else:
                        break
                else:    
                    print('Barcode does not exist.')
                    break
        #Menghapus semua item
        elif responechoiceDelete == 'Delete All Item':
            showitem(listItem)
            deleteAll = pypi.inputYesNo(
            prompt= 'Do you want to delete all items? (yes/no)')
            if deleteAll == 'yes':
                for key in listItem.copy().keys():
                    if key == 'Column':
                        continue
                    del listItem[key]
                print('All item deleted successfully.')
                showitem(listItem)
                break
        else:
            break





def func(db):
    #Mengubah value list item menjadi list
    dataitem = list(db.values())[1:]
    header = db['Column']
    return dataitem, header





def main():
    while True:
        #Tampilan utama
        prompt = f'SUPERMARKET WAREHOUSE\nMain Menu:\n'
        #Pilihan main menu
        choice = ['Show Item',
                  'Add Item',
                  'Update Item',
                  'Delete Item',
                  'Exit']
        responsemain = pypi.inputMenu(
            prompt=prompt, 
            choices=choice, 
            numbered=True)
        #Menampilkan Item Gudang
        if responsemain == 'Show Item':
                while True:
                    #Tampilan Menu Show Item
                    prompt = f'SUPERMARKET WAREHOUSE\nShow Item Menu:\n'
                    #Pilihan Menu Show Item
                    choice = ['Show All Item',
                            'Show by Barcode Item',
                            'Main Menu']
                    responseshow = pypi.inputMenu(
                        prompt=prompt, 
                        choices=choice, 
                        numbered=True)
                    #Menampilkan Menu Show Item
                    if responseshow == 'Show All Item':
                        # list item tidak ada
                        if len(listItem) == 0:
                            print('Item is empty')
                            continue
                        #list item tidak ada
                        elif len(listItem) == 1 and list(listItem.keys())[0] == 'Column':
                            print('Item is empty')
                            continue
                        elif listItem != {}:
                            showitem(listItem)
                    #Menambilkan data berdasarkan barcode
                    elif responseshow == 'Show by Barcode Item':
                         # list item tidak ada
                        if len(listItem) == 0:
                            print('Item is empty')
                            continue
                        #list item tidak ada
                        elif len(listItem) == 1 and list(listItem.keys())[0] == 'Column':
                            print('Item is empty')
                            continue
                        while True:
                            prompt = 'Enter barcode: '
                            responsebarcode = pypi.inputInt(prompt=prompt)
                            dataitem, header = func(listItem)
                            #Memfilter data item berdasarkan barcode
                            filterbarcode = list(filter(lambda row: row[0] == responsebarcode, dataitem))
                            #Barcode ada atau engga dalam data
                            if filterbarcode != []:
                                print(tabulate.tabulate(filterbarcode, header, tablefmt="outline"))
                            else:
                                print('Barcode does not exist.')
                                break
                            break
                    else:
                        break
        #Menambahkan Item Gudang
        elif responsemain == 'Add Item':
            additem()
        #Mengupdate Item Gudang
        elif responsemain == 'Update Item':
            updateitem()
        #Menghapus Item Gudang
        elif responsemain == 'Delete Item':
            deleteitem()
        #Exit program
        else:
            sys.exit()





if __name__ == "__main__":
    #List item
    listItem = {
        'Column' : ['Barcode', 'Item Type', 'Item', 'Unit', 'Price', 'Stock Opname'],
        6749 : [6749, 'non food', 'Soap', 'pcs', 12000, 5],
        1298 : [1298, 'food', 'Cooking Oil', 'pcs', 14000, 7],
        3842 : [3842, 'food', 'Rice', 'pcs', 60000, 3],
        3802 : [3802, 'non food', 'Lamp','pcs', 35000, 8],
        5084 : [5084, 'food', 'Lotus Biscuits', 'pcs', 43000, 9],
        9383 : [9383, 'non food', 'Book', 'box', 8000, 3]
        }
    #Format Item
    formatItem = "{:<2}" + "{:<12}" + "{:<13}" + "{:<18}" + "{:<8}" + "{:<10}" + "{:<15}"
    #Menjalankan fungsi utama main()
    main()