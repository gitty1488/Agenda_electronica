from http.server import HTTPServer, CGIHTTPRequestHandler 
#Adresa serverului
server_address = ('', 80) 
#Creem obiectul Web-server
httpd = HTTPServer(server_address, CGIHTTPRequestHandler) 
#Start Web-server
print('start') 
httpd.serve_forever() 
print('stop')