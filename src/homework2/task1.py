def total_sum(m, n, s):
    sum = (int(m) * 100 + int(n)) * int(s)
    ruble_amount = sum // 100
    kopek_amount = sum % 100

    return f"{ruble_amount} rubles {kopek_amount} kopeks"


if __name__ == "__main__":
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = "0", "5", "5"
    print(total_sum(m, n, s))
