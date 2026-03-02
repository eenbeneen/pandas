import uuid
import pandas as pd
import pyarrow as pa

# Setup
id_val = uuid.uuid4()
pa_array = pa.array([id_val.bytes], type=pa.uuid())
arr = pd.arrays.ArrowExtensionArray(pa_array)
ser = pd.Series(arr)

#Should be false
print(ser[0] in ser)
#Should be true
print(ser[0] in ser.array)
#Should be false
print(None in ser.array)