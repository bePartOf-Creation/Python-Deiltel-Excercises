def calculate_investment_return(p: float, r: float, n: float):
    return p * (1 + r) ** n


def main():
    p_given = 1000
    r_given = 7 / 100
    years_given = [10, 20, 30]

    for years in years_given:
        inv_return = calculate_investment_return(p_given, r_given, years)
        print(f"Year, {years} returns = {inv_return:.2f}")


if __name__ == '__main__':
    main()