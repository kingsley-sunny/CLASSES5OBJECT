# BUDGET CLASS PROJECT
class Budget:
    def __init__(self, process):
        self.process = 0

    def deposit(self):
        depo = int(input('how much did you want to deposit: \n'))
        self.process += depo
        print(f'you have deposited ${depo} to your account and your remaining balance is ${self.process}')

    def withdraw(self):
        withr = int(input('How much did you want to withdraw: \n'))
        self.process -= withr
        print(f'you have received ${withr} to your account and your remaining balance is ${self.process}')

    def transfer(self):
        transf = int(input('How much did you want to transfer: \n'))
        to_whr = str(input('To which category: \n'))
        self.process -= transf
        print(f'you have suuccesfully transferred {transf} to {to_whr} category')

    def check_bal(self):
        self.process()

    def budget(self):
        print('''
            please select the following options of budget class from 1-3
            1.  food
            2.  clothing
            3.  entertainment
        ''')
        budget_option = int(input('please select the following options: \n'))
        if budget_option == 1:
            print(f'WELCOME TO FOOD CATEGORY. THIS ARE THE FOLLOWING OPTIONS')
            print('''
                These arev the following options:
                1.  deposit
                2.  withdraw
                3.  transfer
                4.  Check balance
            ''')
            options = int(input('please select the following options: \n'))
            if options == 1:
                food.deposit()
            elif options == 2:
                food.withdraw()
            elif options == 3:
                food.transfer()
            elif options == 4:
                print(f'this is your remaining balance ${self.process}')

        elif budget_option == 2:
            print(f'WELCOME TO CLOTHING CATEGORY. THIS ARE THE FOLLOWING OPTIONS')
            print('''
                These arev the following options:
                1.  deposit
                2.  withdraw
                3.  transfer
                4.  Check balance
            ''')
            options = int(input('please select the following options: \n'))
            if options == 1:
                food.deposit()
            elif options == 2:
                food.withdraw()
            elif options == 3:
                food.transfer()
            elif options == 4:
                print(f'this is your remaining balance ${self.process}')

        if budget_option == 3:
            print(f'WELCOME TO ENTERTAINMENT CATEGORY. THIS ARE THE FOLLOWING OPTIONS')
            print('''
                These arev the following options:
                1.  deposit
                2.  withdraw
                3.  transfer
                4.  Check balance
            ''')
            options = int(input('please select the following options: \n'))
            if options == 1:
                food.deposit()
            elif options == 2:
                food.withdraw()
            elif options == 3:
                food.transfer()
            elif options == 4:
                print(f'this is your remaining balance ${self.process}')



    





food = Budget(0)
clothing = Budget(0)
entertainment = Budget(0)
food.budget()