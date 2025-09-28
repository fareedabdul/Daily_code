# s = [1,2,3,[11,22,33]]
# s[2] = 22
# print(s)     // List is mutable


# s =( 1, )
# # s[0] = 33
# print(type(s))
# print(s)  
#  Suitcase jisme tumne sab kuch daal diya, lekin lock kar diya — ab andar ka kuch badal nahi sakte


# s = {1,2,5,5}
# print(type(s))
# s.add(66)
# print(s) #* we can change the item and list and dict are not available for SET 

# s = {"Fareed": "182372347"}
# s["Fareed"] = "king"
# print(type(s))
# print(s)

# Summary Table (Support Matrix):

# Data Type →	Accepts       int/str     Accepts list  	Accepts dict	Accepts tuple	   Accepts set
# List	                       ✅ Yes	    ✅ Yes	       ✅ Yes	      ✅ Yes	            ✅ Yes
# Tuple	                       ✅ Yes	    ✅ Yes	       ✅ Yes	      ✅ Yes	            ✅ Yes
# Set	                       ✅ Yes	    ❌ No	       ❌ No	          ✅ Yes	            ✅ Yes (but nested set ❌)
# Dict (key)	              ✅ Yes	        ❌ No	       ❌ No	          ✅ Yes	            ❌ No
# Dict (value)	              ✅ Yes	        ✅ Yes	        ✅ Yes   	  ✅ Yes             ✅ Yes