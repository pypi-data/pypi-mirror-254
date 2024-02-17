import os
import win32com.client as win32


class AspenConnection:

    def __init__(self, filepath, registered_name="Apwn.Document"):
        """

        :param filepath: Path to the simulation file
        :param registered_name: Registered name of Aspen Plus, should not need changing.
        """
        self.filepath = filepath
        self.registered_name = registered_name


    def connect(self):
        """Use to connect the Python and Aspen Plus

        :return: Application Instance to use later
        """
        print("Connecting to Aspen Plus. Please standby")
        app = win32.Dispatch(self.registered_name)
        print("Successful Connection to Aspen Plus")
        return app


    def start(self, app, show=1,):
        """Open the Aspen Plus file. Use .connect first.
        The file path provided in AspenConnection(filepath) is the one this function will connect to.

        :param show: Open the Aspen UI.
        :type show: bool
        :return: Returns the simulation instance
        """
        aspen_path = os.path.abspath(self.filepath)
        print("\n Connected to Aspen Plus")
        print("\n Standby for Aspen to open, this may take a couple of minutes")
        app.InitFromArchive2(aspen_path)
        app.visible = show
        print("\n Ready to Go!")

    def disconnect(self, app):
        """Disconnects from the Aspen Plus instance

        :param app: Pass the simulation instance obtained by .connect()
        """
        print("Disconnecting from Aspen Plus")
        aspen_path = os.path.abspath(self.filepath)
        app.Quit(aspen_path)
        print("Successfully disconnected from Aspen Plus")
