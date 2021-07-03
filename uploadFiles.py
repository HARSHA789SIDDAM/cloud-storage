import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.AzsUGl9zHwmfApB-INPG-dgzsqmgTDWO-avlD97vwxogwRbbQxN6A9dJ5mHYTGRbjoq0DJCwTjE26X1b_wdnfeZRDxrrRrHG6vJQBbzCdRh0Hzc4ST7g8obwS0k2jRUH9slp99dZTNg"
    transferData = TransferData(access_token)
    file_from = input("enter the file to transfer: ")
    file_to = input("enter the file path to upload to DropBox: ")
    transferData.upload_file(file_from, file_to)
    print("file has been moved to DropBox")

main()