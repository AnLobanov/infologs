from libfptr10 import IFptr

# Connecting to device through USB
fptr = IFptr("")
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_USB))
fptr.applySingleSettings()
fptr.open()
if not fptr.isOpened():  # If script can't connect to device, try to reconnect
    while not fptr.isOpened():
        fptr.open()

# Get serial number
fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STATUS)
fptr.queryData()
serialNumber = fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)

# Get registration number
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_REG_INFO)
fptr.fnQueryData()
regNumber = fptr.getParamString(1037)

# Get expiration date
fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
fptr.fnQueryData()
expirationDate = fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME).strftime("%d.%m.%Y")

# Close connection and write information to log-file
fptr.close()
with open('IL.log', 'w') as file:
    file.write(serialNumber + ';' + regNumber + ';' + expirationDate)