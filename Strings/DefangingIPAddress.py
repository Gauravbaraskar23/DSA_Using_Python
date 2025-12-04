# 1108. Given a valid (IPv4) IP address ,replaces every period "." with "[.]".

# def defangIPAddr(address):
#     return address.replace("." , "[.]")

# OR

def defangIPAddr(address):
    ans  =""
    for addr in address:
        if addr != ".":
            ans += addr
        
        else:
            ans += "[.]"
    return ans
             


address = "255.100.50.0"
print(defangIPAddr(address))