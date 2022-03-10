from shared_memory_dict import SharedMemoryDict

jsonMemory = SharedMemoryDict(name="blackList", size=2048)

jsonMemory["hello"] = "12544444444455555555555222222222111111111111111111111"

print(jsonMemory["hello"])

del jsonMemory["hello"]
try:
    print(jsonMemory["hello"])
except:
    print("memory deleted")

jsonMemory["hello"] = "nd again"
print(jsonMemory["hello"])
