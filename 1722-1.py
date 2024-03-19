# Machine Learning class HW1(K-means) 1101722 林峻毅
import math
import random
import matplotlib.pyplot as plt

def add_random_piece(chessboard, total_number_points):
    # Random add new data
    for i in range((total_number_points - 15)):
        new_piece = [random.randint(1, 10000), random.randint(1, 10000)]
        
        if (new_piece in chessboard):
            new_piece = [random.randint(1, 10000), random.randint(1, 10000)]
        chessboard.append(new_piece)
    return chessboard

def search_grouping(chessboard, chessboard_point_information, initial_code_word_values_list):
    # Search(Grouping/Partition) function
    for i in range(len(chessboard)):
        point = chessboard[i]
        # initial comparison
        short_distance_point = -1
        for j in range(len(initial_code_word_values_list)):
            distance = math.sqrt((point[0] - initial_code_word_values_list[j][0]) ** 2 + (point[1] - initial_code_word_values_list[j][1]) ** 2)
            if j == 0:
                short_code_word_values = distance
                short_distance_point = j
            elif distance < short_code_word_values:
                short_code_word_values = distance
                short_distance_point = j
        chessboard_point_information.append(short_distance_point)
    return chessboard_point_information   

def update_code_word_values_list(chessboard_point_information, update_code_word_values, initial_code_word_values, initial_chessboard):  
    # Update(function)
    dimensions = len(initial_chessboard[0])  
    
    for i in range(len(initial_code_word_values)):
        vector_sum = [0] * dimensions  
        count = 0
        for j in range(len(initial_chessboard)):
            if i == chessboard_point_information[j]:
                count += 1
                for dim in range(dimensions):
                    vector_sum[dim] += initial_chessboard[j][dim]
        result_vector = [number / count for number in vector_sum]
        
        update_code_word_values.append(result_vector)
        
    return update_code_word_values

def loss_fn(chessboard_point_information, update_code_word_values, initial_chessboard):   
    # Search(Grouping/Partition) function 
    distance = 0
    count = 0
    for i in range(len(initial_chessboard)):
        code_word_point = chessboard_point_information[i]
        code_word_value = update_code_word_values[code_word_point]
        point_value = initial_chessboard[i]
        temp_distance = math.sqrt((point_value[0] - code_word_value[0]) ** 2 + (point_value[1] - code_word_value[1]) ** 2)
        count += 1
        distance = distance + temp_distance

    loss = distance / count
    return loss


def main():
    # Initialization
    # build initial chessboard
    before_initial_chessboard = [[5, 2], [4, 3], [3, 3], [2, 3], [4, 4], [3, 4],
                                 [6, 6], [4, 6], [3, 6], [7, 7], [6, 7], [5, 7],
                                 [2, 7], [7, 8], [6, 8]]
    initial_code_word_values = [[2, 2], [6, 4], [5, 6], [8, 8]]
    total_number_points = 10000
    # random add
    # initial_chessboard = add_random_piece(before_initial_chessboard, total_number_points)
    # 15
    initial_chessboard = before_initial_chessboard
    # build chessboard each point information(for eachtime)
    loss_list = []
    epochs_list = []
    word_values = initial_code_word_values
    for i in range(40):
        # build the chessboard information to put each position closed word value
        chessboard_point_information = []
        # initial_chessboard is initial value
        # To searched closed position information
        chessboard_point_information = search_grouping(initial_chessboard, chessboard_point_information, word_values)

        update_code_word_values = []
        update_code_word_values = update_code_word_values_list(chessboard_point_information, update_code_word_values, initial_code_word_values, initial_chessboard)
        
        loss = loss_fn(chessboard_point_information, update_code_word_values, initial_chessboard)
        loss_list.append(loss)
        epochs_list.append(i)
        word_values = update_code_word_values
    
    plt.plot(epochs_list, loss_list, marker='o', linestyle='-')

    plt.title('Loss Function over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    plt.show()

if __name__ == "__main__":
    main()