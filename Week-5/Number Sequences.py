
def even_acc_num():
    """
    :return: this function returns the even number from 1 to 100 in ascending order
    """
    for i in range(0,101,1):
        if i%2 ==0:
            print(i)


def even_dec_num():
    """
    :return: this function returns the even number from 1 to 100 in descending order
    """
    for k in range(100,-1,-1):
        if k%2==0:
            print(k)

def main():
    even_acc_num()
    even_dec_num()

main()
