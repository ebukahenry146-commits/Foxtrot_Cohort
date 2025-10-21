# -------------- CONTROL STRUCTURES ----------------

# Condition

# IF STATEMENT
destination_fee = 1000
transport_fee = 500
train ="available" 

#if transport_fee <= destination_fee: 
#     print(f"{"==" * 24}\nGetting to destination successful.\n{"==" * 24}")
#else:
#    print(f"{"==" * 24}\nGetting to destination unsuccessful.\n{"==" * 24}") 

if transport_fee <= destination_fee: 
     print(f"{"==" * 24}\nGetting to destination successful.\n{"==" * 24}")
else:
     print(f"{"==" * 24}\nGetting to destination unsuccessful.\n{"==" * 24}") 

if transport_fee <= destination_fee and train == "available":
     print(f"{"==" * 24}\nGetting to a destination A successful.\n{"==" * 24}")
elif transport_fee <= destination_fee and train != "available":
     print(f"{"==" * 24}\nGetting to a destination A through a train successful.\n{"==" * 24}")
else:
     print(f"{"==" * 24}\nGetting to a destination unsuccessful.\n{"==" * 24}")
















































