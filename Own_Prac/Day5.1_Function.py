# def function(*names):
#     for name in names:
#         print("hi",name)
# function("Fareed","madhu","TXF")

# ✅ Final Master Formula to Remember:
# Type	Syntax	Packed into	Access Like
# Positional	*args	Tuple ((…))	for i in args
# Keyword	**kwargs	Dict ({key: val})	for k,v in kwargs.items()

# 🔥 Visual Mind Map (Just Remember This):
# pgsql
# Copy
# Edit
# Function Call → def func(*args, **kwargs)
#      |
#      |__ 10, 20, 30 → *args → (10, 20, 30)
#      |__ name="Fareed", age=21 → **kwargs → {"name": "Fareed", "age": 21}
# ✅ Real-Life Analogy:
# You run a pizza shop:

# *args = Customer orders extra toppings (unlimited, just names)

# **kwargs = Customer gives extra info like size="large", sauce="spicy" (name + value)

# You don’t know in advance what they’ll send – but your function accepts it all.