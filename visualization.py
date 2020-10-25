import matplotlib.pyplot as plt

input_file1 = 'random_numbers.csv'
input_file2 = 'update_numbers.csv'
output_file = 'visualization.jpg'

def visualize(x, y):
    plt.scatter(x, y, alpha=0.6, s=1)
    plt.xlabel('number id')
    plt.ylabel('number value')
    plt.title('The distribution of 1000 random numbers for the function y = 3x + 6')
    plt.savefig(output_file)
    plt.show()

def main():
    with open(input_file1, 'r') as f:
        x = list(map(float, f.readlines()))
    with open(input_file2, 'r') as f:
        y = list(map(float, f.readlines()))
    visualize(x, y)

if __name__ == '__main__':
    main()