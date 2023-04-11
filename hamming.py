# Python program to demonstrate
# hamming code
 
def calcRedundantBits(m):
 
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation
 
    for i in range(m):
        if(2**i >= m + i + 1):
            return i
 
def posRedundantBits(data, r):
 
    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)
    res = ''
 
    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
 
    # The result is reversed since positions are
    # counted backwards. (m + r+1 ... 1)
    return res[::-1]
 
 
def calcParityBits(arr, r, paridad):
    n = len(arr)
    parBits = ""
 
    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = paridad
        for j in range(1, n + 1):
 
            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                # -1 * j is given since array is reversed
 
        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr
 
 
def detectError(arr, nr, paridad):
    n = len(arr)
    res = 0
    errorTests = [0, 0, 0, 0]
 
    # Calculate parity bits again
    for i in range(nr):
        val = paridad
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                if i == 0:
                    # print(arr[-1*j], val)
                    pass
 
        # Create a binary no by appending
        # parity bits together.
 
        res = res + val*(2**i)
        errorTests[i] = val
    # Convert binary to decimal
    return res, errorTests
 
if __name__ == "__main__":
    # Enter the data to be transmitted
    data = '10011011000'
    
    # Calculate the no of Redundant Bits Required
    m = len(data)
    r = calcRedundantBits(m)
    
    # Determine the positions of Redundant Bits
    arr = posRedundantBits(data, r)
    
    # Determine the parity bits
    arr = calcParityBits(arr, r)

    # Data to be transferred
    print("Data transferred is " + arr) 
    
    # Stimulate error in transmission by changing
    # a bit value.
    # 100110101001010 -> 110110101001010, error in 2th position.
    
    arr = '101110101001010'
    print("Error Data is " + arr)
    correction, err = detectError(arr, r)
    if(correction==0):
        print("There is no error in the received message.")
    else:
        print("The position of error is ",len(arr)-correction+1,"from the left")
        
