#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

# Change to the directory containing the HTML file
os.chdir('/workspace/project')

PORT = 12000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Allow iframe embedding
        self.send_header('X-Frame-Options', 'ALLOWALL')
        super().end_headers()

with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Operating Systems Concepts server running at:")
    print(f"   Local: http://localhost:{PORT}")
    print(f"   Network: https://work-1-pibqbwrwwqvhbgld.prod-runtime.all-hands.dev")
    print(f"\n📚 Features:")
    print(f"   • Interactive visual explanations")
    print(f"   • 5 major OS topic categories")
    print(f"   • Detailed diagrams and algorithms")
    print(f"   • Mobile-responsive design")
    print(f"\n🎯 Click on any category card to explore concepts!")
    print(f"\nPress Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped")
        sys.exit(0)