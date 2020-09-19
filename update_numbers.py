
input_file = 'random_numbers.txt'
output_file = 'update_numbers.txt'

def main():
    with open(input_file, 'r') as fr:
        with open(output_file, 'w') as fw:
            number = fr.readline()
            while(number):
                fw.write(str(3 * float(number) + 6) + '\n')
                number = fr.readline()

if __name__ == '__main__':
    main()