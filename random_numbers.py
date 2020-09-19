from random import uniform

output_file = 'random_numbers.csv'

def main():
    with open(output_file, 'w') as f:
        for num in range(1000):
            f.write(str(uniform(0, 100)) + '\n')


if __name__ == '__main__':
    main()