import matplotlib.pyplot as plt

input_file = 'random_numbers.csv'
output_file = 'update_numbers.csv'

def main():
    x = range(1, 1001)
    y = []
    with open(input_file, 'r') as fr:
        with open(output_file, 'w') as fw:
            number = fr.readline()
            while number:
                v = 3 * float(number) + 6
                y.append(v)
                fw.write(str(v) + '\n')
                number = fr.readline()
    plt.scatter(x, y, s=4, alpha=1)
    plt.xlabel('number ID')
    plt.ylabel('number values')
    plt.title('The distribution of 1000 after-function random numbers from 6 to 306')
    plt.show()

if __name__ == '__main__':
    main()