from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainWidget(BoxLayout):
    status_label = StringProperty("Status: waiting")

    def on_button_click(self):
        self.status_label = "Status: klick"
        try:
            # Get list of servers
            try:
                import speedtest

                print("Loading server list...")
                test = speedtest.Speedtest()
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
                print(e)

        except Exception as e:
            print(e)


class MainMenu(App):
    pass


if __name__ == '__main__':
    MainMenu().run()
