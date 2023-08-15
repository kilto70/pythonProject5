def calculate_ticket_price(age):
    if age < 18:
        return 0
    elif age < 25:
        return 990
    else:
        return 1390


def calculate_total_price(num_tickets):
    total_price = 0
    for i in range(num_tickets):
        age = int(input(f"Введите возраст посетителя {i + 1}-го билета: "))
        total_price += calculate_ticket_price(age)
    if num_tickets > 3:
        total_price *= 0.9
    return total_price


num_tickets = int(input("Введите количество билетов: "))
total_price = calculate_total_price(num_tickets)
print(f"Сумма к оплате: {total_price} руб.")