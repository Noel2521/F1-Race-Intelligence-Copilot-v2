import json
import boto3
import joblib
import numpy as np
import os
import tempfile
 
# These will be set as environment variables in Lambda console
BUCKET_NAME = os.environ.get('S3_BUCKET', 'noel-f1-intelligence-2024')
MODEL_KEY = os.environ.get('MODEL_KEY', 'lap_time_predictor.pkl')
 
# Global variable — model loads once and stays in memory
# This means it only downloads from S3 on the FIRST request
# All subsequent requests are much faster
model = None
 
 
def load_model():
    '''Download model from S3 and load into memory'''
    global model
    if model is not None:
        return model  # Already loaded, skip download
    
    s3 = boto3.client('s3')
    # Lambda can only write to /tmp folder
    with tempfile.NamedTemporaryFile(suffix='.pkl', delete=False) as tmp:
        s3.download_file(BUCKET_NAME, MODEL_KEY, tmp.name)
        model = joblib.load(tmp.name)
    
    return model
 
 
def handler(event, context):
    '''
    Main Lambda handler — called on every API request
    event: contains the HTTP request data
    context: AWS runtime info (we dont use this)
    '''
    try:
        # Parse the request body
        body = json.loads(event.get('body', '{}'))
        
        # Extract features from request
        # These match exactly the features our model was trained on
        lap_number = float(body.get('LapNumber', 20))
        stint = float(body.get('Stint', 1))
        tyre_life = float(body.get('TyreLife', 10))
        tyre_life_sq = tyre_life ** 2
        compound_encoded = float(body.get('CompoundEncoded', 1))
        is_out_lap = float(body.get('IsOutLap', 0))
        is_in_lap = float(body.get('IsInLap', 0))
        speed_i1 = float(body.get('SpeedI1', 280))
        speed_i2 = float(body.get('SpeedI2', 255))
        speed_fl = float(body.get('SpeedFL', 245))
        speed_st = float(body.get('SpeedST', 300))
        
        # Build feature array in EXACT same order as training
        features = [[
            lap_number, stint, tyre_life, tyre_life_sq,
            compound_encoded, is_out_lap, is_in_lap,
            speed_i1, speed_i2, speed_fl, speed_st
        ]]
        
        # Load model and predict
        mdl = load_model()
        prediction = float(mdl.predict(features)[0])
        
        # Format as minutes:seconds
        minutes = int(prediction // 60)
        seconds = prediction % 60
        formatted = f'{minutes}:{seconds:.3f}'
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'predicted_lap_time_seconds': round(prediction, 3),
                'predicted_lap_time_formatted': formatted,
                'status': 'success'
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': str(e),
                'status': 'failed'
            })
        }
