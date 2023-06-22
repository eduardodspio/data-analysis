import numpy as np

def calculate(list):
    if (len(list) !=9):
        raise ValueError("List must contain nine numbers.")
      
    ls = np.array(list)
    print(ls)

    mean_rowns = [ls[[0, 1, 2]].mean(), ls[[3, 4, 5]].mean(), ls[[6, 7, 8]].mean()]
    mean_columns = [ls[[0, 3, 6]].mean(), ls[[1, 4, 7]].mean(), ls[[2, 5, 8]].mean()]

    var_rowns = [ls[[0, 1, 2]].var(), ls[[3, 4, 5]].var(), ls[[6, 7, 8]].var()]
    var_columns = [ls[[0, 3, 6]].var(), ls[[1, 4, 7]].var(), ls[[2, 5, 8]].var()]

    std_rowns = [ls[[0, 1, 2]].std(), ls[[3, 4, 5]].std(), ls[[6, 7, 8]].std()]
    std_columns = [ls[[0, 3, 6]].std(), ls[[1, 4, 7]].std(), ls[[2, 5, 8]].std()]

    max_rowns = [ls[[0, 1, 2]].max(), ls[[3, 4, 5]].max(), ls[[6, 7, 8]].max()]
    max_columns = [ls[[0, 3, 6]].max(), ls[[1, 4, 7]].max(), ls[[2, 5, 8]].max()]

    min_rowns = [ls[[0, 1, 2]].min(), ls[[3, 4, 5]].min(), ls[[6, 7, 8]].min()]
    min_columns = [ls[[0, 3, 6]].min(), ls[[1, 4, 7]].min(), ls[[2, 5, 8]].min()]

    sum_rowns = [ls[[0, 1, 2]].sum(), ls[[3, 4, 5]].sum(), ls[[6, 7, 8]].sum()]
    sum_columns = [ls[[0, 3, 6]].sum(), ls[[1, 4, 7]].sum(), ls[[2, 5, 8]].sum()]


#rowns:

#ls[[0, 1, 2]] selects the elements at indices 0, 1, and 2 from the array ls. This corresponds to the first row of the array.
#ls[[3, 4, 5]] selects the elements at indices 3, 4, and 5 from the array ls. This corresponds to the second row of the array.
#ls[[6, 7, 8]] selects the elements at indices 6, 7, and 8 from the array ls. This corresponds to the third row of the array.

#columns:

#ls[[0, 3, 6]] selects the elements at indices 0, 3, and 6 from the array ls. This corresponds to the first column of the array.
#ls[[1, 4, 7]] selects the elements at indices 1, 4, and 7 from the array ls. This corresponds to the second column of the array.
#ls[[2, 5, 8]] selects the elements at indices 2, 5, and 8 from the array ls. This corresponds to the third column of the array.


    return {
        'mean': [mean_columns, mean_rowns, ls.mean()],
        'variance': [var_columns, var_rowns, ls.var()],
        'standard deviation': [std_columns, std_rowns, ls.std()],
        'max': [max_columns, max_rowns, ls.max()],
        'min': [min_columns, min_rowns, ls.min()],
        'sum': [sum_columns, sum_rowns, ls.sum()],
    }
