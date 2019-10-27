import cherrypy

from pathlib import Path
import os
import os.path
import random
import string

import csv

from collections import defaultdict
from formating import format_forms
from formating import format_question
from formating import format_evaluation

from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('api-key')
question_folder = "./app/"
index_file = "./static/index.html"

def get_questions(folder):
    """Returns a list of lists of strings"""
    questions = list()
    question_files = sorted(Path(folder).glob("*.txt"), key = lambda x: int(x.stem))
    for question_file in question_files:
        with open(question_file) as f:
            f = list(f)
            questions.append(f)
    return questions

watson_min = 100
def standarize_input(text : str):
    """Makes a text watson-ready"""
    if len(text) < watson_min:
        n = int(watson_min/len(text.split())+1)
        evaluation_text = " ".join([text for _ in range(n)])
    else:
        evaluation_text = text
    print(evaluation_text)
    return evaluation_text

def evaluate_personality(text : str) -> dict:
    """Returns dict[metric:str]->value:str
    The output of watson with text as a dict."""
    service = PersonalityInsightsV3(
        version='2017-10-13',
        authenticator=authenticator)
    service.set_service_url('https://gateway.watsonplatform.net/personality-insights/api')

    response = service.profile(
        #profile_json.read(),
        text,
        accept='text/csv',
        csv_headers=True).get_result()

    profile = response.content
    cr = csv.reader(profile.decode('utf-8').splitlines())
    my_list = list(cr)
    return dict(zip(my_list[0], my_list[1]))

class Story(object):
    @cherrypy.expose
    def index(self, error :str = None):
        if 'answers' not in cherrypy.session:
            cherrypy.session['answers'] = list()
        question_n      = len(cherrypy.session['answers'])
        questions       = get_questions(question_folder)
        # Build replacements
        replacements = {
                'errors':"",
                'question':"",
                'form':"",
                'results':"",
        }
        # Open index template
        with open(index_file) as f:
            string_file = "".join(map(str,f))
        # Replace as needed
        if error:
            replacements['errors'] = error
        if question_n >= len(questions):
            # Ya terminó
            try:
                answers = cherrypy.session['answers']
                evaluation_input = standarize_input(" ".join(answers))
                evaluation = evaluate_personality(evaluation_input)
                replacements['results'] = format_evaluation(evaluation)
            except Exception as e:
                replacements['errors']="We can not evaluate you."
                replacements['errors'] += str(e)
            replacements['form'] = restartform
        else:
            # Está en pregunta número question_n
            replacements['question'] = format_question(questions, question_n)
            replacements['form'] = format_forms(question_n)
        # Replace
        print(replacements)
        string_file = string_file.format(**replacements)
        return string_file

    @cherrypy.expose
    def pop(self):
        if 'answers' not in cherrypy.session:
            return self.index()
        if len(cherrypy.session['answers']) > 0:
            cherrypy.session['answers'].pop()
        return self.index()

    @cherrypy.expose
    def restart(self, error = None):
        cherrypy.session['answers'] = list()
        return self.index(error = error)

    @cherrypy.expose
    def put(self, answer=""):
        if answer == "":
            return self.index(error="No empty! CUSTOMiZE THis")
        if 'answers' not in cherrypy.session:
            return self.index()
        cherrypy.session['answers'].append(answer)
        return self.index()

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    webapp = Story()
    cherrypy.quickstart(webapp, '/', conf)
