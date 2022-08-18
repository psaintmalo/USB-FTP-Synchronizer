# USB FTP Sync by psaintmalo

import os
import platform


class UsbExplorer:
    # Current media devices stored as an array of tuples (Media Name, Media Path)
    media_devices = []

    def __init__(self):
        # Initialize the object by getting the username and platform to be able to fetch media correctly
        self.user = os.getlogin()
        self.platform = platform.system()

        # Update media array
        self.update()

    # Updates the array of available media devices
    # returns any additions or deletions to the array, "+" as addition and "-" as deletion
    def update(self):

        # Store current media to calculate differences
        old_media = self.media_devices

        # Update media array
        self.media_devices = self.fetch_media(self.user, self.platform)

        # Return differences
        return self.check_changes(old_media)

    def check_changes(self, old_media):

        # Get media devices not present in both the new and old array
        non_intersecting_media = list(set(old_media).symmetric_difference(self.media_devices))
        diff = []
        # Check if any of the media that has changed has been removed or added
        for media in non_intersecting_media:
            # TODO: Append the media tuple of just the name?
            if media in old_media:
                diff.append((media, "-"))
            else:
                diff.append((media, "+"))

        return diff

    # Fetch the available media devices utilising platform dependant techniques
    # returns a tuple array in the form [(Media Name, Media Path)]
    @staticmethod
    def fetch_media(username, platform):
        if platform == "Linux":
            media = UsbExplorer.fetch_linux_media(username)

        elif platform == "Windows":
            media = UsbExplorer.fetch_windows_media()

        else:
            media = []
            exit("Error: Platform not supported")

        return media

    # Fetch the available media in Linux
    # returns a tuple array in the form [(Media Name, Media Path)]
    @staticmethod
    def fetch_linux_media(username):
        # Default dir for media in linux
        media_dir = "/run/media/{}/".format(username)

        # Scan the media directory for any subdirectories
        media = [(i.name, i.path) for i in os.scandir(media_dir) if i.is_dir()]

        return media

    # TODO: Implement
    # Fetch the available media in Windows
    # returns a tuple array in the form [(Media Name, Media Path)]
    @staticmethod
    def fetch_windows_media():
        media = []
        print("Windows media discovery not implemented!")
        return media


def main():
    # TODO: Make modifiable through configuration file
    DATA_FOLDER = os.path.expanduser('~') + "/data/"

    print("USB FTP Sync 0.0\n")

    # Initialize USB Explorer
    usb_explorer = UsbExplorer()


if __name__ == '__main__':
    main()
