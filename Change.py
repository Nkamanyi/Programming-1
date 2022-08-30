
def main():
    purchase_cost = int(input("Purchase price: "))
    amount_paid = int(input("Paid amount of money: "))
    if amount_paid > purchase_cost:
        print("Offer change:")
    if (amount_paid-purchase_cost)//10 > 0:
        print((amount_paid-purchase_cost)//10, "ten-euro notes")
    if ((amount_paid-purchase_cost)%10)//5 > 0:
        print(((amount_paid-purchase_cost)%10)//5, "five-euro notes")
    if (((amount_paid-purchase_cost)%10)%5)//2 > 0:
        print((((amount_paid-purchase_cost)%10)%5)//2, "two-euro coins")
    if ((((amount_paid-purchase_cost)%10)%5)%2)//1 > 0:
        print(((((amount_paid-purchase_cost)%10)%5)%2)//1, "one-euro coins")
    if amount_paid <= purchase_cost:
        print("No change")

main()