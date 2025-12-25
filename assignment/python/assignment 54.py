#check multiple keys exists in a dictionary.
dict = {"a": 1, "b": 2, "c": 3, "d":4,"e": 5,"f":6,"c":9}
keys_to_check = ["a", "b", "c"]

missing = [i for i in keys_to_check if i not in dict]

if missing:
    print("Missing keys:", missing)
else:
    print("All keys exist")
 