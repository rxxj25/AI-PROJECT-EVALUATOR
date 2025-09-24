from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import uuid
import json
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY

# Initialize components with fallback to demo mode
try:
    from snowflake_integration import SnowflakeManager
    snowflake_manager = SnowflakeManager()
    print("✅ Snowflake integration loaded successfully")
except Exception as e:
    print(f"⚠️ Snowflake integration failed: {e}")
    print("🔄 Switching to demo mode...")
    from demo_mode import demo_manager as snowflake_manager
    # Create demo data
    from demo_mode import create_demo_data
    create_demo_data()

from ai_evaluator import AIProjectEvaluator
ai_evaluator = AIProjectEvaluator()

@app.route('/')
def index():
    """Main dashboard page"""
    try:
        projects = snowflake_manager.get_all_projects()
        leaderboard = snowflake_manager.get_leaderboard()
        return render_template('index.html', projects=projects, leaderboard=leaderboard)
    except Exception as e:
        flash(f'Error loading dashboard: {str(e)}', 'error')
        return render_template('index.html', projects=[], leaderboard=[])

@app.route('/submit', methods=['GET', 'POST'])
def submit_project():
    """Project submission page"""
    if request.method == 'POST':
        try:
            # Generate unique project ID
            project_id = str(uuid.uuid4())
            
            # Collect form data
            project_data = {
                'project_id': project_id,
                'project_name': request.form.get('project_name'),
                'description': request.form.get('description'),
                'team_name': request.form.get('team_name'),
                'raw_data': {
                    'github_url': request.form.get('github_url', ''),
                    'demo_url': request.form.get('demo_url', ''),
                    'tech_stack': request.form.get('tech_stack', ''),
                    'challenge_category': request.form.get('challenge_category', ''),
                    'additional_notes': request.form.get('additional_notes', '')
                }
            }
            
            # Insert project into Snowflake
            if snowflake_manager.insert_project(project_data):
                flash('Project submitted successfully! Evaluation in progress...', 'success')
                
                # Start AI evaluation
                evaluation_result = ai_evaluator.evaluate_project(project_data)
                
                # Insert evaluation into Snowflake
                if snowflake_manager.insert_evaluation(evaluation_result):
                    flash('AI evaluation completed!', 'success')
                else:
                    flash('Project submitted but evaluation failed. Please contact support.', 'warning')
                
                return redirect(url_for('project_detail', project_id=project_id))
            else:
                flash('Failed to submit project. Please try again.', 'error')
                
        except Exception as e:
            flash(f'Error submitting project: {str(e)}', 'error')
    
    return render_template('submit.html')

@app.route('/project/<project_id>')
def project_detail(project_id):
    """Project detail page with evaluation results"""
    try:
        # Get project details
        projects = snowflake_manager.get_all_projects()
        project = next((p for p in projects if p['PROJECT_ID'] == project_id), None)
        
        if not project:
            flash('Project not found.', 'error')
            return redirect(url_for('index'))
        
        # Get metrics for this project
        metrics = snowflake_manager.get_project_metrics(project_id)
        
        return render_template('project_detail.html', project=project, metrics=metrics)
        
    except Exception as e:
        flash(f'Error loading project details: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/leaderboard')
def leaderboard():
    """Leaderboard page"""
    try:
        leaderboard_data = snowflake_manager.get_leaderboard()
        return render_template('leaderboard.html', leaderboard=leaderboard_data)
    except Exception as e:
        flash(f'Error loading leaderboard: {str(e)}', 'error')
        return render_template('leaderboard.html', leaderboard=[])

@app.route('/api/evaluate', methods=['POST'])
def api_evaluate():
    """API endpoint for real-time evaluation"""
    try:
        data = request.get_json()
        
        if not data or 'project_id' not in data:
            return jsonify({'error': 'Project ID required'}), 400
        
        # Get project data
        projects = snowflake_manager.get_all_projects()
        project = next((p for p in projects if p['PROJECT_ID'] == data['project_id']), None)
        
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        
        # Perform evaluation
        evaluation_result = ai_evaluator.evaluate_project({
            'project_id': project['PROJECT_ID'],
            'project_name': project['PROJECT_NAME'],
            'description': project['DESCRIPTION'],
            'team_name': project['TEAM_NAME'],
            'raw_data': json.loads(project['RAW_DATA']) if project['RAW_DATA'] else {}
        })
        
        # Insert evaluation
        if snowflake_manager.insert_evaluation(evaluation_result):
            return jsonify({
                'success': True,
                'evaluation': evaluation_result
            })
        else:
            return jsonify({'error': 'Failed to save evaluation'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/metrics/<project_id>')
def api_metrics(project_id):
    """API endpoint for project metrics"""
    try:
        metrics = snowflake_manager.get_project_metrics(project_id)
        return jsonify({'metrics': metrics})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/insights')
def api_insights():
    """API endpoint for AI-generated insights"""
    try:
        projects = snowflake_manager.get_all_projects()
        evaluations = []
        
        for project in projects:
            if project.get('OVERALL_SCORE'):
                evaluations.append({
                    'project_name': project['PROJECT_NAME'],
                    'team_name': project['TEAM_NAME'],
                    'overall_score': float(project['OVERALL_SCORE']),
                    'innovation_score': project.get('INNOVATION_SCORE', 0),
                    'technical_score': project.get('TECHNICAL_SCORE', 0),
                    'impact_score': project.get('IMPACT_SCORE', 0),
                    'presentation_score': project.get('PRESENTATION_SCORE', 0)
                })
        
        insights = ai_evaluator.generate_insights(evaluations)
        return jsonify({'insights': insights})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analytics')
def analytics():
    """Analytics dashboard"""
    try:
        projects = snowflake_manager.get_all_projects()
        leaderboard = snowflake_manager.get_leaderboard()
        
        # Calculate statistics
        total_projects = len(projects)
        evaluated_projects = len([p for p in projects if p.get('OVERALL_SCORE')])
        avg_score = sum([float(p['OVERALL_SCORE']) for p in projects if p.get('OVERALL_SCORE')]) / evaluated_projects if evaluated_projects > 0 else 0
        
        return render_template('analytics.html', 
                             total_projects=total_projects,
                             evaluated_projects=evaluated_projects,
                             avg_score=round(avg_score, 2),
                             leaderboard=leaderboard)
    except Exception as e:
        flash(f'Error loading analytics: {str(e)}', 'error')
        return render_template('analytics.html', total_projects=0, evaluated_projects=0, avg_score=0, leaderboard=[])

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host='0.0.0.0', port=5000)
