import threading
import webview
import time
import webbrowser
from app import app

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
