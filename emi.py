def get_emi(p,n,r):
    """E = p x r x (1+r)^n/((1+r)^n - 1, where 

    E = Equated Monthly Instalment
    p stands for principal amount
    r denotes applicable rate of interest
    n stands for the loan term or tenure"""

    n = n * 12
    r = r / 12 / 100
    emi = round(p * r * (1 + r) ** n / (((1 + r) ** n) - 1))
    print(emi)

    outstanding_principal = p
    components = []
    for month in range(1, n+1):
        int_component = outstanding_principal * r
        prin_component = emi - int_component

        outstanding_principal = outstanding_principal - prin_component

        components.append(
            (
                month, 
                round(prin_component), 
                round(int_component), 
                round(outstanding_principal)
            )
        )

    return emi, components


if __name__ == '__main__':
    principal = 1000000
    no_of_year = 1
    rate_of_interest = 7.2

    get_emi(principal, no_of_year, rate_of_interest)



