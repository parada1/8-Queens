

import numpy as np




def array_to_string(a):
    s=""
    for n in a:
        s=s+str(n)
    return str(s)
    
def string_to_array(s):
    lista2 =[]
    for i in range(len(s)):
        lista2.append(int(s[i]))
    return np.array(lista2)
    

def main():
    a = np.array([0, 5, 7, 0, 3, 6, 2, 1])
    print(array_to_string(a))
    print(string_to_array("05703621"))

    s= {"123", "456","789","123"}
    print(s)


if __name__ == "__main__":
    main()

