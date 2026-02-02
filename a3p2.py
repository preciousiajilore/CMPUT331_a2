#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 Precious Ajilore
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
"""
#--------------------------------------------------------------
#Affine Encryption:
# c = (a*p + b) mod m 
# where gcd(a, m) = 1, a is a coprime to m, b is any integer in the range [0, m-1]
"""
Problem 2 (2 Marks)
A Caesar cipher has only m − 1 possible keys, where m is the number of characters in
its alphabet. An affine cipher instead uses a pair of integers (a, b) as its key, which greatly
increases the number of possible keys. The value b may be any integer modulo m, but a must
be coprime with m. This condition ensures that multiplying distinct integers by a(mod m)
produces distinct outputs.

Because of this restriction, determining the number of valid affine cipher keys is less straight-
forward. Complete the module “a3p2.py” by implementing the function “affine key count(m)”,
where m is the size of the alphabet. The function must return the total number of distinct affine
cipher keys available for an alphabet of that size. Note that we do not count the degenerate
case where the ciphertext is identical to the plaintext (i.e., where the chosen keys leave every
character unchanged). For example:
>>> affine_key_count(65)
3119

"""
#--------------------------------------------------------------

def affine_key_count(m):
    #count how many choices for b 
    #b E {0,1,2,...,m-1} => m choices for b
    count_b = m

    #count how many choices for a
    #a E {1,2,3,...,m-1} and gcd(a,m) = 1
    count_a = 0
    
    #factor m to find coprime, try p while p^2 <= m and trial division up to sqrt(m)
    #if p divides m, record p and divide m by p until it no longer divides
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def totient(m):
        #keep a copy of m so that i can divide out factors as i find them
        n = m

        #start off with everything being coprime and then subtract those that are not
        phi = m

        #trial division to find prime factors
        p = 2

        #test divisors up to sqrt(n)
        while p * p <= n:
            if n % p == 0:
                # p is a prime factor of n
                #if p is a prime factor, sthen 1/p of the numbers from 1..m are divisible by p.
                # Those cannot be coprime. So remove that fraction.
                phi -= phi // p
                while n % p == 0:
                    #remove all copies of p from n so we dont treat the same prime factor again
                    n //= p
                
            p += 1
        if n > 1:
            phi -= phi // n
        return phi

    """
    If m has prime factors like 5 and 13 (example: 65 = 5×13), then:
    - any number divisible by 5 is not coprime with 65
    - any number divisible by 13 is not coprime with 65
    """
    count_a = totient(m)

    #total keys = choices for a * choices for b - 1 (degenerate case)
    total_keys = (count_a * count_b) - 1
    return total_keys

    #raise NotImplementedError
    



def test():
    assert affine_key_count(65) == 3119
    

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()