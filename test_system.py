#!/usr/bin/env python3
"""
System Test for AI Project Evaluator
Tests all major components to ensure everything is working correctly
"""

import sys
import traceback
from snowflake_integration import SnowflakeManager
from ai_evaluator import AIProjectEvaluator
from config import Config

def test_snowflake_connection():
    """Test Snowflake connection and table creation"""
    print("🔗 Testing Snowflake connection...")
    try:
        snowflake_manager = SnowflakeManager()
        print("✅ Snowflake connection successful")
        
        # Test table creation
        print("📊 Testing table creation...")
        snowflake_manager.setup_tables()
        print("✅ Tables created/verified successfully")
        
        return True
    except Exception as e:
        print(f"❌ Snowflake test failed: {e}")
        return False

def test_ai_evaluator():
    """Test AI evaluator functionality"""
    print("🤖 Testing AI evaluator...")
    try:
        ai_evaluator = AIProjectEvaluator()
        
        # Test with sample project data
        test_project = {
            'project_id': 'test-project-123',
            'project_name': 'Test Project',
            'description': 'This is a test project to verify AI evaluation functionality.',
            'team_name': 'Test Team',
            'raw_data': {
                'tech_stack': 'Python, Flask, AI',
                'challenge_category': 'ai-ml'
            }
        }
        
        print("🧪 Running test evaluation...")
        evaluation_result = ai_evaluator.evaluate_project(test_project)
        
        if evaluation_result and 'overall_score' in evaluation_result:
            print(f"✅ AI evaluation successful - Score: {evaluation_result['overall_score']}/100")
            return True
        else:
            print("❌ AI evaluation returned invalid result")
            return False
            
    except Exception as e:
        print(f"❌ AI evaluator test failed: {e}")
        return False

def test_configuration():
    """Test configuration settings"""
    print("⚙️ Testing configuration...")
    try:
        # Check required configuration values
        required_configs = [
            'SNOWFLAKE_ACCOUNT',
            'SNOWFLAKE_USER', 
            'SNOWFLAKE_PASSWORD',
            'GEMINI_API_KEY'
        ]
        
        for config in required_configs:
            if not hasattr(Config, config) or not getattr(Config, config):
                print(f"❌ Missing configuration: {config}")
                return False
        
        print("✅ All required configurations present")
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("📦 Testing dependencies...")
    try:
        required_modules = [
            'flask',
            'snowflake.connector',
            'pandas',
            'numpy',
            'requests'
        ]
        
        for module in required_modules:
            try:
                __import__(module)
                print(f"✅ {module} - OK")
            except ImportError:
                print(f"❌ {module} - Missing")
                return False
        
        print("✅ All dependencies installed")
        return True
        
    except Exception as e:
        print(f"❌ Dependency test failed: {e}")
        return False

def run_all_tests():
    """Run all system tests"""
    print("🧪 AI Project Evaluator - System Tests")
    print("=" * 50)
    
    tests = [
        ("Dependencies", test_dependencies),
        ("Configuration", test_configuration),
        ("Snowflake Connection", test_snowflake_connection),
        ("AI Evaluator", test_ai_evaluator)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name} test...")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:.<30} {status}")
        if result:
            passed += 1
    
    print("-" * 50)
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! System is ready to run.")
        print("🚀 You can now start the application with: python run.py")
        return True
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        print("🔧 Fix the issues before running the application.")
        return False

def main():
    """Main function"""
    try:
        success = run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n👋 Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
