import speedtest
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class MainWidget(BoxLayout):
    status_label = StringProperty("Status: waiting")
    server_label = StringProperty("Server:")
    download_label = StringProperty('Download speed:')
    upload_label = StringProperty('Upload speed:')
    test = speedtest.Speedtest()

    def on_press(self):
        self.status_label = "Status: Loading server list..."

    def on_release(self):
        self.status_label = "Status: Speed testing..."
        # Get list of servers
        try:
            self.test.get_servers()
        except Exception as e:
            print(e)
        # Choose best server
        best = self.test.get_best_server()
        self.server_label = f"Found best server in: {best['country']}, {best['name']}"

    def download_test(self):
        download_result = self.test.download()
        self.download_label = f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s"

    def upload_test(self):
        upload_result = self.test.upload()
        self.status_label = "Status: Test complete"
        self.upload_label = f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s"


class MainMenu(App):
    pass


if __name__ == '__main__':
    MainMenu().run()
