import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=float)
parser.add_argument("--principal",type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)   
args = parser.parse_args()
error = "Incorrect parameters"

if args.type != "annuity" and args.type != "diff":
    print(error)
    exit()

numero_args = 0
for arg in args.__dict__:
    if args.__dict__[arg] != None:
        numero_args = numero_args + 1

if numero_args != 4:
    print(error)
    exit()

elif args.type == "diff":
    if args.payment != None:
        print(error)
        exit()
    else:
        i = args.interest / (12 * 100)
        total_pagos = 0
        for m in range(1, args.periods + 1):
            diff = args.principal / args.periods + i * (args.principal - (args.principal * (m-1)/args.periods))
            diff = math.ceil(diff)
            total_pagos = total_pagos + diff
            print("Month {}: paid out {}".format(m, round(diff)))
        print()
        over_payment = total_pagos - args.principal
        print("Overpayment = {}".format(math.ceil(over_payment)))
        pass
    pass 
    
elif args.type == "annuity": 
    if args.periods == None:
        principal_credit = args.principal
        monthly_p = args.payment
        credit_interest = args.interest
        i = credit_interest / (12 * 100)
        n = math.log(monthly_p/(monthly_p - i * principal_credit ),1+i)
        n = math.ceil(n)
        years = n // 12
        meses = n - (n // 12)*12
        meses = math.ceil(meses)
        if meses == 1:
            string_meses = "month"
        else:
            string_meses = "months"
        
        if years == 1:
            string_years = "year"
        else:
            string_years = "years"
            
        if years == 0:
            print("You need {} {} to repay this credit!".format(meses, string_meses))
        else:
            if meses == 0:
                print("You need {} {} to repay this credit!".format(years, string_years))
            else:
                print("You need {} {} and {} {} to repay this credit!".format(years, string_years, meses, string_meses))  
        over_payment = args.payment * n - args.principal
        print("Overpayment = {}".format(math.ceil(over_payment)))
                
    if args.payment == None:
        credit_principal = args.principal
        count = args.periods
        credit_interest = args.interest
        i = credit_interest / (12 * 100)
        a= credit_principal * (i * (1+i)**count/((1 + i)**count - 1) )
        a = math.ceil(a)
        print("Your annuity payment = {}!".format(round(a)))
        over_payment = a * count - args.principal
        print("Overpayment = {}".format(math.ceil(over_payment)))
        
    if args.principal == None:
        monthly_p = args.payment
        count = args.periods
        credit_interest = args.interest
        i = credit_interest / (12 * 100)
        annuity_p = monthly_p
        credit_principal = annuity_p / ((i * (1 + i)**count)/((1 + i)** count - 1))
        credit_principal = math.floor(credit_principal)
        print("Your credit principal = {}!".format(credit_principal))
        over_payment = args.payment * count - credit_principal
        print("Overpayment = {}".format(math.ceil(over_payment)))

