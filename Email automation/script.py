import win32com.client as win32
app = win32.gencache.EnsureDispatch("Outlook.Application")
namespace = app.GetNamespace("MAPI")

EMAIL_ACCOUNT = 'santhosh@skcript.com'
READ_FOLDER = 'Inbox'
read_folder = namespace.Folders[EMAIL_ACCOUNT].Folders[READ_FOLDER]

for i in range(item_count, 0, -1):
  print(i)