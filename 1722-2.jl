using Random
using Statistics
using Plots

function add_random_piece(chessboard, total_number_points)
    # Randomly add new data
    for i in 1:(total_number_points-15)
        new_piece = [rand(1:10000), rand(1:10000)]

        while new_piece in chessboard
            new_piece = [rand(1:10000), rand(1:10000)]
        end

        push!(chessboard, new_piece)
    end
    return chessboard
end

function search_grouping(chessboard, chessboard_point_information, initial_code_word_values_list)
    # Search (Grouping/Partition) function
    for point in chessboard
        # Initial comparison
        short_distance_point = -1
        short_code_word_values = 0
        for (j, code_word) in enumerate(initial_code_word_values_list)
            distance = sqrt((point[1] - code_word[1])^2 + (point[2] - code_word[2])^2)
            if j == 1
                short_code_word_values = distance
                short_distance_point = j
            elseif distance < short_code_word_values
                short_code_word_values = distance
                short_distance_point = j
            end
        end
        push!(chessboard_point_information, short_distance_point)
    end
    return chessboard_point_information
end

function update_code_word_values_list(chessboard_point_information, update_code_word_values, initial_code_word_values, initial_chessboard)
    # Update function
    for (i, _) in enumerate(initial_code_word_values)
        x = 0
        y = 0
        count = 0
        for (j, _) in enumerate(initial_chessboard)
            if i == chessboard_point_information[j]
                count += 1
                x += initial_chessboard[j][1]
                y += initial_chessboard[j][2]
            end
        end
        result_x = x / count
        result_y = y / count
        push!(update_code_word_values, [result_x, result_y])
    end
    return update_code_word_values
end

function loss_fn(chessboard_point_information, update_code_word_values, initial_chessboard)
    # Loss function
    distance = 0
    count = 0
    for (i, _) in enumerate(initial_chessboard)
        code_word_point = chessboard_point_information[i]
        code_word_value = update_code_word_values[code_word_point]
        point_value = initial_chessboard[i]
        temp_distance = sqrt((point_value[1] - code_word_value[1])^2 + (point_value[2] - code_word_value[2])^2)
        count += 1
        distance += temp_distance
    end
    loss = distance / count
    return loss
end

function main()
    # Initialization
    before_initial_chessboard = [[5, 2], [4, 3], [3, 3], [2, 3], [4, 4], [3, 4],
        [6, 6], [4, 6], [3, 6], [7, 7], [6, 7], [5, 7],
        [2, 7], [7, 8], [6, 8]]
    initial_code_word_values = [[2, 2], [6, 4], [5, 6], [8, 8]]
    total_number_points = 10000
    initial_chessboard = add_random_piece(copy(before_initial_chessboard), total_number_points)

    loss_list = Float64[]
    epochs_list = Int[]
    word_values = copy(initial_code_word_values)

    for i in 1:40
        chessboard_point_information = Int[]
        chessboard_point_information = search_grouping(initial_chessboard, chessboard_point_information, word_values)

        update_code_word_values = Vector{Vector{Float64}}()
        update_code_word_values = update_code_word_values_list(chessboard_point_information, update_code_word_values, initial_code_word_values, initial_chessboard)

        loss = loss_fn(chessboard_point_information, update_code_word_values, initial_chessboard)
        push!(loss_list, loss)
        push!(epochs_list, i)
        word_values = copy(update_code_word_values)
    end

    plot(epochs_list, loss_list, marker="o", linestyle="-", color="red")
    title("Loss Function over Epochs")
    xlabel("Epochs")
    ylabel("Loss")
    show()
end

main()
