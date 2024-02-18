def matrix_dot(parra, vano) -> list:
    try:
        if not isinstance(parra, list) or not isinstance(vano, list):
            raise TypeError("Both input1 and input2 must be of type list.") # I can directly raise my question here
        # Check if the number of columns in input1 equals the number of rows in input2
        if len(parra[0]) != len(vano):
            raise ValueError("Matrices are not compatible for multiplication")
    
        # Initialize the output matrix with zeros
        rows_output = len(parra)
        cols_output = len(vano[0])
        output = [[0 for _ in range(cols_output)] for _ in range(rows_output)]  #so I create an empty list here. list in list.
    
        # Perform matrix multiplication
        for i in range(rows_output):
            for j in range(cols_output):
                for k in range(len(vano)):
                    output[i][j] += parra[i][k] * vano[k][j]
        return output
        
    except Exception as e:
        print(e)