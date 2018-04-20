#! usr/local/bin/python3

import bs4
import openpyxl

def write(pages, filename):

	output = openpyxl.Workbook()
	outSheet = output.active
	itr = 1
	# configureOutput()

	for page in pages: 

		comments = page.select(".mainContent")

		for comment in comments:

			row = []

			if comment.find('span', {'class' : 'userLocation'}) == None:
				row.append("")
			else:
				row.append(comment.find('span', {'class' : 'userLocation'}).text.strip())
			row.append(comment.find('span', {'class' : 'ratingDate'})["title"].strip())
			row.append(comment.find('span', {'class' : 'ui_bubble_rating'})["class"][1][7:].strip())
			row.append(comment.find('span', {'class' : 'noQuotes'}).text.strip())
			text = comment.find('p', {'class' : 'partial_entry'}).text.strip() 
			text = text.split('\n')
			row.append(" ".join(text))
			# print(str(itr) + ". " + str(row))

			outSheet['A' + str(itr)] = row[0]
			outSheet['B' + str(itr)] = row[1]
			outSheet['C' + str(itr)] = row[2]
			outSheet['D' + str(itr)] = row[3]
			outSheet['E' + str(itr)] = row[4]

			itr += 1

	output.save("%s.xlsx" % filename)

def configureOutput():

    outSheet.column_dimensions['A'].width = 10
    outSheet.column_dimensions['B'].width = 10
    outSheet.column_dimensions['C'].width = 5
    outSheet.column_dimensions['D'].width = 20
    outSheet.column_dimensions['E'].width = 30