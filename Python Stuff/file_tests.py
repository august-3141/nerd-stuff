# File handling go brr

import file_library as fl

print("*** File Writer ***")
print("-------------------")

print(fl.opendoc("sample_doc"))

TEXT = str(input("What should I write? "))

print(fl.writedoc("sample_doc", TEXT))

print("Reading Document:")
print(fl.readdoc("sample_doc"))
