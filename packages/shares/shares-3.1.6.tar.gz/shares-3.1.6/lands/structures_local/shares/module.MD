
---

# "shares" is no longer the name of this endeavor.    
## The endeavor continues as "sphene"   
[https://pypi.org/project/sphene](https://pypi.org/project/sphene)    

If there are problems with "shares", change requests    
might still be addressed.   

******

Bravo!  You have received a Mercantilism Diploma in "shares" from     
the Orbital Convergence University International Air and Water  
Embassy of the 🍊 Planet (the planet that is one ellipse further from  
the Sun than Earth's ellipse).  

You are now officially certified to include "shares" in your practice.  

******


# shares

---

## description
Started from the shell, "shares" presents files in the current working directory (cwd) that have extension ".s.HTML" (case sensitive).

---		
		
## install
`[ZSH] pip install shares`

---


## start from shell
`[ZSH] shares`

Shares starts on port 2345, or the first avaible port after that.  
 * Running on http://127.0.0.1:2345  

This is the equivalent of:   
`[ZSH] shares start --port 2345`   

--
  
Alternatively you can add `--static-port` and "shares"   
stops if the port specified is unavailable.  
`[ZSH] shares start --port 2345 --static-port`   

--

### This is an example ".s.HTML" file.


```
<pre>
	<h1>This is an example HTML file.</h1>
	<p>
		It really only needs the "pre" tag to    
		look like a reflection of its contents in a browser.   
	</p>   
	<p>
		Tags like "html" and "body" are actually not   
		necessary for rendering HTML in modern browsers.  
	</p>   
	<p>  
		for text to wrap, instead of extending off the page,    
		style "white-space: pre-wrap" can be utilized instead of 
		a "pre" tag like so:
		
		<div style="white-space: pre-wrap"></div>
	</p>
</pre>
```


However, here is the "CSS1Compat" option,   
[https://developer.mozilla.org/en-US/docs/Web/HTML/Quirks_Mode_and_Standards_Mode](https://developer.mozilla.org/en-US/docs/Web/HTML/Quirks_Mode_and_Standards_Mode)   

with scaling based on the browser screen "viewport" of the screen,  
[https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)  

and support for UTF-8 characters.    
[http://www.unicode.org/charts](http://www.unicode.org/charts)    
[https://www.w3.org/International/questions/qa-html-encoding-declarations]([https://www.w3.org/International/questions/qa-html-encoding-declarations])     



```
<!doctype html>
<html>
	<head>	
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
	</head>
	<body>
		<main>
			<article style="white-space: pre-wrap">
				
			
			</article>
		</main>
	</body>
</html>
```

---

## start programmatically
```
import pathlib
from os.path import dirname, join, normpath
this_folder = pathlib.Path (__file__).parent.resolve ()

import shares
shares.start ({
	"extension": ".s.HTML",
	
	#
	#	This is the node from which the traversal occur.
	#
	"directory": str (this_folder) + "/structures/shares",
	
	#
	#	This path is removed from the absolute path of share files found.
	#
	"relative path": str (this_folder) + "/structures/shares"
})

import time
while True:
	time.sleep (1000)
```

---

## Contacts
bgrace2345@pm.me