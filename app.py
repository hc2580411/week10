from flask import Flask, jsonify 
import os 

app = Flask(__name__) 
@app.route('/') 
def home(): 
    # Get instance name from environment variable 
    instance_name = os.getenv('INSTANCE_NAME', 'RPS') 
    return jsonify({ 
    "message": f"Welcome to {instance_name}!", 
    "instructions": "You can play Rock-Paper-Scissors here." 
}) 

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000)