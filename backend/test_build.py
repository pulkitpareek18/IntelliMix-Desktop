#!/usr/bin/env python3
"""
Simple test to verify that the desktop app can import all necessary modules.
This doesn't test the GUI but ensures all dependencies are correctly bundled.
"""

def test_imports():
    """Test that all required modules can be imported."""
    try:
        import threading
        import webview
        import time
        import webbrowser
        from app import app
        print("[OK] All modules imported successfully")
        return True
    except ImportError as e:
        print(f"[ERROR] Import error: {e}")
        return False

def test_flask_app():
    """Test that the Flask app can be created."""
    try:
        from app import app
        with app.test_client() as client:
            # Test if the app has routes configured
            response = client.get('/')
            print(f"[OK] Flask app responds (status: {response.status_code})")
            return True
    except Exception as e:
        print(f"[ERROR] Flask app error: {e}")
        return False

if __name__ == "__main__":
    print("Testing IntelliMix Desktop App Components...")
    
    import_success = test_imports()
    flask_success = test_flask_app()
    
    if import_success and flask_success:
        print("SUCCESS: All tests passed! The app should work correctly.")
        exit(0)
    else:
        print("FAILURE: Some tests failed. Check the errors above.")
        exit(1)