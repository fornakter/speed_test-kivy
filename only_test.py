import speedtest

test = speedtest.Speedtest()

print("Loading server list...")
# Get list of servers
test.get_servers()
# Choose best server
best = test.get_best_server()
print(f"Found best server in: {best['country']}, {best['name']}")
print("Download test...")
download_result = test.download()
print("Upload test...")
upload_result = test.upload()
print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")