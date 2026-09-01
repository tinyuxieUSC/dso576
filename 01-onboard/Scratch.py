# %%
def a(x):
    print("a")
    return x

def b(x):
    print("b")
    return a(x) + a(x)

r = b(3)

# %%
