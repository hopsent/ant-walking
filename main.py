def get_sum(x, y):
    """Возвращает сумму всех цифр в координатах."""
    return sum(map(int, str(x)+str(y)))

def ant_walking(x, y):

    visited = []
    to_visit = [(x, y)]

    while to_visit:

        visited.append((x, y))
        observed = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        to_visit += [
            node for node in observed
            if get_sum(*node) < 26 and node not in visited and node not in to_visit
        ]
        x, y = to_visit.pop()
    
    return len(visited)

if __name__ == '__main__':
    x, y = 1000, 1000
    print(ant_walking(x, y))
