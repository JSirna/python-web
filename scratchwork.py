import csv
with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Name'] + ['Date'] + ['Name2'] + ['Date2'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])