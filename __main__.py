#! python
from PersianUnicode import PersianUnicode
if __name__ == "__main__":
    pu = PersianUnicode();
    user = input("Type Persian: ")
    print("Normal: " + user);
    print("PersianUnicode: " + pu.convert(user));