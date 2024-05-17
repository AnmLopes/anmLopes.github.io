import http.server
import socketserver

# Set the port number you want to use
PORT = 8000

# Change to the directory containing your HTML file
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at port", PORT)
    # This will keep the server running until you press Ctrl+C
    httpd.serve_forever()
