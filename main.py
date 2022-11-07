import string
import random
import sys

def process(s):
    file = open("IsEven.java", "a")
    file.write(s + "\n")
    file.close()

def main():
    process("public class IsEven {")
    process("    public static boolean isEven(int i) {")
    maximum = 1000000
    for i in range(maximum):
        even = "true" if i % 2 == 0 else "false"
        if i == 0:
            process("        if(i == " + str(i) + ") return " + even + ";")
        elif i == maximum - 1:
            process("        else return " + even + ";")
        else:
            process("        else if(i == " + str(i) + ") return " + even + ";")
    process("    }" + "\n")
    process("}")

main()
