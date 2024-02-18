import nbformat
import json
import requests
from IPython.display import display, HTML
import webbrowser, tempfile, os

class NotebookGrader:
    def __init__(self, course_id, assignment_id, notebook_name, feedback_in_browser=True):
        self.assignment_id = assignment_id
        self.course_id = course_id
        self.notebook_name = notebook_name
        self.notebook_data = None
        self.feedback_in_browser = feedback_in_browser
        

    def load_notebook(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.notebook_data = nbformat.read(file, as_version=4)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            self.notebook_data = None

    def grade(self):
        self.load_notebook(self.notebook_name)
        if self.notebook_data is not None:
            print(f"Grading notebook")
            # Convert notebook data to JSON
            notebook_json = nbformat.writes(self.notebook_data)

            payload = {
                'notebook': json.loads(notebook_json),
                'course_id': self.course_id,
                'assignment_id': self.assignment_id
            }

            # URL of your Flask server's grade endpoint
            url = 'http://127.0.0.1:5000/grade'
            
            # Make POST request to Flask server
            response = requests.post(url, json=payload)

            # Handle the response
            if response.status_code == 200:
                print("Grading completed successfully.")
                result = response.json()
                print("Grade:", result['score'])
                
                if self.feedback_in_browser:
                    # Create a temporary file to write the HTML content
                    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as temp_file:
                        temp_file.write(result['html'])
                        filepath = temp_file.name

                    # Open the temporary HTML file in the default browser
                    webbrowser.open_new_tab(f'file://{filepath}')
                else:
                    display(HTML("<style>.output { max-height: 400px; overflow-y: scroll; }</style>"))
                    display(HTML(result['html'])) 

            else:
                print("Error in grading:", response.text)
        else:
            print("No notebook data loaded. Please load a notebook first.")