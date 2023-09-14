def bubbleSort(dataset):
    """
    implementation of sorting algoritmn
    """
    print('current state: {}'.format(dataset))
    for i in range(len(dataset)):
        # print(dataset[i])
        for j in range(len(dataset)-1 -i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp 
                
            
                
                
       


def main():
    """
    This is the main body
    """
    list = [6,20,8,9,87,49,53,56,19]
    bubbleSort(list)
    print("Result: {}".format(list))


if __name__ == "__main__":
    main()