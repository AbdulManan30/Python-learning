marks = {
    "Manan": 100,
    "Kuki": 77,
    "Noman": 99,
}
print(marks.items()) # it will give us an tuple key with their values
print(marks.get("Kuki")) # it will give us the value of the key "Kuki"
print(marks.keys()) # it will give us all the keys
print(marks.values()) # it will give us all the values
print(marks.copy()) # it will give us a copy of the dictionary
marks.update({"Manan": 78, "Kuki": 100}) # it will update the dictionary
marks.pop('Noman') # it will delete the key "Noman" from the dictionary
print(marks)
