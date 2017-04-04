#!/usr/local/Python-3.5.3/bin/python

#import all of the modules you need - cgi and pymysql, and cgitb would help.
#don't forget to enable cgitb
import cgi
import pymysql
import cgitb
cgitb.enable()

#let the internet know that you'll be feeing it html
print("Content-type: text/html\n")

#print out some html! Use string substitutions to make your life easier.
print("""<!DOCTYPE html>
<html>
	<head>
		<style>
				body {
			background-color: #cc0000;
		}

		#headerImage {
			position: relative;
			top: 5px;
			padding-top: -5px;
			padding-top: -5px;
		}

		#header {
			z-index: 1;
			height: 80px;
			position: relative;
			width: 101%;
			background-color: white;
			text-align: center;
			margin-top: -20px;
			margin-left: -8px;
		}

		#bannerImage {
			position: relative;
			height: 80px;
			text-align: center;
			position: relative;
			margin-top: -20px;
			margin-left: -5px;
		}

		table {
			position: absolute;
			background-color: white;
			margin-top: 100px;
			left: 50%; 
			-webkit-transform: translate(-50%, 0);
			
		}

		table {
			position: absolute;
			background-color: white;
			margin-top: 100px;
			left: 50%; 
			-webkit-transform: translate(-50%, 0);
			
		}

		.formBox:hover {
			background-color: #4DC2F4;
		}
			
		p {
			color: black;
			font-size: 30px;
			margin-top: 75px;
			position: relative;
		}
		</style>
		
		<title>Microbial Database</title>
	</head>
	<body>
		<div id="header">
			<h3 id="headerImage"><img id="myImage" src="http://www.bu.edu/anthrop/files/2015/09/2000px-Boston_University_Wordmark.png" width="150"</h3>
		</div>
		<div>
			<h3 id="bannerImage"><img id="banner" src="http://blog.microbiologynetwork.com/wp-content/uploads/2013/02/cropped-bannerSmall.jpg"</h3>
		</div>
		<div>
			<table>
				<tr>
					<td>
						Search Criteria
						<select>
						  <option value="volvo">Species</option>
						  <option value="saab">Metabolism</option>
						  <option value="opel">Relationship</option>
						  <option value="audi">Habitat</option>
						</select>
						<br>
						<br>
						Fields To Display
						<br>
						<input type="checkbox" name="groupCheck">Group Number
						<input type="checkbox" name="semesterCheck">Semester
						<input type="checkbox" name="cultureCheck">Culture
						<input type="checkbox" name="16sCheck">16S-Sequence
						<input type="checkbox" name="genusCheck">Top Genus Result
						<input type="checkbox" name="accuracyCheck">Accuracy Percentage
						<input type="checkbox" name="queryCheck">Query Percentage<br>
						<input type="checkbox" name="o2Check">O2 Requirement
						<input type="checkbox" name="MinPHCheck">Optimal PH (Min)
						<input type="checkbox" name="MaxPHCheck">Optimal PH (Max)
						<input type="checkbox" name="tempCheck">Optimal Temperature
						<input type="checkbox" name="glucoseCheck">Glucose Fermentation
						<input type="checkbox" name="lactoseCheck">Lactose Fermentation<br>
						<input type="checkbox" name="manCheck">Man Fermentation
						<input type="checkbox" name="ofAerobicCheck">OF Aerobic
						<input type="checkbox" name="ofAnaerobicCheck">OF Anaerobic
						<input type="checkbox" name="motilityCheck">Motility
						<input type="checkbox" name="indoleCheck">Indole
						<input type="checkbox" name="sulfurCheck">Sulfur Reduction
						<input type="checkbox" name="caseinCheck">Casein
						<input type="checkbox" name="gelatinCheck">Gelatin<br>
						<input type="checkbox" name="starchCheck">Starch
						<input type="checkbox" name="oxidaseCheck">Oxidase
						<input type="checkbox" name="catalaseCheck">Catalase
						<input type="checkbox" name="gramCheck">Gram
						<input type="checkbox" name="sporeCheck">Spore
						<input type="checkbox" name="validatedCheck">Validated
						<input type="checkbox" name="selectAllCheck">Select All
						<br>
						<br>
					</td>
				</tr>

				<tr>
					<td>
					<form id="search" name="search" action="https://bioed.bu.edu/cgi-bin/students_17/gellerup/search_upload.py" method="post" enctype="multipart/form-data">
					Search:<textarea name="microbe" rows= cols=>Enter Species Name</textarea>
					</form>
					<input class="formBox" type="submit" value="SEARCH">
					<br>
					</td>
				</tr>
				<tr>
					<td>
					Upload a file:<input type="file" name="file_upload" size=100 /><br>
					</td>
				</tr>
			</table>
		</div>
	</body>
</html>""")


