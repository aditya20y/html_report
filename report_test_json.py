import json
from json2html import *
import pandas as pd
with open("results.json", 'r') as f:
    data = json.load(f)
d1 = data["tests"][0]
d2 = d1["tests"][0]
d3 = d2["tests"][0]

# to change the scenerio numbering from 1, 2...
total_scenirio = d3["tests"]

for i in range(len(total_scenirio)):
    total_scenirio_dict = d3["tests"][i]
    # change the steps numbering from 1,2..
    total_steps = total_scenirio_dict['tests']
    # print(total_steps)
    for j in range(len(total_steps)):
        # print(d3['tests'][i]['tests'][j]['lineNo'])
        d3['tests'][i]['tests'][j]['lineNo'] = j+1
    d3['tests'][i]['lineNo'] = i+1
# print(d3)

json_data = json.dumps(d3)
html_syn = json2html.convert(json=json_data)
content = ''
with open("multiplelevel_normalized_data1.html", 'w') as r:
    r.write(html_syn)

with open("multiplelevel_normalized_data1.html", 'r') as d:
    content += d.read()


# manipulating table content
new_content = content.replace('table border="1"', 'table class="table table-bordered" border="6px;"')
new_content = new_content.replace('<td>FAIL</td>', '<td style="background-color:#F20D0D;">FAIL</td>')
new_content = new_content.replace('<td>PASS</td>', '<td style="background-color:#06BA24;">PASS</td>')
new_content = new_content.replace('<th>', '<th style="background-color:	#00BFFF;">')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">detail</th>',
                                  '<th style="background-color:	#00BFFF;width:400px;">Detail</th>')
new_content = new_content.replace('<tr><th style="background-color:	#00BFFF;">lineNo</th><td>1</td></tr>', '')

# for table toggling
new_content = new_content.replace('<th style="background-color:	#00BFFF;">tests</th>',
                                  '<th style="background-color:	#00BFFF; cursor:pointer;" id="first">Tests [+]</th>', 1)
new_content = new_content.replace('<th style="background-color:	#00BFFF;">tests</th>',
                                  '<th style="background-color:	#00BFFF;">Tests <a href="#">[+]</a></th>')


# to change the Line no to Scenerio no
new_content = new_content.replace('<th style="background-color:	#00BFFF;">lineNo</th>',
                                  '<th style="background-color:	#00BFFF;">ScenerioNo</th>', 1)
# to change the Line no to Step no
for i in range(len(total_scenirio)):
    new_content = new_content.replace('<th style="background-color:	#00BFFF;">lineNo</th>',
                                      '<th style="background-color:	#00BFFF;">StepNo</th>', i+2)

# for capitalizing headers
new_content = new_content.replace('<th style="background-color:	#00BFFF;">description</th>',
                                  '<th style="background-color:	#00BFFF;">Description</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">name</th>',
                                  '<th style="background-color:	#00BFFF;">Name</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">start</th>',
                                  '<th style="background-color:	#00BFFF;">Start</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">type</th>',
                                  '<th style="background-color:	#00BFFF;">Type</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">uri</th>',
                                  '<th style="background-color:	#00BFFF;">Uri</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">stop</th>',
                                  '<th style="background-color:	#00BFFF;">Stop</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">lineNo</th>',
                                  '<th style="background-color:	#00BFFF;">LineNo</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">result</th>',
                                  '<th style="background-color:	#00BFFF;">Result</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">text</th>',
                                  '<th style="background-color:	#00BFFF;">Text</th>')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">time</th>',
                                  '<th style="background-color:	#00BFFF;">Time</th>')

# removing uri from step level
# new_content = new_content.replace('<th style="background-color:	#00BFFF;">Uri</th>',
#                                   '', 3)
# print(new_content)

with open("multiplelevel_normalized_data1.html", 'w+') as t:

    t.seek(0, 0)
    html_head = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <title>Test Report</title>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
            <style>

            </style>
        </head>
        <body>
    '''

    j_script = '''
        <script>
           $('table table table').hide();
           $('th > a').on('click', function(e) {
                $('table table table').toggle();
                e.preventDefault();
        
            });
            
            $('#first').on('click', function(e) {
                $('table table').toggle();
                e.preventDefault();

            });

        </script>
    '''

    t.write(html_head + "\n" + new_content + "\n" + "</body>" + "\n" + j_script + "\n" + "</html>")


print("Report generation complete")

