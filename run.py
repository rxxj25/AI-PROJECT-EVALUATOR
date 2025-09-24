#!/usr/bin/env python3
"""
AI-Powered Project Evaluator
NatWest Hackathon 2025

This is the main entry point for the application.
Run this file to start the AI Project Evaluator.
"""

import os
import sys
from app import app
from config import Config

def main():
    """Main function to run the application"""
    print("🚀 Starting AI-Powered Project Evaluator...")
    print("=" * 50)
    print("🏆 NatWest Hackathon 2025")
    print("🤖 AI-Powered Project Evaluation System")
    print("=" * 50)
    
    # Check if we're in development mode
    if Config.DEBUG:
        print("🔧 Running in DEVELOPMENT mode")
        print("📊 Dashboard: http://localhost:5000")
        print("📝 Submit Projects: http://localhost:5000/submit")
        print("🏅 Leaderboard: http://localhost:5000/leaderboard")
        print("📈 Analytics: http://localhost:5000/analytics")
        print("=" * 50)
    
    try:
        # Start the Flask application
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=Config.DEBUG,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n👋 Shutting down AI Project Evaluator...")
        print("Thank you for using our system!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
