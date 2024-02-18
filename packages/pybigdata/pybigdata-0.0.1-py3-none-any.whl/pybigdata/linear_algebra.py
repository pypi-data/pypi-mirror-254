class Matrix:
    def __init__(self, data=None):
        self.__data = data if data is not None else [[]]

    def get_num_rows(self):
        return len(self.__data)

    def get_num_cols(self):
        return len(self.__data[0])

    def get_row(self, r):
        return self.__data[r]

    def get_column(self, c):
        col = []
        for i in self.__data:
            col.append(i[c])
        return col

    def set_row(self, index, row):
        self.__data[index] = row

    def set_column(self, index, col):
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                if index == j:
                    self.__data[i][j] = col[j]

    def set_values(self, L):
        self.__data = L

    def fill(self, rows, cols, n):
        self.__data = [[n] * cols for _ in range(rows)]

    def T(self):
        transposed_matrix = Matrix()
        transposed_matrix.fill(self.get_num_rows(), self.get_num_cols(), 0)
        transposed_matrix.__data = [list(row) for row in zip(*self.__data)]
        return transposed_matrix

    def det(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for determinant calculation!")

        if self.get_num_rows() == 1:
            return self.__data[0][0]
        elif self.get_num_rows() == 2:
            return (
                self.__data[0][0] * self.__data[1][1]
                - self.__data[0][1] * self.__data[1][0]
            )
        else:
            determinant = 0
            for col in range(self.get_num_cols()):
                cofactor = self.__data[0][col] * self.get_submatrix_determinant(0, col)
                determinant += cofactor if col % 2 == 0 else -cofactor
            return determinant

    def get_submatrix_determinant(self, row, col):
        subdata = []
        for i in range(self.get_num_rows()):
            if i != row:
                subrow = [
                    self.__data[i][j] for j in range(self.get_num_cols()) if j != col
                ]
                subdata.append(subrow)
        submatrix = Matrix(subdata)
        return submatrix.det()

    def inverse(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for inverse calculation!")

        if self.is_singular():
            raise ValueError("Matrix is singular, inverse does not exist!")

        augmented_matrix = [
            row + [1 if i == j else 0 for j in range(self.get_num_cols())]
            for i, row in enumerate(self.__data)
        ]

        for col in range(self.get_num_cols()):
            pivot_row = max(
                range(col, self.get_num_rows()),
                key=lambda i: abs(augmented_matrix[i][col]),
            )

            augmented_matrix[col], augmented_matrix[pivot_row] = (
                augmented_matrix[pivot_row],
                augmented_matrix[col],
            )

            pivot_element = augmented_matrix[col][col]
            augmented_matrix[col] = [
                element / pivot_element for element in augmented_matrix[col]
            ]

            for row in range(self.get_num_rows()):
                if row != col:
                    factor = augmented_matrix[row][col]
                    augmented_matrix[row] = [
                        x - factor * y
                        for x, y in zip(augmented_matrix[row], augmented_matrix[col])
                    ]

        inversed_matrix = [row[self.get_num_cols() :] for row in augmented_matrix]

        return Matrix(inversed_matrix)

    def trace(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for trace calculation!")
        return sum(self.__data[i][i] for i in range(self.get_num_rows()))

    def is_singular(self):
        return self.det() == 0

    def is_squared(self):
        return self.get_num_rows() == self.get_num_cols()

    def is_identity(self):
        return self.is_squared() and all(
            self.__data[i][j] == 1 if i == j else self.__data[i][j] == 0
            for i in range(self.get_num_rows())
            for j in range(self.get_num_cols())
        )

    def is_sparse(self):
        count = sum(
            1
            for i in range(self.get_num_rows())
            for j in range(self.get_num_cols())
            if self.__data[i][j] == 0
        )
        return count > ((self.get_num_rows() * self.get_num_cols()) // 2)

    def is_symmetric(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for symmetry check!")

        for i in range(self.get_num_rows()):
            for j in range(i + 1, self.get_num_cols()):
                if self.__data[i][j] != self.__data[j][i]:
                    return False
        return True

    def is_orthogonal(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for orthogonality check!")

        transpose_matrix = self.T()
        identity_matrix = self * transpose_matrix

        return identity_matrix.is_identity()

    def is_orthonormal(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for orthonormality check!")

        transpose_matrix = self.T()
        product_matrix = self * transpose_matrix

        return self.is_orthogonal() and all(
            self.is_unit_vector(row) for row in product_matrix.__data
        )

    def is_unit_vector(self, vector):
        return sum(x**2 for x in vector) == 1

    def is_triangular(self):
        n = self.get_num_rows()
        # Check if it is upper triangular
        for i in range(n):
            for j in range(i + 1, n):
                if self.__data[i][j] != 0:
                    return False
        # Check if it is lower triangular
        for i in range(1, n):
            for j in range(i):
                if self.__data[i][j] != 0:
                    return False
        return True

    def is_diagonal(self):
        n = self.get_num_rows()
        for i in range(n):
            for j in range(n):
                if i != j and self.__data[i][j] != 0:
                    return False
        return True

    def power_iteration(self, num_iterations, start_vector=None):
        n = self.get_num_rows()
        v = start_vector or [1.0] * n

        for _ in range(num_iterations):
            w = [sum(self.__data[i][j] * v[j] for j in range(n)) for i in range(n)]
            eigenvalue = max(w)
            v = [wi / eigenvalue for wi in w]

        return eigenvalue, v

    def deflate(self, eigenvalue):
        n = self.get_num_rows()
        identity = Matrix(
            [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        )
        self.__data = [
            [self.__data[i][j] - eigenvalue * identity.__data[i][j] for j in range(n)]
            for i in range(n)
        ]

    def eigenvalues(self, num_eigenvalues=1, num_iterations=50):
        if not self.is_squared():
            raise ValueError("Matrix must be square for eigenvalue calculation!")

        eigenvalues = []
        for _ in range(num_eigenvalues):
            eigenvalue, _ = self.power_iteration(num_iterations)
            eigenvalues.append(eigenvalue)
            self.deflate(eigenvalue)

        return eigenvalues

    def eigenvectors(self, eigenvalues, num_iterations=50):
        if not self.is_squared():
            raise ValueError("Matrix must be square for eigenvector calculation!")

        eigenvectors = []
        for eigenvalue in eigenvalues:
            _, eigenvector = self.power_iteration(
                num_iterations, start_vector=[1.0] * self.get_num_rows()
            )
            eigenvectors.append(eigenvector)
            self.deflate(eigenvalue)

        return eigenvectors

    def lu_decomposition(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for LU decomposition!")

        n = self.get_num_rows()
        L = Matrix([[0] * n for _ in range(n)])
        U = Matrix([[0] * n for _ in range(n)])

        for i in range(n):
            # Upper triangular matrix
            for j in range(i, n):
                sum_val = sum(L.__data[i][k] * U.__data[k][j] for k in range(i))
                U.__data[i][j] = self.__data[i][j] - sum_val

            # Lower triangular matrix
            for j in range(i, n):
                if i == j:
                    L.__data[i][i] = 1
                else:
                    sum_val = sum(L.__data[j][k] * U.__data[k][i] for k in range(i))
                    L.__data[j][i] = (self.__data[j][i] - sum_val) / U.__data[i][i]

        return L, U

    def qr_decomposition(self):
        # By using Gram-Schmidt algorithm
        if not self.is_squared():
            raise ValueError("Matrix must be square for QR decomposition!")

        n = self.get_num_rows()
        Q = Matrix([[0] * n for _ in range(n)])
        R = Matrix([[0] * n for _ in range(n)])

        for j in range(n):
            v = self.get_column(j)
            for i in range(j):
                R.__data[i][j] = sum(Q.__data[k][i] * v[k] for k in range(n))
                v = [vi - R.__data[i][j] * Qi for vi, Qi in zip(v, Q.get_column(i))]

            R.__data[j][j] = sum(vi**2 for vi in v) ** 0.5
            Q.set_column(j, [vi / R.__data[j][j] for vi in v])

        return Q, R

    def cholesky_decomposition(self):
        if not self.is_squared():
            raise ValueError("Matrix must be square for Cholesky decomposition!")

        n = self.get_num_rows()
        L = Matrix([[0] * n for _ in range(n)])

        for i in range(n):
            for j in range(i + 1):
                if i == j:
                    sum_val = sum(L[i][k] ** 2 for k in range(j))
                    L[i][j] = (self.__data[i][j] - sum_val) ** 0.5
                else:
                    sum_val = sum(L[i][k] * L[j][k] for k in range(j))
                    L[i][j] = (1 / L[j][j]) * (self.__data[i][j] - sum_val)

        return L

    def __add__(self, X):
        if (
            self.get_num_rows() == X.get_num_rows()
            and self.get_num_cols() == X.get_num_cols()
        ):
            C = Matrix()
            C.fill(self.get_num_rows(), self.get_num_cols(), 0)
            C.__data = [
                [self.__data[i][j] + X.__data[i][j] for j in range(self.get_num_cols())]
                for i in range(self.get_num_rows())
            ]
            return C
        else:
            raise ValueError("These two datatypes should have the same orders!")

    def __sub__(self, X):
        if (
            self.get_num_rows() == X.get_num_rows()
            and self.get_num_cols() == X.get_num_cols()
        ):
            C = Matrix()
            C.fill(self.get_num_rows(), self.get_num_cols(), 0)
            C.__data = [
                [self.__data[i][j] - X.__data[i][j] for j in range(self.get_num_cols())]
                for i in range(self.get_num_rows())
            ]
            return C
        else:
            raise ValueError("These two datatypes should have the same orders!")

    def __mul__(self, X):
        if X.get_num_rows() != self.get_num_cols():
            raise ValueError(
                "The columns order of the first matrix is not equal to the rows order of the second matrix!"
            )

        C = Matrix()
        C.fill(self.get_num_rows(), X.get_num_cols(), 0)
        for i in range(self.get_num_rows()):
            for k in range(self.get_num_cols()):
                for j in range(X.get_num_cols()):
                    C.__data[i][j] += self.__data[i][k] * X.__data[k][j]
        return C

    def __pow__(self, exponent):
        if not self.is_squared():
            raise ValueError("Matrix must be square for matrix exponentiation!")

        if exponent < 0:
            raise ValueError("Exponent must be non-negative for matrix exponentiation!")

        result_matrix = Matrix(
            [
                [1 if i == j else 0 for j in range(self.get_num_cols())]
                for i in range(self.get_num_rows())
            ]
        )

        for _ in range(exponent):
            result_matrix *= self

        return result_matrix

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.__data])
