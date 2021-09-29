#Checks for the largest common prefix  
def lcp(s, t):  
    n = min(len(s),len(t));  
    for i in range(0,n):
        # print("s[" + str(-i) + "] = " + (s[i]))
        # print("t[" + str(-i) + "] = " + (t[i]))
        if((s[i]) != (t[i])):  
            return s[0:i];  
    else:  
        return s[0:n];  
    
# frase = "banana";  
# frase = "banana"
frase = "a bananeira tem banana"
frase_split = frase.split(" ")

for palavra in frase_split:
    lrs="";  
    count = 0
    n = len(palavra);  
    for i in range(0,n):  
        for j in range(i+1,n):  
        #Checks for the largest common factors in every substring  
            # print("string 1: " + palavra[i:n] + "   string 2: " + palavra[j:n])
            x = lcp(palavra[i:n],palavra[j:n]);  

            #If the current prefix is greater than previous one   
            #then it takes the current one as longestr repeating sequence  
            if(len(x) > len(lrs)):  
                palavra_temp = palavra[i:n].replace(x,"", 1)
                # print(palavra_temp)
                if(x in palavra_temp):
                    lrs=x;    
    print("Longest repeating sequence: "+lrs)

    