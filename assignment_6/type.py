file_name=list(input("Please enter your file name: "))
spl=file_name.index(".")
del file_name[:spl+1]
file_type="".join(file_name)
print(f"Your file type: {file_type}")
