print("how many kms do you want to convert ?")

# kms / 1.60934 # "50" / 1.60934

kms = input()

miles = float(kms) / 1.6934

miles = round(miles,2)

print(f"{kms}km is { miles } miles ")


round(miles, 2)
