import snowflake.connector
from snowflake.connector import DictCursor
import pandas as pd
from datetime import datetime
import json
from config import Config

class SnowflakeManager:
    def __init__(self):
        self.conn = None
        self.connect()
        self.setup_tables()
    
    def connect(self):
        """Establish connection to Snowflake"""
        try:
            # First connect without specifying database/schema
            self.conn = snowflake.connector.connect(
                user=Config.SNOWFLAKE_USER,
                password=Config.SNOWFLAKE_PASSWORD,
                account=Config.SNOWFLAKE_ACCOUNT,
                warehouse=Config.SNOWFLAKE_WAREHOUSE
            )
            
            # Create database and schema if they don't exist
            cursor = self.conn.cursor()
            try:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.SNOWFLAKE_DATABASE}")
                cursor.execute(f"USE DATABASE {Config.SNOWFLAKE_DATABASE}")
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {Config.SNOWFLAKE_SCHEMA}")
                cursor.execute(f"USE SCHEMA {Config.SNOWFLAKE_SCHEMA}")
                print("Successfully connected to Snowflake!")
            except Exception as e:
                print(f"Warning: Could not create database/schema: {e}")
                # Try to use existing database
                try:
                    cursor.execute(f"USE DATABASE {Config.SNOWFLAKE_DATABASE}")
                    cursor.execute(f"USE SCHEMA {Config.SNOWFLAKE_SCHEMA}")
                except:
                    # Use default database
                    cursor.execute("USE DATABASE SNOWFLAKE_SAMPLE_DATA")
                    cursor.execute("USE SCHEMA TPCH_SF1")
            finally:
                cursor.close()
                
        except Exception as e:
            print(f"Error connecting to Snowflake: {e}")
            raise
    
    def setup_tables(self):
        """Create necessary tables for the project evaluator"""
        cursor = self.conn.cursor()
        
        try:
            # Drop existing tables if they exist
            cursor.execute("DROP TABLE IF EXISTS real_time_metrics")
            cursor.execute("DROP TABLE IF EXISTS evaluations")
            cursor.execute("DROP TABLE IF EXISTS projects")
            
            # Create projects table
            create_projects_table = """
            CREATE TABLE projects (
                project_id VARCHAR(50) PRIMARY KEY,
                project_name VARCHAR(255) NOT NULL,
                description TEXT,
                team_name VARCHAR(255),
                submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
                status VARCHAR(50) DEFAULT 'submitted',
                raw_data TEXT
            )
            """
            
            # Create evaluations table
            create_evaluations_table = """
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
                detailed_scores TEXT,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            )
            """
            
            # Create real-time metrics table
            create_metrics_table = """
            CREATE TABLE real_time_metrics (
                metric_id VARCHAR(50) PRIMARY KEY,
                project_id VARCHAR(50),
                metric_type VARCHAR(100),
                metric_value DECIMAL(10,4),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
                metadata TEXT,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            )
            """
            
            cursor.execute(create_projects_table)
            cursor.execute(create_evaluations_table)
            cursor.execute(create_metrics_table)
            self.conn.commit()
            print("Tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()
    
    def insert_project(self, project_data):
        """Insert a new project into the database"""
        cursor = self.conn.cursor()
        
        insert_query = """
        INSERT INTO projects (project_id, project_name, description, team_name, raw_data)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        try:
            # Convert raw_data to JSON string
            raw_data_json = json.dumps(project_data.get('raw_data', {}))
            cursor.execute(insert_query, (
                project_data['project_id'],
                project_data['project_name'],
                project_data['description'],
                project_data['team_name'],
                raw_data_json
            ))
            self.conn.commit()
            print(f"Project {project_data['project_id']} inserted successfully!")
            return True
        except Exception as e:
            print(f"Error inserting project: {e}")
            return False
        finally:
            cursor.close()
    
    def insert_evaluation(self, evaluation_data):
        """Insert evaluation results into the database"""
        cursor = self.conn.cursor()
        
        insert_query = """
        INSERT INTO evaluations (
            evaluation_id, project_id, innovation_score, technical_score,
            impact_score, presentation_score, overall_score, feedback,
            detailed_scores
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        try:
            # Convert detailed_scores to JSON string
            detailed_scores_json = json.dumps(evaluation_data.get('detailed_scores', {}))
            cursor.execute(insert_query, (
                evaluation_data['evaluation_id'],
                evaluation_data['project_id'],
                evaluation_data['innovation_score'],
                evaluation_data['technical_score'],
                evaluation_data['impact_score'],
                evaluation_data['presentation_score'],
                evaluation_data['overall_score'],
                evaluation_data['feedback'],
                detailed_scores_json
            ))
            self.conn.commit()
            print(f"Evaluation {evaluation_data['evaluation_id']} inserted successfully!")
            return True
        except Exception as e:
            print(f"Error inserting evaluation: {e}")
            return False
        finally:
            cursor.close()
    
    def insert_metric(self, metric_data):
        """Insert real-time metrics into the database"""
        cursor = self.conn.cursor()
        
        insert_query = """
        INSERT INTO real_time_metrics (metric_id, project_id, metric_type, metric_value, metadata)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        try:
            # Convert metadata to JSON string
            metadata_json = json.dumps(metric_data.get('metadata', {}))
            cursor.execute(insert_query, (
                metric_data['metric_id'],
                metric_data['project_id'],
                metric_data['metric_type'],
                metric_data['metric_value'],
                metadata_json
            ))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting metric: {e}")
            return False
        finally:
            cursor.close()
    
    def get_all_projects(self):
        """Retrieve all projects with their evaluations"""
        cursor = self.conn.cursor(DictCursor)
        
        query = """
        SELECT p.*, e.overall_score, e.feedback, e.evaluation_date
        FROM projects p
        LEFT JOIN evaluations e ON p.project_id = e.project_id
        ORDER BY p.submission_date DESC
        """
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error retrieving projects: {e}")
            return []
        finally:
            cursor.close()
    
    def get_project_metrics(self, project_id):
        """Get real-time metrics for a specific project"""
        cursor = self.conn.cursor(DictCursor)
        
        query = """
        SELECT * FROM real_time_metrics
        WHERE project_id = %s
        ORDER BY timestamp DESC
        """
        
        try:
            cursor.execute(query, (project_id,))
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error retrieving metrics: {e}")
            return []
        finally:
            cursor.close()
    
    def get_leaderboard(self):
        """Get the current leaderboard"""
        cursor = self.conn.cursor(DictCursor)
        
        query = """
        SELECT p.project_name, p.team_name, e.overall_score, e.innovation_score,
               e.technical_score, e.impact_score, e.presentation_score
        FROM projects p
        JOIN evaluations e ON p.project_id = e.project_id
        ORDER BY e.overall_score DESC
        """
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error retrieving leaderboard: {e}")
            return []
        finally:
            cursor.close()
    
    def close(self):
        """Close the Snowflake connection"""
        if self.conn:
            self.conn.close()
            print("Snowflake connection closed.")
