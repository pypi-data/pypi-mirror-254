class ols:
    def __init__(self) -> None:
        self.row = None
        self.column = None

    def set_row_column(self, parra) -> None:
        self.row = len(parra)
        self.column = len(parra[0]) if self.row > 0 else 0

    def transpose(self, parra) -> None:
        return [list(i) for i in zip(*parra)]

    def multiply_matrices(self, A, B) -> None:
        result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        return result

    def gauss_jordan_inverse(self, parra) -> None:
        n = len(parra)
        identity = [[float(i == j) for i in range(n)] for j in range(n)]
        for fd in range(n):
            fd_scaler = 1.0 / parra[fd][fd]
            for j in range(n):
                parra[fd][j] *= fd_scaler
                identity[fd][j] *= fd_scaler
            for i in list(range(n))[0:fd] + list(range(n))[fd+1:]:
                cr_scaler = parra[i][fd]
                for j in range(n):
                    parra[i][j] = parra[i][j] - cr_scaler * parra[fd][j]
                    identity[i][j] = identity[i][j] - cr_scaler * identity[fd][j]
        return identity

    def get_weights(self, X, Y) -> None:
        self.set_row_column(X)
        X_transposed = self.transpose(X)
        XTX = self.multiply_matrices(X_transposed, X)
        XTX_inv = self.gauss_jordan_inverse(XTX)
        XTY = self.multiply_matrices(X_transposed, [[y] for y in Y])
        weights = self.multiply_matrices(XTX_inv, XTY)
        return [w[0] for w in weights]