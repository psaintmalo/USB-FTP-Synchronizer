# USB FTP Sync by psaintmalo

import os
import platform


class UsbExplorer:
    media_devices = []

    def __init__(self):
        self.user = os.getlogin()
        self.platform = platform.system()

        self.update()

    def check_changes(self):
        old_media = self.media_devices
        self.update()

        if old_media == self.media_devices:
            return False
        else:
            non_intersecting_media = list(set(old_media).symmetric_difference(self.media_devices))
            diff = []
            for media in non_intersecting_media:
                # TODO: Append the media tuple of just the name?
                if media in old_media:
                    diff.append((media, "-"))
                else:
                    diff.append((media, "+"))

        return diff

    def update(self):

        media = self.fetch_media(self.user, self.platform)

        self.media_devices = media

    @staticmethod
    def fetch_media(username, platform):
        if platform == "Linux":
            media = UsbExplorer.fetch_linux_media(username)

        elif platform == "Windows":
            media = UsbExplorer.fetch_windows_media()

        else:
            media = "NULL"
            exit("Error: Platform not supported")

        return media

    @staticmethod
    def fetch_linux_media(username):
        media_dir = "/run/media/{}/".format(username)

        media = [(i.name, i.path) for i in os.scandir(media_dir) if i.is_dir()]

        return media

    # TODO: Implement
    @staticmethod
    def fetch_windows_media():
        media = [("TBI", "TBI")]
        print("Windows media discovery not implemented!")
        return media


def main():
    # TODO: Make modifiable through configuration file
    DATA_FOLDER = os.path.expanduser('~') + "/data/"

    print("USB FTP Sync 0.0\n")

    usb_explorer = UsbExplorer()


if __name__ == '__main__':
    main()
