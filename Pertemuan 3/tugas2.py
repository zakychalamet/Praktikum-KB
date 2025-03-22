import random
import time

def main():
    menu = {
        "1": ("Manchester by the Sea", 35000),
        "2": ("Dune: Part Two", 45000),
        "3": ("500 Days of Summers", 50000)
    }
    total = 0
    
    print("Pilih film yang ingin anda tonton:")
    for key in menu:
        name, price = menu[key]
        print(key + ". " + name + " - Rp" + str(price))
    
    while True:
        choice = input("Pilih menu (0 untuk selesai): ")
        if choice == "0":
            break
        elif choice in menu:
            total += menu[choice][1]
            print("Ditambahkan: " + menu[choice][0] + ". Total: Rp" + str(total))
        else:
            print("Pilihan tidak valid.")
    
    transaction_id = "TRX-" + str(random.randint(1000, 9999))
    transaction_time = time.ctime()
    
    print("Total bayar: Rp" + str(total))
    print("ID Transaksi: " + transaction_id)
    print("Waktu Transaksi: " + transaction_time)
    print("Terima kasih!")

if __name__ == "__main__":
    main()