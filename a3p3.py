#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 3 Student Solution
January 2026
Author: Precious Ajilore

Random numbers are an integral component of cryptography. Alice knows random numbers
are difficult to generate efficiently. In order to securely communicate with Bob, she is trying
to use pseudorandom number generators (PRNGs), algorithms which produce sequences of
pseudorandom numbers, which appear random, but which, with some extra (typically hidden)
information, can be predicted. Alice found an algorithm which uses a recurrence relation similar
to the affine cipher’s encryption function:

Ri+2 = (aRi+1 + bRi + c) (mod m) i ≥ 0
where a, b, c, m, R1, and R0 are chosen in advance. For reference, a, b, and c are called the
“keys”, m is called the “modulus”, and R0 and R1 are called “seeds”. We will assume that m
is a prime number. For example, if we run this algorithm with a = 3, b = 5, c = 9, m = 17,
R0 = 11 and R1 = 6, then R2 = 14 since (3 · 6 + 5 · 11 + 9) = 82 = 14 (mod 17), and R3 = 13
since (3 · 14 + 5 · 6 + 9) = 81 = 13 (mod 17).
Complete the module “a3p3.py” by implementing the function “random generator(a, b, c,
m, r0, r1, n)”, where a, b, c, and m are as above, and r0 and r1 are the seeds values of R0 and
R1, which returns a list of integers containing the next n elements of generated numbers
(R2, R3, . . ., Rn+1). The following demonstrates invocation sequences that should run without
error and produce identical output:
>>> random_generator(3, 5, 9, 17, 11, 6, 3)
[14, 13, 16]
"""

def random_generator(a, b, c, m, r0, r1, n):
    #Ri+2 = (aRi+1 + bRi + c) (mod m) i ≥ 0
    result = []
    #Start with prev = R0
    prev = r0

    #Start with curr = R1
    curr = r1
    
    #Repeat n times: 
    for _ in range(n):  
        #compute the next value using the formula
        next_val = (a*curr + b*prev + c) % m
    
        #append next_val to result
        result.append(next_val)
        #shift current to prev and next_val to curr
        # old R_{i+1} becomes new R_i
        # new R_{i+2} becomes new R_{i+1}
        prev, curr = curr, next_val


    return result

def test():
    assert random_generator(3, 5, 9, 17, 11, 6, 3) == [14, 13, 16]
    #assert random_generator(3,5,9,17,11,6,0) == []


from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()