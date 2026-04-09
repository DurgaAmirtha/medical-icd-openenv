from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess
import threading

PORT = 7860

# Run inference in background
def run_inference():
    try:
        subprocess.run(["python", "inference.py"])
    exceapt Exception as e:
        print("Error running inference:", e)

# Start inference in separate thread
threading.Thread(target=run_inference).start()

# Start simple web server
print(f"Serving on port {PORT}")
HTTPServer(("", PORT), SimpleHTTPRequestHandler).serve_forever()