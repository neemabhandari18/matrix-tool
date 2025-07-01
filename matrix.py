import numpy as np  # NumPy is used for all matrix operations

# ───────────────────────────────────────────────
# Function to take matrix input from the user
# ───────────────────────────────────────────────
def input_matrix(name):
    """
    Takes matrix name (like A or B) and asks the user to input:
    - number of rows
    - number of columns
    - each row of the matrix
    Returns a NumPy 2D array.
    """
    # Ask user for number of rows and columns
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter the elements for {name}, one row at a time:")
    matrix = []

    # Loop through rows
    for i in range(rows):
        # Input a row, split into list of numbers
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)  # Convert to NumPy matrix

# ───────────────────────────────────────────────
# Function to display operation menu
# ───────────────────────────────────────────────
def show_menu():
    print("\n===== Matrix Operations =====")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Exit")

# ───────────────────────────────────────────────
# Main function
# ───────────────────────────────────────────────
def main():
    while True:
        show_menu()  # Show menu each time
        choice = input("Enter your choice (1-6): ")

        # ── 1. Matrix Addition ─────────────────
        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                result = A + B
                print("Result of A + B:\n", result)
            else:
                print("Error: Matrices must be the same size for addition.")

        # ── 2. Matrix Subtraction ──────────────
        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                result = A - B
                print("Result of A - B:\n", result)
            else:
                print("Error: Matrices must be the same size for subtraction.")

        # ── 3. Matrix Multiplication ───────────
        elif choice == "3":
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                result = np.dot(A, B)
                print("Result of A × B:\n", result)
            else:
                print("Error: Number of columns in A must match rows in B.")

        # ── 4. Matrix Transpose ────────────────
        elif choice == "4":
            A = input_matrix("Matrix")
            print("Transpose of Matrix:\n", A.T)

        # ── 5. Matrix Determinant ──────────────
        elif choice == "5":
            A = input_matrix("Square Matrix")
            if A.shape[0] == A.shape[1]:  # Check if square matrix
                det = np.linalg.det(A)
                print("Determinant of Matrix:", det)
            else:
                print("Error: Matrix must be square to compute determinant.")

        # ── 6. Exit ────────────────────────────
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        # ── Invalid choice ─────────────────────
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# ───────────────────────────────────────────────
# Run the program
# ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
