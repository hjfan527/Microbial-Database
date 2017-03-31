#!/usr/local/Python-3.5.3/bin/python
import cgi
import cgitb
cgitb.enable()
import pymysql

print("Content-type: text/html\n")

print("""<!DOCTYPE html>
<html>
	<head>
		<title>Microbial Database</title>
		<link type="text/css" rel="stylesheet" href="stylesheet.css" />
	</head>
	<body>
		<div id="header">
			<h3 id="headerImage"><img id="myImage" src="http://www.bu.edu/anthrop/files/2015/09/2000px-Boston_University_Wordmark.png" width="150"</h3>
		</div>
		<table>
			<tr>
				<td><form id="search" name="search" action="https://bioed.bu.edu/cgi-bin/students_17/gellerup/search_upload.py" method="post" enctype="multipart/form-data">
				Enter a microbe:<textarea name="microbe" rows= cols=>Microbe to search</textarea><br />
				</form><br /></td>
				<td><input type="submit" value="SEARCH" /></td>
			</tr>
			<tr>
				<td>
				Upload a file:<input type="file" name="file_upload" size=100 /><br />
				<br />
				</td>
			</tr>
		</table>
	</body>
</html>""")