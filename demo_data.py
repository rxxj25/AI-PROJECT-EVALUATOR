#!/usr/bin/env python3
"""
Demo Data Generator for AI Project Evaluator
Creates sample projects to demonstrate the system capabilities
"""

import uuid
import json
from datetime import datetime, timedelta
from snowflake_integration import SnowflakeManager
from ai_evaluator import AIProjectEvaluator

def create_demo_projects():
    """Create sample projects for demonstration"""
    
    # Initialize components
    snowflake_manager = SnowflakeManager()
    ai_evaluator = AIProjectEvaluator()
    
    # Sample project data
    demo_projects = [
        {
            'project_name': 'FinTech AI Assistant',
            'description': 'An intelligent AI assistant that helps users manage their finances, provides investment advice, and automates budgeting. Uses machine learning to analyze spending patterns and suggest personalized financial strategies.',
            'team_name': 'AI Finance Wizards',
            'raw_data': {
                'github_url': 'https://github.com/example/fintech-ai',
                'demo_url': 'https://demo.fintech-ai.com',
                'tech_stack': 'Python, TensorFlow, React, Snowflake, OpenAI',
                'challenge_category': 'fintech',
                'additional_notes': 'Focuses on democratizing financial advice through AI'
            }
        },
        {
            'project_name': 'Sustainable Energy Tracker',
            'description': 'A comprehensive platform that tracks renewable energy usage, carbon footprint, and provides recommendations for sustainable living. Integrates with smart home devices and energy providers.',
            'team_name': 'GreenTech Innovators',
            'raw_data': {
                'github_url': 'https://github.com/example/sustainable-tracker',
                'demo_url': 'https://demo.sustainable-tracker.com',
                'tech_stack': 'Node.js, MongoDB, IoT, Machine Learning',
                'challenge_category': 'sustainability',
                'additional_notes': 'Real-time energy monitoring and carbon offset recommendations'
            }
        },
        {
            'project_name': 'Social Impact Marketplace',
            'description': 'A platform connecting social entrepreneurs with investors and volunteers. Features include project funding, skill matching, and impact measurement tools.',
            'team_name': 'Social Impact Squad',
            'raw_data': {
                'github_url': 'https://github.com/example/social-marketplace',
                'demo_url': 'https://demo.social-marketplace.com',
                'tech_stack': 'React, Node.js, PostgreSQL, Blockchain',
                'challenge_category': 'social-impact',
                'additional_notes': 'Blockchain-based transparency and impact verification'
            }
        },
        {
            'project_name': 'AI-Powered Healthcare Diagnostics',
            'description': 'An AI system that analyzes medical images and patient data to assist healthcare professionals in diagnosis. Uses deep learning for pattern recognition and early disease detection.',
            'team_name': 'MedTech Pioneers',
            'raw_data': {
                'github_url': 'https://github.com/example/healthcare-ai',
                'demo_url': 'https://demo.healthcare-ai.com',
                'tech_stack': 'Python, PyTorch, Medical Imaging APIs, HIPAA Compliance',
                'challenge_category': 'ai-ml',
                'additional_notes': 'FDA compliance considerations and clinical trial data'
            }
        },
        {
            'project_name': 'Smart City Traffic Optimization',
            'description': 'An intelligent traffic management system that uses real-time data and AI to optimize traffic flow, reduce congestion, and improve urban mobility.',
            'team_name': 'UrbanTech Solutions',
            'raw_data': {
                'github_url': 'https://github.com/example/traffic-optimization',
                'demo_url': 'https://demo.traffic-optimization.com',
                'tech_stack': 'Python, Computer Vision, IoT Sensors, Cloud Computing',
                'challenge_category': 'data-analytics',
                'additional_notes': 'Integration with city infrastructure and emergency services'
            }
        }
    ]
    
    print("🚀 Creating demo projects...")
    print("=" * 50)
    
    for i, project_data in enumerate(demo_projects, 1):
        # Generate unique project ID
        project_id = str(uuid.uuid4())
        project_data['project_id'] = project_id
        
        print(f"📝 Creating project {i}: {project_data['project_name']}")
        
        # Insert project into Snowflake
        if snowflake_manager.insert_project(project_data):
            print(f"✅ Project inserted successfully")
            
            # Perform AI evaluation
            print(f"🤖 Running AI evaluation...")
            evaluation_result = ai_evaluator.evaluate_project(project_data)
            
            # Insert evaluation
            if snowflake_manager.insert_evaluation(evaluation_result):
                print(f"✅ Evaluation completed - Score: {evaluation_result['overall_score']}/100")
            else:
                print(f"❌ Evaluation failed")
        else:
            print(f"❌ Project insertion failed")
        
        print("-" * 30)
    
    print("🎉 Demo data creation completed!")
    print("=" * 50)
    print("📊 You can now view the projects in the dashboard")
    print("🏅 Check the leaderboard for rankings")
    print("📈 Explore analytics for insights")

def main():
    """Main function"""
    try:
        create_demo_projects()
    except Exception as e:
        print(f"❌ Error creating demo data: {e}")
        print("Make sure Snowflake connection is working and dependencies are installed")

if __name__ == '__main__':
    main()
