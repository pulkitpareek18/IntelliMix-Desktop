import threading
import time
import webbrowser
import os
import sys
from app import app

# Import webview with fallback handling
try:
    import webview
    WEBVIEW_AVAILABLE = True
except ImportError as e:
    print(f"Warning: webview not available: {e}")
    WEBVIEW_AVAILABLE = False

# --- Run Flask in background ---
def start_flask():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


# --- Intercept navigation to handle downloads ---
def on_navigate(url):
    # If user clicks a link that looks like a file download, open externally
    if "/files" in url or url.endswith((".mp3", ".mp4")):
        webbrowser.open(url)
        return False  # prevent opening inside webview
    return True


if __name__ == "__main__":
    # Start Flask in a background thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Give Flask time to start
    time.sleep(2)

    if WEBVIEW_AVAILABLE:
        try:
            print("Starting IntelliMix Desktop Application...")
            
            # Create window
            window = webview.create_window(
                title="IntelliMix Desktop",
                url="http://127.0.0.1:5000",
                width=1200,
                height=800,
                resizable=True,
            )

            # Attach navigation handler (using modern event API)
            try:
                window.events.loading += lambda url: on_navigate(url)
            except Exception:
                # Fallback for older pywebview versions
                window.events.loaded += lambda: None

            # Run GUI loop
            webview.start(debug=False)
            
        except Exception as e:
            print(f"Error starting desktop GUI: {e}")
            print("Falling back to web browser mode...")
            WEBVIEW_AVAILABLE = False
    
    if not WEBVIEW_AVAILABLE:
        print("=== IntelliMix Web Mode ===")
        print("Desktop GUI not available, running in web browser mode")
        print("Open your browser and go to: http://127.0.0.1:5000")
        print("Press Ctrl+C to stop the server")
        
        # Optionally try to open browser automatically
        try:
            webbrowser.open("http://127.0.0.1:5000")
        except Exception:
            pass
        
        # Keep Flask running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nApplication stopped by user")
            sys.exit(0)
