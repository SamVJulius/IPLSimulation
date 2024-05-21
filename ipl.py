from flask import Flask, render_template, request
from io import StringIO
import sys
from main import game

ipl = Flask(__name__)

# Route to display the form
@ipl.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@ipl.route('/', methods=['POST'])
def start_game():
    # Get team names from the form
    team_one = request.form['team1']
    team_two = request.form['team2']

    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the game function with team names
    game(False, team_one, team_two)
    
    # Get the printed output and reset stdout
    output = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    
    # Replace newline characters with HTML line breaks
    output = output.replace('\n', '<br>')
    output_list = output.split('<br>')
    
    return render_template('output.html', output_list=output_list)

if __name__ == '__main__':
    ipl.run(debug=True)
