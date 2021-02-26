import pythoncom

context = pythoncom.CreateBindCtx(0)

# Get all the Running Objects
running_coms = pythoncom.GetRunningObjectTable()

# Creates an enumerator that can list the monikers of all the objects 
# currently registered in the Running Object Table (ROT).
monikiers = running_coms.EnumRunning()

# loop through all the monikiers returend
for monikier in monikiers:
    
    print('-'*100)
    
    # Gets the display name, which is a user-readable representation of this moniker. 
    print(monikier.GetDisplayName(context, monikier))

    print(monikier.Hash())
    
    # Indicates whether this moniker is of one of the system-supplied moniker classes. 4(MKSYS_ITEMMONIKER)
    print(monikier.IsSystemMoniker())
    
    # Supplies an enumerator that can enumerate the components of a composite moniker. 
    print(monikier.Enum())