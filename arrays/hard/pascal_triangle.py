def nCr(n, r):
    """
    Compute nCr (n choose r).

    Meaning:
        Number of ways to choose r items from n items
        when order does NOT matter.

    Mathematical formula:
        nCr = n! / (r! * (n-r)!)

    Directly computing factorials can be inefficient and may
    overflow in languages with fixed-size integers.

    We use the recurrence:

        nC(r+1) = nCr * (n-r) / (r+1)

    Starting from:
        nC0 = 1

    We repeatedly generate the next coefficient from the
    previous coefficient.

    Example:
        5C0 = 1
        5C1 = 1 * 5/1 = 5
        5C2 = 5 * 4/2 = 10

    Symmetry property:
        nCr = nC(n-r)

    Therefore we choose the smaller of r and (n-r)
    to minimize the number of iterations.

    Time Complexity:
        O(min(r, n-r))

    Space Complexity:
        O(1)
    """

    # Use symmetry:
    # Choosing 97 from 100 is the same as choosing
    # the 3 elements that are left out.
    r = min(r, n - r)

    # nC0 = 1
    res = 1

    # Generate:
    # nC1, nC2, ..., nCr
    for i in range(r):

        # Current coefficient:
        # nCi
        #
        # Next coefficient:
        # nC(i+1)
        #
        # Formula:
        # nC(i+1) = nCi * (n-i) / (i+1)
        res = (res * (n - i)) // (i + 1)

    return res


def pascal_triangle(row, col):
    """
    Pascal Triangle facts:

    Every element at position (row, col) is:

        rowCcol

    Example:

            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1

    Row 4:
        4C0 4C1 4C2 4C3 4C4
         1   4   6   4   1

    Pascal relation:

        nCr = (n-1)Cr + (n-1)C(r-1)

    Intuition:
        Pick one special element.

        Every valid selection either:
            - contains it
            - does not contain it

        Adding these two cases gives the recurrence
        used to construct Pascal's Triangle.
    """
    print(nCr(row, col))


pascal_triangle(5, 2)
