"""The rgb function is incomplete.
Complete it so that passing in 
RGB decimal values will result in a 
hexadecimal representation being returned
. 
Valid decimal values for RGB are 0 - 255.
Any values that fall out
of that range must be rounded to the 
closest valid value.

Note: Your answer should always be 6 characters long,
the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"""

#convert the RGB to hex
#Store that value into a new variable

def rgb(r, g, b):
    if r > 255:
        r = 255
    if r <= 0:
        r = 0
    if g > 255:
        g = 255
    if g <= 0:
        g = 0
    if b > 255:
        b = 255
    if b <= 0:
        b = 0
    value = ''
    temp_value = ''
    for i in [r, g, b]:
        temp_value = hex(i).upper()[2:]
        if len(temp_value) <= 1:
            temp_value = '0' + temp_value
        value += temp_value
    return value
print(rgb(-1, 256, 0))