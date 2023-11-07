from dictionary import get_p_distance_matrix
#import dictionary

def is_valid_sequence(sequence):
    valid_chars = {'A', 'C', 'G', 'T', 'a', 'c', 'g', 't'}
    return all(char in valid_chars for char in sequence)

def get_valid_sequence_count():
    while True:
        n = input("Enter the number of sequences: ")
        if not n.isdigit():
            print("Invalid input. Please enter a valid number for the number of sequences.")
        else:
            return int(n)


while True:
    print("\nMenu:")
    print("1- Get P distance matrix")
    print("2- Exit")
    choice = input("Select an option: ")

    if choice == '1':
        n = get_valid_sequence_count()
        sequences = []
        length = None

        for i in range(n):
            sequence = input(f"Enter sequence {i + 1}: ").strip()
            if length is None:
                length = len(sequence)
            elif len(sequence) != length:
                print("The sequences you entered are not the same length, please try again:")
                break
            elif not is_valid_sequence(sequence):
                print("Invalid characters in the sequence. Please use only 'A', 'C', 'G', or 'T' (case-insensitive).")
                break
            sequences.append(list(sequence))
        else:
            distance_matrix = get_p_distance_matrix(sequences)
            print("P-distance matrix:")
            for row in distance_matrix:
                print(' '.join(f'{distance:.5f}' for distance in row))
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose 1 or 2.")