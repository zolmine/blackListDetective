from shared_memory_dict import SharedMemoryDict

jsonMemory = SharedMemoryDict(name="blackList", size=2048)

print(jsonMemory["hello"])