# File handling go brr

import file_module as fm

print("*** File Writer ***")
print("-------------------")

print(fm.opendoc("sample_doc"))

TEXT = str(input("What should I write? "))

print(fm.writedoc("sample_doc", TEXT))

print("Reading Document:")
print(fm.readdoc("sample_doc"))
