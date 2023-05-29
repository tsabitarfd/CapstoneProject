import sys
import tabulate
import pyinputplus as pypi

def showitem(dict, title="\nSupermarket Warehouse\n"):
    #Menampilkan judul
    print(title)
    #Menampilkan dalam bentuk tabel
    data = list(listItem.values())[1:]
    header = listItem['Column']
    print(tabulate.tabulate(data, header, tablefmt="outline"))
    print("\n")

def additem():
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
    #Menambahkan qty
    itemQty = pypi.inputStr(
        prompt = 'Enter Item Qty (pcs/box/dz): ',
        applyFunc = lambda x: x.lower(),
        blockRegexes = [r'[0-9]'])
    #Menambhakan stock opname
    itemStock = pypi.inputInt(
        prompt = 'Enter Stock Item: ')
    #Menampilkan konfirmasi item sudah ditambhakan
    addUpdate = pypi.inputYesNo(prompt = 'Do you want to add items? (yes/no)')
    if addUpdate == 'yes':
        print('Item added successfully.')
        #Loop item dalam list item
        for key, value in listItem.copy().items():
            #Penambahan item yang diinginkan dalam show item
            if itemBarcode in list(listItem):
                listItem[key][1] = itemType
                listItem[key][2] = itemName
                listItem[key][3] = itemQty
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
                    itemQty,
                    itemPrice,
                    itemStock]})
        showitem(listItem)

            
            
    

def updateitem():
    #Tampilan menu update
    while True:
        prompt = f'Update Stock and Price\n'
        choiceUpdate = ['Update Stock',
                        'Update Price',
                        'Main Menu']
        responsechoiceUpdate = pypi.inputMenu(prompt=prompt, choices=choiceUpdate, numbered=True)
    #Masukkan pilihan update stock item/no
        if responsechoiceUpdate == 'Update Stock':
            while True:
                itemBarcode = pypi.inputInt(prompt = 'Enter Barcode Item: ',)
                #Cek barcode tidak ditemukan
                if itemBarcode not in listItem.keys():
                    print('Barcode does not exist.')
                    continue
                else:
                    break
            updatestockItem = pypi.inputInt(prompt = 'Add new item stock: ' )
            #Update stock item
            listItem[itemBarcode][5] += updatestockItem
            choiceUpdate = pypi.inputYesNo(prompt = 'Do you want to update stock items? (yes/no)')
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
                    break
            updatePriceitem = pypi.inputInt(prompt = 'Add new price item: ' )
                #Update stock item
            listItem[itemBarcode][4] = updatePriceitem
            choiceupdatePrice = pypi.inputYesNo(
                    prompt = 'Do you want to update price items? (yes/no)')
            if choiceupdatePrice == 'yes':    
                print('Price item updated successfully')
                showitem(listItem)
            else:
                break
                
        #kembali ke menu utama
        else:
            break
    #Update stock opname item



def deleteitem():
    #validasi barcode item yang ada
    while True:
        itemBarcode = pypi.inputInt(
            prompt = 'Enter Barcode Item: ', 
            min = 1001, 
            max = 9999)
        #Cek barcode ada atau tidak (balik menu delete item)
        if itemBarcode in listItem.keys(): 
            #Delete item dengan barcode kalau yes dan barcode ada di list
            for key, value in listItem.copy().items():
                if itemBarcode in value:
                    del listItem[key]
            print('Item deleted successfully.')
            showitem(listItem)
            deleteUpdate = pypi.inputYesNo(
                prompt = 'Do you want to delete item? (yes/no)')
            if deleteUpdate == 'yes':
                continue
            else:
                break
        else:    
            print('Barcode does not exist.')
            continue



def func(db):
    #Mengubah value list item menjadi list
    dataitem = list(db.values())[1:]
    header = db['Column']
    return dataitem, header



def main():
    while True:
        #Tampilan utama
        prompt = f'Supermarket Warehouse\nMain Menu:\n'
        #Pilihan main menu
        choice = ['Show Item',
                  'Add Item',
                  'Update Item',
                  'Delete Item',
                  'Exit']
        responsemain = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)
        #Menampilkan Item Gudang
        if responsemain == 'Show Item':
            # list item tidak ada
            if len(listItem) == 0:
                print('item is empty')
                continue
            #list item tidak ada
            elif len(listItem) == 1 and list(listItem.keys())[0] == 'Column':
                print('item is empty')
                continue
            elif listItem != {}:
                while True:
                    #Tampilan Menu Show Item
                    prompt = f'Supermarket Warehouse\nShow Item Menu:\n'
                    #Pilihan Menu Show Item
                    choice = ['Show All',
                            'Show by Barcode',
                            'Main Menu']
                    responseshow = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)
                    #Menampilkan Menu Show Item
                    if responseshow == 'Show All':
                        showitem(listItem)
                    #Menambilkan data berdasarkan barcode
                    elif responseshow == 'Show by Barcode':
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
                                continue
                            break
                    else:
                        break
            else:
                print('Empty data, please enter available data first')
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
        'Column' : ['Barcode', 'Item Type', 'Item', 'Qty', 'Price', 'Stock Opname'],
        3001 : [3001, 'non food', 'Soap', 'pcs', 12000, 5],
        1001 : [1001, 'food', 'Cooking Oil', 'pcs', 14000, 7],
        1002 : [1002, 'food', 'Rice', 'pcs', 60000, 3],
        3002 : [3002, 'non food', 'Lamp','pcs', 35000, 8],
        1003 : [1003, 'food', 'Lotus Biscuits', 'pcs', 43000, 9],
        }
    #Format Item
    formatItem = "{:<2}" + "{:<12}" + "{:<13}" + "{:<18}" + "{:<8}" + "{:<10}" + "{:<15}"
    #Menjalankan fungsi utama main()
    main()