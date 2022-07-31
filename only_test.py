import speedtest

def speed_test():
    test = speedtest.Speedtest()

    print("Loading server list...")
    # Get list of servers
    try:
        test.get_servers()
    except Exception as e:
        print(e)
    # Choose best server
    best = test.get_best_server()
    print(f"Found best server in: {best['country']}, {best['name']}")
    print("Download test...")
    download_result = test.download()
    print("Upload test...")
    upload_result = test.upload()
    print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
    print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")

speed_test()
