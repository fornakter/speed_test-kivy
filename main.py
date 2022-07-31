from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainWidget(BoxLayout):
    status_label = StringProperty("Status: waiting")

    def on_button_click(self):
        self.status_label = "Status: klick"
        try:
            #import speedtest
            from speedtest import Speedtest
        except Exception as e:
            print('Error import: ', e)
        try:
            print("Loading server list...")
            test = Speedtest()
            # Get list of servers
            test.get_servers()
            # Choose best server
            best = test.get_best_server()
            # print(f"Found best server in: {best['country']}, {best['name']}")
            print("Download test...")
            download_result = test.download()
            print("Upload test...")
            # upload_result = test.upload()
            print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
            # print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
        except Exception as e:
            print('Another error: ', e)

class MainMenu(App):
    pass


if __name__ == '__main__':
    MainMenu().run()
