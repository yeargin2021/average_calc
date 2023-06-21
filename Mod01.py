from statistics import mean as avg

numbers = []

def calculate():
    return program()

def program():
    while True:
        populate = input("Enter a dollar amount, or \'x\' to stop: $")
        if populate == 'x':
            break  
        else:
            numbers.append(float(populate))
            return calculate()
    answer = round((avg(numbers)), 2)
    print(f"Average weekly takehome is: ${answer}")

program()

############################
# By: Tommy H. Yeargin, Jr.#
#      21 June 2023        #
#                          #
#      Python 3.11.4       #
############################

# Released under MIT License
# 
# Copyright (c) 2023 Tommy H. Yeargin, Jr.
# 
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files 
# (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
