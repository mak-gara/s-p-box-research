# S-Box and P-Box Implementation
This project implements functions for both direct and inverse transformations using the S-Box and P-Box algorithms.

## Task Description
Implement your own functions for direct and inverse transformations using the S-Box and P-Box algorithms.

### S-Box and P-Box Definitions
- S-Box (Substitution Box): A substitution box used for byte substitution.
- P-Box (Permutation Box): A permutation box used for byte permutation.

## Usage
### S-Box Transformation
You can substitute a byte using the provided S-Box by calling the `substitute_byte` function. This function takes an input byte (as an integer from 0 to 255) and S-Box table. It returns the substituted byte.
```python
result = substitute_byte(input_byte, S_BOX)
```
When performing S-Box Transformation in this project, the AES block cipher constant table is used.
```text
63 7C 77 7B F2 6B 6F C5 30 01 67 2B FE D7 AB 76
CA 82 C9 7D FA 59 47 F0 AD D4 A2 AF 9C A4 72 C0
B7 FD 93 26 36 3F F7 CC 34 A5 E5 F1 71 D8 31 15
04 C7 23 C3 18 96 05 9A 07 12 80 E2 EB 27 B2 75
09 83 2C 1A 1B 6E 5A A0 52 3B D6 B3 29 E3 2F 84
53 D1 00 ED 20 FC B1 5B 6A CB BE 39 4A 4C 58 CF
D0 EF AA FB 43 4D 33 85 45 F9 02 7F 50 3C 9F A8
51 A3 40 8F 92 9D 38 F5 BC B6 DA 21 10 FF F3 D2
CD 0C 13 EC 5F 97 44 17 C4 A7 7E 3D 64 5D 19 73
60 81 4F DC 22 2A 90 88 46 EE B8 14 DE 5E 0B DB
E0 32 3A 0A 49 06 24 5C C2 D3 AC 62 91 95 E4 79
E7 C8 37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08
BA 78 25 2E 1C A6 B4 C6 E8 DD 74 1F 4B BD 8B 8A
70 3E B5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E
E1 F8 98 11 69 D9 8E 94 9B 1E 87 E9 CE 55 28 DF
8C A1 89 0D BF E6 42 68 41 99 2D 0F B0 54 BB 16
```

### Inverse S-Box Transformation
To perform the inverse S-Box transformation, you must first obtain the inverse table of constants. This can be done by calling the `get_inverse_s_box` function and passing a regular table of constants as a parameter.
```python
inverse_s_box = get_inverse_s_box(S_BOX)
```
After that, we simply call the `substitute_byte` function to perform the S-Box transformation, but with the inverse constant table passed as a parameter.
```python
substituted_byte = substitute_byte(input_byte, inverse_s_box)
```

### P-Box Transformation
Permutation of a byte using the P-Box can be done with the `permutate_byte` function.
```python
permutated_byte = permutate_byte(input_byte, P_BOX)
```
The P-box transformation uses a custom permutation formula.
```text
Bit position before transformation:         0   1   2   3   4   5   6   7
                                            |   |   |   |   |   |   |   |
Bit position after transformation:          3   0   5   1   2   6   7   4
```

### Inverse P-Box Transformation
To perform the inverse P-Box transformation, you first need to calculate the inverse table of constants. This is achieved by using the `get_inverse_p_box` function.
```python
inverse_p_box = get_inverse_p_box(P_BOX)
```
Next, you need to call the `permutate_byte` function and simply pass the inverse constant table as a parameter.
```python
permutated_byte = permutate_byte(input_byte, inverse_p_box)
```

### Examples
Here is an example of how to perform a direct and inverse S-Box transformation:
```python
# Substitute a byte using the S-Box
original_byte = 0xD1
# Substitute 0xD1 to 0x3E
substituted_byte = substitute_byte(original_byte, S_BOX) 

# Get the Inverse S-Box and apply it to the substituted byte
inv_s_box = get_inverse_s_box(S_BOX)
# Substitute 0x3E to 0xD1
inv_substituted_byte = substitute_byte(substituted_byte, inv_s_box)
```
Also, an example of performing a direct and inverse P-Box transformation:
```python
# Permutate a byte using the P-Box
original_byte = 0xD1
# Permutate 0xD1 to 0xD8
permutated_byte = permutate_byte(original_byte, P_BOX) 

# Get the Inverse P-Box and apply it to the permutated byte
inv_p_box = get_inverse_p_box(P_BOX)
# Permutate 0xD8 to 0xD1
inv_permutated_byte = permutate_byte(permutated_byte, inv_p_box)
```

### Running Tests
To run the tests for this code, execute the tests.py file.

```shell
python tests.py
```
This will run a series of tests to verify the correctness of the S-Box and P-Box functions.