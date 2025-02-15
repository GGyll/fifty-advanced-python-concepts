import threading
import time

def download(url):
    print(f"Starting download: {url}")
    time.sleep(2)  # Simulate download time
    print(f"Finished download: {url}")

urls = ["url1", "url2", "url3"]

threads = []
for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All downloads completed")





from concurrent.futures import ThreadPoolExecutor
import time

def download(url):
    print(f"Downloading: {url}")
    time.sleep(2)
    print(f"Finished: {url}")

urls = ["url1", "url2", "url3"]

with ThreadPoolExecutor() as executor:
    executor.map(download, urls)
