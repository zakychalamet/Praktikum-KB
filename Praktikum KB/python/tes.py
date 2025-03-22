import random
import time

def main():
    tickets = {
        "1": ("Manchester by the Sea", 35000),
        "2": ("Dune: Part Two", 45000),
        "3": ("La La Land", 50000)
    }
    total = 0
    booked_tickets = []
    
    print("Pilih Film yang ingin anda tonton:")
    for key in tickets:
        name, price = tickets[key]
        print(key + ". " + name + " - Rp" + str(price))
    
    while True:
        choice = input("Pilih tiket (0 untuk selesai): ")
        if choice == "0":
            break
        elif choice in tickets:
            booked_tickets.append(tickets[choice])
            total += tickets[choice][1]
            print("Ditambahkan: " + tickets[choice][0] + ". Total: Rp" + str(total))
        else:
            print("Pilihan tidak valid.")
    
    transaction_id = "TICK-" + str(random.randint(1000, 9999))
    transaction_time = time.ctime()
    
    print("\nRingkasan Pemesanan:")
    for ticket in booked_tickets:
        print("- " + ticket[0] + " - Rp" + str(ticket[1]))
    print("Total bayar: Rp" + str(total))
    print("ID Transaksi: " + transaction_id)
    print("Waktu Transaksi: " + transaction_time)
    print("Terima kasih telah memesan tiket!")

if __name__ == "__main__":
    main()