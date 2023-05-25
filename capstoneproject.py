import sys
import tabulate
import pyinputplus as pypi

def showitem(dict, formatItem, title="\nSupermarket Warehouse\n"):
    #Menampilkan judul
    print(title)
    #Menampilkan dalam bentuk tabel
    data = list(listItem.values())[1:]
    header = listItem['Column']
    print(tabulate.tabulate(data, header, tablefmt="outline"))
    print("\n")

def additem():
    #Pilihan mau input barcode atau tidak (yes/no)
    addChoice = pypi.inputYesNo(
        prompt = 'Do you want to add items? (yes/no)')
    if addChoice == 'yes':
        #Menambahkan barcode item
        while True:
            itemBarcode = pypi.inputInt(
                prompt = 'Enter Barcode Item: ',)
            #Cek barcode sudah ada atau belum pakai filter
            filterbarcode = list(filter(lambda row: row[0] == itemBarcode, list(listItem.values())))
            if filterbarcode != []:
                print('Barcode already exist.')
                continue
            else:
            #Menambahkan item type
                itemType = pypi.inputStr(
                    prompt = 'Enter Item Type: ',
                    applyFunc = lambda x: x.capitalize(),)
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
                    prompt = 'Enter Item Qty: ',)
                #Menambhakan stock opname
                itemStock = pypi.inputInt(
                    prompt = 'Enter Stock Item: ')
                #Loop item dalam list item
                for key, value in listItem.copy().items():
                    #Penambahan item yang diinginkan dalam show item
                    if itemBarcode in list(listItem):
                        listItem[key][1] = itemType
                        listItem[key][2] = itemName
                        listItem[key][3] = itemPrice
                        listItem[key][4] = itemQty
                        listItem[key][5] += itemStock
                    #Menambahkan item baru
                    else:
                        index = len(listItem) - 1
                        listItem.update(
                            {f'{itemBarcode}':
                            [itemBarcode,
                            itemType,
                            itemName,
                            itemPrice,
                            itemQty,
                            itemStock]})
    else:

    # #Menampilkan daftar stock gudang terbaru
        showitem(listItem, formatItem)
    
    

# def updateitem():
    #Update stock opname item

def deleteitem():
    #Masukin pilihan delete/no

    #validasi barcode item yang ada
    itemBarcode = pypi.inputInt(
        prompt = 'Enter Barcode Item: ',
        lessThan = 9999)
    #Cek barcode ada atau tidak (balik menu delete item)

    #Delete item dengan barcode kalau ,pilih yes
    for key, value in listItem.copy().items():
        if itemBarcode in value:
            del listItem[key]
    #Menampilkan item yang masih ada
    showitem(listItem, formatItem)

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
            if listItem != {}:
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
                        showitem(listItem, formatItem)
                    #Menambilkan data berdasarkan barcode
                    elif responseshow == 'Show by Barcode':
                        prompt = 'Enter barcode: '
                        responsebarcode = pypi.inputInt(prompt=prompt)
                        dataitem, header = func(listItem)
                        #Memfilter data item berdasarkan barcode
                        filterbarcode = list(filter(lambda row: row[0] == responsebarcode, dataitem))
                        if filterbarcode != []:
                            print(tabulate.tabulate(filterbarcode, header, tablefmt="outline"))
                        else:
                            print('Barcode does not exist.')
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
        'Soap' : [3001, 'Non Food', 'Soap', 'pcs', 12000, 5],
        'Cooking Oil' : [1002, 'Food', 'Cooking Oil', 'pcs', 14000, 7],
        'Rice' : [1003, 'Food', 'Rice', 'pcs', 60000, 3],
        'Lamp' : [3004, 'Non Food', 'Lamp','pcs', 35000, 8],
        'Lotus Biscuits' : [1005, 'Food', 'Lotus Biscuits', 'pcs', 43000, 9],
        }
    #Format Item
    formatItem = "{:<2}" + "{:<12}" + "{:<13}" + "{:<18}" + "{:<8}" + "{:<10}" + "{:<15}"
    #Menjalankan fungsi utama main()
    main()