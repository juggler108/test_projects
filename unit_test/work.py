import matplotlib.pyplot as plt

data = {'Smartphone': 251, 'Computer': 340, 'Tablet': 50, 'TV': 10}


def percent(arr):
    return [i / sum(arr) * 100 for i in arr]


def test_arr(arr):
    return list(arr.keys()), list(arr.values())


def table(arr):
    if type(arr) != dict:
        raise TypeError
    index, values = test_arr(arr)

    plt.title('Analytics')
    plt.xlabel('Device')
    plt.ylabel('Indicator in pieces')
    plt.bar(index, percent(values))
    plt.show()


if __name__ == '__main__':
    table(data)
