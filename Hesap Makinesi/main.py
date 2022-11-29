# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Bir işlem komutu seçiniz.")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

while True:

    choice = input("İşlem yapmak istediğiniz sayıyı giriniz (1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("İlk sayıyı lütfen giriniz: "))
        num2 = float(input("İkinci numarayı lütfen giriniz: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_calculation = input("Hesap Makinesinin çalışmasını istiyor musunuz? (evet/hayır): ")
        if next_calculation == "hayır":
            break

    else:
        print("Geçersiz giriş yaptınız")