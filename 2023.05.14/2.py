def taxi_cost(route_length: int, waiting_time: int = 0) -> int | None:

    """Вычисляет и возвращает стоимость поездки, если вычисление невозможно возвращает None"""
    
    base_cost = 80
    time_cost = waiting_time * 3
    lenght_cost = route_length / 150 * 6
    find = 80    
    
    if route_length >= 0 and waiting_time >= 0:
    
        if route_length == 0:
            return base_cost + find  + time_cost
        if route_length < 150:
            return base_cost + time_cost    
        return round(base_cost + lenght_cost + time_cost)
             
# делала через переменные на случай если будет изменение тарифов))
# >>> taxi_cost(42130,8)
# 1789
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(0,5)
# 175
# >>> print(taxi_cost(150,-10))
# None
# >>> print(taxi_cost(-150,10))
# None
# >>> taxi_cost(149)
# 80
# >>> taxi_cost(150)
# 86