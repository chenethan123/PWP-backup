from flask import Flask

app = Flask(__name__)

@app.route('/navigate/<direction>', methods=['GET'])
def navigate(direction):  #Retrieve the movement direction from the POST data
  if direction in ['FORWARD', 'BACKWARD', 'RIGHT', 'LEFT', 'STOP']:
    print(f"Moving: {direction}")
    return f"Moving {direction}", 200
  else:
    return "Invalid Direction", 400

if __name__ == '__main__':
    app.run(port=5000)
