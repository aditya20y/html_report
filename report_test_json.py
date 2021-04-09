import json
from json2html import *
import pandas as pd
with open("results.json", 'r') as f:
    data = json.load(f)
d1 = data["tests"][0]
d2 = d1["tests"][0]
d3 = d2["tests"][0]
json_data = json.dumps(d3)
html_syn = json2html.convert(json=json_data)
content = ''
with open("multiplelevel_normalized_data1.html", 'w') as r:
    r.write(html_syn)

with open("multiplelevel_normalized_data1.html", 'r') as d:
    content += d.read()

print(content)

# data = content.split('<tr>')
# for i in data:
#     pass
#
# print(data)

# manipulating table content
new_content = content.replace('table border="1"', 'table class="table table-bordered" border="6px;"')
new_content = new_content.replace('<td>FAIL</td>', '<td style="background-color:#F20D0D;">FAIL</td>')
new_content = new_content.replace('<td>PASS</td>', '<td style="background-color:#06BA24;">PASS</td>')
new_content = new_content.replace('<th>', '<th style="background-color:	#00BFFF;">')
new_content = new_content.replace('<th style="background-color:	#00BFFF;">detail</th>',
                                  '<th style="background-color:	#00BFFF;width:400px;">Detail</th>')
new_content = new_content.replace('<tr><th style="background-color:	#00BFFF;">lineNo</th><td>1</td></tr>', '')

# for table toggling
new_content = new_content.replace('<th style="background-color:	#00BFFF;">tests</th>', '<th style="background-color:	#00BFFF; cursor:pointer;" id="first">Tests [+]</th>', 1)
new_content = new_content.replace('<th style="background-color:	#00BFFF;">tests</th>', '<th style="background-color:	#00BFFF;">Tests <a href="#">[+]</a></th>')

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

