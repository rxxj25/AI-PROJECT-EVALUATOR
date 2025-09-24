# AI-Powered Project Evaluator for NatWest Hackathon

A comprehensive AI-powered project evaluation system that integrates with Snowflake for real-time data management and uses Google's Gemini AI for intelligent project assessment.

## 🚀 Features

### Core Functionality
- **AI-Powered Evaluation**: Uses Google Gemini AI to evaluate projects across multiple criteria
- **Real-time Snowflake Integration**: Seamless data upload and management in Snowflake
- **Comprehensive Scoring**: Multi-dimensional evaluation (Innovation, Technical, Impact, Presentation)
- **Live Dashboard**: Real-time project tracking and leaderboard
- **Advanced Analytics**: Detailed insights and trend analysis

### Key Components
- **Project Submission Portal**: User-friendly interface for project submission
- **AI Evaluation Engine**: Intelligent scoring using Gemini AI
- **Real-time Metrics**: Live tracking of project performance
- **Leaderboard System**: Dynamic ranking and competition tracking
- **Analytics Dashboard**: Comprehensive data visualization and insights

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Interface │    │  AI Evaluator   │    │   Snowflake     │
│                 │    │                 │    │                 │
│  - Dashboard    │◄──►│  - Gemini AI    │◄──►│  - Projects     │
│  - Submission   │    │  - Scoring      │    │  - Evaluations  │
│  - Analytics    │    │  - Feedback     │    │  - Metrics      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: Snowflake (Cloud Data Warehouse)
- **AI Engine**: Google Gemini Pro
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Charts**: Chart.js
- **Icons**: Font Awesome

## 📋 Prerequisites

- Python 3.8+
- Snowflake account (provided for hackathon)
- Google Gemini API key
- Modern web browser

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd ai-project-evaluator
pip install -r requirements.txt
```

### 2. Configuration
The system is pre-configured with your hackathon credentials:
- **Snowflake Account**: `sfsehol-natwest_learnaix_hack4acause_zrkzae`
- **Username**: `USER`
- **Password**: `sn0wf@ll`
- **Gemini API Key**: `AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk`

### 3. Run the Application
```bash
python app.py
```

### 4. Access the Application
Open your browser and navigate to: `http://localhost:5000`

## 📊 Evaluation Criteria

The AI evaluates projects across four key dimensions:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Innovation** | 25% | Novelty and creativity of the solution |
| **Technical Excellence** | 30% | Quality of implementation and code |
| **Impact** | 25% | Potential for real-world change |
| **Presentation** | 20% | Clarity and documentation quality |

## 🎯 How It Works

### 1. Project Submission
- Teams submit projects through the web interface
- Project data is immediately stored in Snowflake
- AI evaluation process is triggered automatically

### 2. AI Evaluation
- Gemini AI analyzes project details
- Scores are generated for each criterion
- Comprehensive feedback is provided
- Results are stored in real-time

### 3. Real-time Updates
- Dashboard updates automatically
- Leaderboard reflects current standings
- Analytics provide ongoing insights

## 📈 Key Features

### Dashboard
- **Project Overview**: Total projects, evaluation status, average scores
- **Recent Activity**: Latest submissions and evaluations
- **Quick Actions**: Easy navigation to key functions

### Project Submission
- **Comprehensive Form**: Detailed project information collection
- **Real-time Validation**: Instant feedback on form completion
- **Auto-save**: Prevents data loss during submission

### Leaderboard
- **Top 3 Podium**: Visual representation of top performers
- **Complete Rankings**: Full list with detailed scores
- **Category Leaders**: Best performers in each evaluation area

### Analytics
- **Score Trends**: Visual representation of performance over time
- **Category Analysis**: Breakdown by evaluation criteria
- **AI Insights**: Intelligent analysis and recommendations

## 🔧 API Endpoints

### Core Endpoints
- `GET /` - Main dashboard
- `GET /submit` - Project submission form
- `POST /submit` - Submit new project
- `GET /project/<id>` - Project details
- `GET /leaderboard` - Current rankings
- `GET /analytics` - Analytics dashboard

### API Endpoints
- `POST /api/evaluate` - Trigger AI evaluation
- `GET /api/metrics/<project_id>` - Get project metrics
- `GET /api/insights` - Generate AI insights

## 🗄️ Database Schema

### Projects Table
```sql
CREATE TABLE projects (
    project_id VARCHAR(50) PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    description TEXT,
    team_name VARCHAR(255),
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    status VARCHAR(50) DEFAULT 'submitted',
    raw_data VARIANT
);
```

### Evaluations Table
```sql
CREATE TABLE evaluations (
    evaluation_id VARCHAR(50) PRIMARY KEY,
    project_id VARCHAR(50),
    innovation_score INTEGER,
    technical_score INTEGER,
    impact_score INTEGER,
    presentation_score INTEGER,
    overall_score DECIMAL(5,2),
    feedback TEXT,
    evaluation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    evaluator_type VARCHAR(50) DEFAULT 'ai',
    detailed_scores VARIANT
);
```

### Real-time Metrics Table
```sql
CREATE TABLE real_time_metrics (
    metric_id VARCHAR(50) PRIMARY KEY,
    project_id VARCHAR(50),
    metric_type VARCHAR(100),
    metric_value DECIMAL(10,4),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    metadata VARIANT
);
```

## 🎨 UI/UX Features

### Modern Design
- **Gradient Backgrounds**: Eye-catching visual appeal
- **Glass Morphism**: Modern translucent design elements
- **Responsive Layout**: Works on all device sizes
- **Smooth Animations**: Engaging user interactions

### User Experience
- **Intuitive Navigation**: Easy-to-use interface
- **Real-time Feedback**: Instant status updates
- **Auto-refresh**: Live data updates
- **Error Handling**: Graceful error management

## 🔒 Security Features

- **Input Validation**: Comprehensive form validation
- **SQL Injection Protection**: Parameterized queries
- **XSS Prevention**: Output sanitization
- **Error Handling**: Secure error messages

## 📱 Mobile Responsiveness

The application is fully responsive and optimized for:
- **Desktop**: Full-featured experience
- **Tablet**: Adapted layout and interactions
- **Mobile**: Touch-optimized interface

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🎯 Hackathon Advantages

### For Judges
- **Consistent Evaluation**: AI ensures fair and consistent scoring
- **Comprehensive Analysis**: Multi-dimensional project assessment
- **Real-time Insights**: Live tracking of all submissions
- **Detailed Feedback**: Actionable insights for participants

### For Participants
- **Fair Assessment**: Objective AI evaluation
- **Immediate Feedback**: Instant scoring and feedback
- **Transparent Process**: Clear evaluation criteria
- **Competitive Spirit**: Live leaderboard and rankings

### For Organizers
- **Efficient Management**: Automated evaluation process
- **Data Analytics**: Comprehensive insights and trends
- **Scalable Solution**: Handles any number of submissions
- **Professional Presentation**: Polished, modern interface

## 🏆 Winning Features

1. **AI-Powered Intelligence**: Advanced AI evaluation using Gemini
2. **Real-time Integration**: Seamless Snowflake data management
3. **Professional UI/UX**: Modern, responsive design
4. **Comprehensive Analytics**: Deep insights and visualizations
5. **Scalable Architecture**: Enterprise-ready solution
6. **Hackathon Focused**: Built specifically for competition evaluation

## 📞 Support

For technical support or questions during the hackathon:
- Check the application logs for error details
- Ensure all dependencies are installed
- Verify Snowflake connectivity
- Confirm Gemini API key is valid

## 🎉 Ready to Win!

This AI-powered project evaluator is designed to give you a competitive edge in the NatWest Hackathon. With its advanced AI capabilities, real-time data integration, and professional presentation, it demonstrates innovation, technical excellence, and real-world impact.

**Good luck with your hackathon submission!** 🚀