"""This modules implements functions to transform to HTML"""

popform = '<form method="get" action="pop"><button class="button" type="submit">Back</button></form>'
putform = '<form method="get" action="put"><input minlength="20" type="text" id="toCount" value="" required name="answer" /><button class="button" type="submit">Speak</button></form>'
restartform = '<form method="get" action="restart"><button class="button" type="submit">Restart</button></form>'

questionform = '\
      <h5>Escribe tu respuesta:</h5>\
        <div class="grid-x grid-padding-x">\
          <div class="large-12 cell">\
          {forms}\
          </div>\
        </div>\
'

questiontemplate = '\
      <div class="grid-x grid-padding-x">\
        <div class="large-12 cell">\
          <div class="callout">\
            <h2>{questiontitle}</h2>\
            <h4>{questiontext}</h4>\
          </div>\
        </div>\
      </div>\
      <hr/>\
'
resultstemplate = '\
      <div class="grid-x grid-padding-x">\
        <div class="large-12 cell">\
          <div class="callout">\
            <h2>{metric}</h2>\
            <h4>{value}</h4>\
          </div>\
        </div>\
      </div>\
      <hr/>\
'

def format_question(questions : list, index : int):
    question = [q.strip() for q in questions[index]]
    title = question[0]
    text  = "\n".join(question[1:])
    html = questiontemplate.format(questiontitle = title, questiontext = text)
    #print(html)   
    return html

def format_forms(index : int):
    forms = str()
    forms += putform
    if index > 0:
        forms += popform
    forms += restartform
    html = questionform.format(forms = forms)
    #print(html)   
    return html

def format_evaluation(evaluation : dict):
    html = str()
    fake = lambda x: zip(x.keys(), x.values())
    for metric, value in fake(evaluation):
        html += resultstemplate.format(metric=metric, value=value)
    #print(html)   
    return html

