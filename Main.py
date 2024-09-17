#Health Management System

def function():

    print("\nDo You Want To Continue\nPress Y to Continue\nPress N To Cancel")
    inp = input()

    if "Y" or 'y' in inp:
        True
    if 'N' or 'n' in inp:
        print("\nThanku You For Visit Himanshu's Project")
        print("Visit Again!!!!!!!!!!!!")
        exit()


while True:
    print("Please Input Your Name You Want To see The Report  :-    ")

    print("1 For Himanshu \n2 For Vishal\n3 For Vivek")

    Inpnum = input(int())


    if '1' in Inpnum:
        print("Please Press '1' For Excercise Log & '2' For Diet Log")
        H1 = input(int())
        if '1' in H1:
            print("Your Data For Himanshu Excercise Log Is here")
            with open("himanshu Ex.txt") as H_File:
                H = H_File.read()
                print(H)
            function()
        elif '2' in H1:
            print("Your Data For Himanshu Diet Log Is here")
            with open("himanshu.txt") as Diet:
                Diet_File = Diet.read()
                print(Diet_File)
            function()

    if '2' in Inpnum:
        print("Please Press '1' For Excercise Log & '2' For Diet Log")
        Vishal = input(int())
        if '1' in Vishal:
            print("Your Data For Vishal Excercise Log Is here")
            with open("vishal Ex.txt") as Excercise:
                V1 = Excercise.read()
                print(V1)
            function()
        elif '2' in Vishal:
            print("Your Data For Vishal Diet Log Is here")
            with open("vishal.txt") as Diet1:
                V2 = Diet1.read()
                print(V2)
            function()

    if '3' in Inpnum:
        print("Please Press '1' For Excercise Log & '2' For Diet Log")
        Vivek = input(int())
        if '1' in Vivek:
            print("Your Data For Vivek Excercise Log Is here")
            with open("vivek Ex.txt") as Excercise1:
                V1 = Excercise1.read()
                print(V1)
            function()
        elif '2' in Vivek:
            print("Your Data For Vivek Diet Log Is here")
            with open("vivek.txt") as Diet2:
                V2 = Diet2.read()
                print(V2)
            function()
        

