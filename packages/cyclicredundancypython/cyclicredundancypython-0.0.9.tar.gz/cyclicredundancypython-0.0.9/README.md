# Redundancy Check Script

This Python script performs a redundancy check on transmitted data using a long division technique. It checks for errors in the transmitted bits by calculating the remainder and syndrome.

<strong>To Install with PIP >> https://pypi.org/project/cyclicredundancypython</strong>

## Usage

1. **Install Python:**
   Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Run the Script:**

    If installed with pip

   ```bash
   cyc
   ```
   
   Or clone the repository and Open a terminal or command prompt, navigate to the script's directory, and run the script using the following command:

   ```bash
   python cyc.py
   ```
   
### Enter Inputs:
Follow the prompts to enter the dividend and divisor when prompted.

### View Results:
The script will display the remainder, codeword, and check if there are errors in the transmitted bits.

# Script Details

## `longXDv` Function

This function performs long division on binary numbers, simulating the XOR operations for each step.

### Parameters:

- `dividend`: Binary number representing the data to be transmitted.
- `divisor`: Binary number representing the divisor for the redundancy check.
- `appender`: Appender pattern used in the long division.

### Returns:

- The remainder after the division.

## `changeDividendLBit` Function

This function changes the last bit of the given dividend.

### Parameters:

- `dividend`: Original binary number.
- `val`: New value (0 or 1) for the last bit.

### Returns:

- The modified binary number.


# Usage

1. **Run the Script:**
   Open a terminal or command prompt, navigate to the script's directory, and run the script using the following command:

   ```bash
   cyc
    ```

2.  **Enter Inputs:**

Follow the prompts to enter the dividend and divisor when prompted.

**Example:**

```bash
Enter Dividend:- 1001
Enter Divisor:- 1011
The remainder is:- 110
The Syndrome is zero, hence the transmitted bits are error-free.
For testing changing the last bit of dividend from 1001 to 1000, testing started :-
Test has errors
```

### Connect with me on
<a href="https://www.linkedin.com/in/thejashari/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="linkedin" height="30" width="40" /></a>
<a href="https://instagram.com/nuthejashari" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="instagram" height="30" width="40" /></a>

