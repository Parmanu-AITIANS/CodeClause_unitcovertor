def convert_distance():
    print("This program converts kilometers to miles.")
    km = float(input("Enter the distance in kilometers: "))
    miles = km / 1.609
    print(f"That is {miles} miles.")

def convert_temperature():
    print("This program converts Celsius to Fahrenheit.")
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"That is {fahrenheit} degrees Fahrenheit.")

def main():
    while True:
        print("Please select an option:")
        print("1. Convert kilometers to miles")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            convert_distance()
        elif choice == "2":
            convert_temperature()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
