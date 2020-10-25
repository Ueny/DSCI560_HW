from random import uniform
import matplotlib.pyplot as plt

output_file = 'random_numbers.csv'

def main():
    x = range(1, 1001)
    y = []
    with open(output_file, 'w') as f:
        for num in range(1000):
            v = uniform(0, 100)
            y.append(v)
            f.write(str(v) + '\n')
    plt.scatter(x, y, s=4, alpha=1)
    plt.xlabel('number ID')
    plt.ylabel('number values')
    plt.title('The distribution of 1000 random numbers from 0 to 100')
    plt.show()

if __name__ == '__main__':
    main()