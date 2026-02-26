bracket = input("Введіть дужку: ")

if bracket == "(" or bracket == ")":
    print("Кругла дужка")
elif bracket == "[" or bracket == "]":
    print("Квадратна дужка")
elif bracket == "{" or bracket == "}":
    print("Фігурна дужка")
else:
    print("Це не дужка")