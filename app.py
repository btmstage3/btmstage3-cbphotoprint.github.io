import cgi

# Get the form data
form = cgi.FieldStorage()
num_photos = form.getvalue('num_photos')

# Generate the passport photos
# ...

# Output the results as an HTML response
print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>Passport Photo Results</title>")
print("</head>")
print("<body>")
print("<h1>Passport Photo Results</h1>")
print("<p>Number of photos printed: {0}</p>".format(num_photos))
print("</body>")
print("</html>")
 




