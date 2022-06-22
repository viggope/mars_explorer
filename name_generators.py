import random
letters = "abcdefghijklmnopqrstuvwxyz"
greek = ("alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega")

def generate_ship():
    name = ""
    name += random.choice(letters).upper()
    name += str(random.randint(1000, 9999))
    name += random.choice(letters) + random.choice(letters)
    name += random.choice(greek).upper()
    return name

def generate_robot():
    name = ""
    name += input("namn i svenska ordboken: ").upper()
    name += "-" + random.choice(letters).upper()
    name += str(random.randint(0,9))
    return name

print (generate_robot())
print (generate_ship())