from flask import Flask , jsonify, request
import json
from pymongo import MongoClient 

app = Flask(__name__)
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
db = conn.influr
  

@app.route('/<keywords>', methods=['GET','POST'])
def get_all_keywords(keywords):
	if request.method=='POST':
	    keywords = db.keywords 
	    data= request.get_json(force=True)
	    key= data['keyword']
	    keys=key.split()
	    lst=['the','at','there','some','my','of','be','use','her','than','and'	,'this','an','would','first','best']
	    def filterKey(key):
		    if(key in lst):
		        return False
		    else:
		        return True
	    


	    filteredKeys = list(filter(filterKey, keys))
	    length= len(filteredKeys)
	    partial = []
	    complete = [] 
	    for q in keywords.find():
	    	c=False
	    	a=0
	    	p=False
	    	s=q['Keyword'].split()
	    	for i in s:
	    		if(i in filteredKeys):
	    			a+=1
	    			p=True
	    		if(a==length):
	    			c=True
	    	if(c):
	    		complete.append(q['Keyword'])
	    	elif(p):
	        	partial.append(q['Keyword'])
	    return jsonify({'partial match' :partial, 'complete match' :complete})
if __name__ == "__main__":
    app.run(debug=True)