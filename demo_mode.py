#!/usr/bin/env python3
"""
Demo Mode for AI Project Evaluator
This version works without Snowflake for demonstration purposes
"""

import json
import uuid
from datetime import datetime
from ai_evaluator import AIProjectEvaluator

class DemoDataManager:
    """In-memory data manager for demo purposes"""
    
    def __init__(self):
        self.projects = []
        self.evaluations = []
        self.metrics = []
        self.ai_evaluator = AIProjectEvaluator()
    
    def insert_project(self, project_data):
        """Insert a new project"""
        self.projects.append(project_data)
        print(f"Demo: Project {project_data['project_id']} inserted")
        return True
    
    def insert_evaluation(self, evaluation_data):
        """Insert evaluation results"""
        self.evaluations.append(evaluation_data)
        print(f"Demo: Evaluation {evaluation_data['evaluation_id']} inserted")
        return True
    
    def insert_metric(self, metric_data):
        """Insert real-time metrics"""
        self.metrics.append(metric_data)
        return True
    
    def get_all_projects(self):
        """Get all projects with evaluations"""
        result = []
        for project in self.projects:
            # Find evaluation for this project
            evaluation = next((e for e in self.evaluations if e['project_id'] == project['project_id']), None)
            
            project_dict = {
                'PROJECT_ID': project['project_id'],
                'PROJECT_NAME': project['project_name'],
                'DESCRIPTION': project['description'],
                'TEAM_NAME': project['team_name'],
                'SUBMISSION_DATE': datetime.now(),
                'STATUS': 'evaluated' if evaluation else 'submitted',
                'RAW_DATA': json.dumps(project.get('raw_data', {})),
                'OVERALL_SCORE': evaluation['overall_score'] if evaluation else None,
                'INNOVATION_SCORE': evaluation['innovation_score'] if evaluation else None,
                'TECHNICAL_SCORE': evaluation['technical_score'] if evaluation else None,
                'IMPACT_SCORE': evaluation['impact_score'] if evaluation else None,
                'PRESENTATION_SCORE': evaluation['presentation_score'] if evaluation else None,
                'FEEDBACK': evaluation['feedback'] if evaluation else None,
                'EVALUATION_DATE': evaluation['evaluation_date'] if evaluation else None
            }
            result.append(project_dict)
        
        return result
    
    def get_leaderboard(self):
        """Get the current leaderboard"""
        result = []
        for evaluation in self.evaluations:
            # Find project for this evaluation
            project = next((p for p in self.projects if p['project_id'] == evaluation['project_id']), None)
            if project:
                result.append({
                    'PROJECT_NAME': project['project_name'],
                    'TEAM_NAME': project['team_name'],
                    'OVERALL_SCORE': evaluation['overall_score'],
                    'INNOVATION_SCORE': evaluation['innovation_score'],
                    'TECHNICAL_SCORE': evaluation['technical_score'],
                    'IMPACT_SCORE': evaluation['impact_score'],
                    'PRESENTATION_SCORE': evaluation['presentation_score']
                })
        
        # Sort by overall score
        result.sort(key=lambda x: x['OVERALL_SCORE'], reverse=True)
        return result
    
    def get_project_metrics(self, project_id):
        """Get metrics for a specific project"""
        return [m for m in self.metrics if m['project_id'] == project_id]

# Global demo data manager
demo_manager = DemoDataManager()

def create_demo_data():
    """Create some demo projects for demonstration"""
    demo_projects = [
        {
            'project_id': str(uuid.uuid4()),
            'project_name': 'AI-Powered Financial Advisor',
            'description': 'An intelligent AI system that provides personalized financial advice using machine learning algorithms to analyze user spending patterns and investment goals.',
            'team_name': 'FinTech Innovators',
            'raw_data': {
                'github_url': 'https://github.com/example/financial-advisor',
                'demo_url': 'https://demo.financial-advisor.com',
                'tech_stack': 'Python, TensorFlow, React, Snowflake',
                'challenge_category': 'fintech'
            }
        },
        {
            'project_id': str(uuid.uuid4()),
            'project_name': 'Sustainable Energy Tracker',
            'description': 'A comprehensive platform that tracks renewable energy usage and provides recommendations for sustainable living with real-time carbon footprint monitoring.',
            'team_name': 'GreenTech Solutions',
            'raw_data': {
                'github_url': 'https://github.com/example/energy-tracker',
                'demo_url': 'https://demo.energy-tracker.com',
                'tech_stack': 'Node.js, IoT, Machine Learning',
                'challenge_category': 'sustainability'
            }
        },
        {
            'project_id': str(uuid.uuid4()),
            'project_name': 'Social Impact Marketplace',
            'description': 'A platform connecting social entrepreneurs with investors and volunteers, featuring blockchain-based transparency and impact verification.',
            'team_name': 'Social Impact Squad',
            'raw_data': {
                'github_url': 'https://github.com/example/social-marketplace',
                'demo_url': 'https://demo.social-marketplace.com',
                'tech_stack': 'React, Node.js, Blockchain',
                'challenge_category': 'social-impact'
            }
        }
    ]
    
    print("🚀 Creating demo projects...")
    
    for project_data in demo_projects:
        # Insert project
        demo_manager.insert_project(project_data)
        
        # Evaluate project
        evaluation_result = demo_manager.ai_evaluator.evaluate_project(project_data)
        demo_manager.insert_evaluation(evaluation_result)
        
        # Add some metrics
        for i in range(3):
            metric_data = {
                'metric_id': str(uuid.uuid4()),
                'project_id': project_data['project_id'],
                'metric_type': f'Performance Metric {i+1}',
                'metric_value': 75.0 + (i * 5),
                'metadata': {'source': 'demo'}
            }
            demo_manager.insert_metric(metric_data)
    
    print("✅ Demo data created successfully!")
    print(f"📊 Created {len(demo_projects)} projects with evaluations")

if __name__ == '__main__':
    create_demo_data()
