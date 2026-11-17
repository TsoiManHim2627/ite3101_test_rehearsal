def main():
    while True:
        try:
            n = int(input("Type an integer:"))
            break
        except ValueError:
            print("Please enter an integer.")
    if n % 10 == 0 and n % 3 !=0:
            print(f'{n} is divisible by 10 and not divisble by 3.')
    else:
            print(f'{n} is not divisible by 10 or divisble by 3.")
        



if __name__ == "__main__":
    # execute only if run as a script
    main()