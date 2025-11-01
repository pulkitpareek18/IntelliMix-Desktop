# IntelliMix Desktop App - Auto Build System

This repository is configured with GitHub Actions to automatically build executable files for both **Ubuntu Linux** and **Windows** on every push to the main branch.

## ✅ What's Working Now

- **✅ Environment Variables**: API keys loaded from `.env` file
- **✅ Cross-platform Build**: Ubuntu and Windows executables
- **✅ Local Build Tested**: Successfully built 279MB executable
- **✅ Automated Testing**: Import and Flask app tests
- **✅ Auto Releases**: GitHub releases with downloadable executables

## 🚀 Setup Instructions

### 1. Add GitHub Secrets (Required)

To enable the build process to include your API key:

1. Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions**
2. Click "**New repository secret**"
3. Add: `GENAI_API_KEY` = `your-actual-api-key-here`

### 2. How It Works

Every push to `main` branch triggers:

1. **🧪 Test Phase**: Verifies all imports work
2. **🔨 Build Phase**: Creates executables for both platforms
3. **📦 Package Phase**: Uploads artifacts (30-day retention)
4. **🚀 Release Phase**: Creates GitHub release with both executables

### 3. Output Files

After successful build, download from **Releases** section:

- **`IntelliMix-Linux`**: For Ubuntu/Linux (279MB+)
- **`IntelliMix-Windows.exe`**: For Windows (similar size)

Both are **self-contained** - no Python installation required!

## 🛠️ Local Development

### Build Locally:
```bash
cd backend
pip install -r requirements.txt
python test_build.py  # Test first
pyinstaller IntelliMix.spec  # Build executable
./dist/IntelliMix  # Run (Linux) or IntelliMix.exe (Windows)
```

### File Structure:
```
backend/
├── .env                    # Your API keys (gitignored)
├── IntelliMix.spec        # PyInstaller config
├── test_build.py          # Build verification tests
├── desktop.py             # Main desktop app entry
├── app.py                 # Flask backend
├── requirements.txt       # Dependencies (includes pyinstaller)
└── dist/IntelliMix        # Built executable
```

## 🔧 Configuration

### Environment Variables (.env):
```bash
GENAI_API_KEY=your-google-genai-api-key
GENAI_MODEL=gemini-2.0-flash
```

### Dependencies Added:
- `pyinstaller` - Creates executables
- `pywebview[cef]` - Desktop GUI framework
- `python-dotenv` - Environment variable loading
- `flask` - Web backend

## 🐛 Troubleshooting

### Common Issues:
1. **Missing API Key**: Add `GENAI_API_KEY` to GitHub secrets
2. **Import Errors**: Check `test_build.py` output
3. **Large File Size**: Expected (~279MB) due to bundled Python + Qt + dependencies
4. **Linux Libraries**: GitHub Actions installs required system deps

### Build Warnings (Safe to Ignore):
- `libxcb-cursor.so.0` warnings - UI libraries for different systems
- Old Python version warnings - CEF compatibility libraries

## 📋 Workflow Status

Current workflow (`.github/workflows/main.yml`) includes:
- ✅ Cross-platform matrix build (Ubuntu + Windows)
- ✅ System dependency installation
- ✅ Python environment setup
- ✅ Pre-build testing
- ✅ PyInstaller executable creation
- ✅ Artifact upload with 30-day retention
- ✅ Automatic GitHub releases

## 🎯 Next Steps

1. **Push to main branch** - Triggers automatic build
2. **Check Actions tab** - Monitor build progress
3. **Download from Releases** - Get your executables
4. **Distribute to users** - Self-contained, no installation needed!