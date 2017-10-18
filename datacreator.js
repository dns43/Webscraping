
//The following commands are needed to be excuted in the data processing directory before using the code:

//1.  npm init

//2.  npm install esprima
//  npm install estraverse
  
//3.  npm install file-api

//4.  npm install escope

var fs = require('fs');
var esprima = require('esprima');
var escope = require('escope');
	 
 var FileAPI = require('file-api')
 , File = FileAPI.File
 , FileList = FileAPI.FileList
 , FileReader = FileAPI.FileReader
 ;
var loc = "C:\\Users\\dns43\\Desktop\\Drexel\\webscraper\\data\\";
 console.log("dennis:"+loc);
 var path = require('path');
 var js_files = [];

 
 //var FileReader = require('filereader');  
 function trimHashbang(code) {
	    if (code.substring(0, 2) === '#!') {
	        var end = code.indexOf('\n');
	        var filler = '';
	        for (var i = 0; i < end; ++i) {
	           filler += ' ';
	        }
	        code = filler + code.substring(end, code.length);
	    }
	    return code;
	}
 
 
 function processDir(startPath,filter)
 {
	         
           if (!fs.existsSync(startPath))
           {
               console.log("no dir ",startPath);
               return;
           }

           var files=fs.readdirSync(startPath);
           
           var extension = '.js';
       //    js_files = files.filter(function(file){
       // 	    return file.indexOf(extension) !== -1;
       // 	});
           
           //console.log(files);
           for(var i=0;i<files.length;i++)
           {
        	  
        	   
        	   //var filename=path.join(startPath,files[i]);

        	   
        	  // var fileReader = new FileReader();
        	   
        	   var filename=path.join(startPath,files[i]);
        	   var filename_without_path = files[i];
        	  
               
               var stat = fs.lstatSync(filename);
               if (stat.isDirectory()){
            	   processDir(filename,filter); //recurse

               }
               else if (filename.indexOf(filter)>=0) 
               {
            	   (function(file){
            	   
            	   js_files.push(filename);
            	   //dns43: this is depricated ant not working on every browser/version
            	   //dns43: revised it using the File System (fs) Library
            	   //dns43: var file = new File(filename);
                   var f = fs.openSync(filename, "a+");

            	   var exact_filename = filename_without_path.slice(0, -3);
            	   console.log(exact_filename);
            	   	   
            	   	//console.log(txt_filename);
            	   	 // var ast_filename = startPath + '/' + exact_filename + '.ast'; 
            	    
                  var txt_filename = startPath + "\\"+exact_filename + '.txt';
                  console.log("filename:"+txt_filename);
                  //dns43:this is depricated ant not working on every browser/version
            	  //dns43: revised it using the File System (fs) Library
                  //var fileReader = new FileReader();
                  var contents = fs.readFileSync(f,"utf8")
                  //dns43: var fileReader = fs.readFileSync(f,"utf8",(err,data)=>contents=data)
               	  //dns43:fileReader.readAsBinaryString(file, 'utf-8');

            	   //dns43:fileReader.readAsBinaryString(file);
               	  
               	
            	   
               	//dns43: commented out these lines, no more necessary
               	//dns43:fileReader.onload = function(event) 
             	  //dns43:{
            		   //dns43:this is depricated ant not working on every browser/version
            	  	   //dns43: revised it using the File System (fs) Library
               	 	  //dns43:var contents = fileReader.data;
                   fs.writeFileSync(txt_filename, contents)//dns43:, function(error)
           	    	//dns43: commented out these lines, no more necessary
           	    	//	dns43:{
           	    	// dns43:		if(error)
           	    	 	//dns43:		{
           	    	 		//dns43:		console.error("write error: " + error.message);
           	    	 		//dns43:	}
           	    	 		//dns43:console.log('1');
           	    	 	//dns43:	else
           	    	 			//dns43:{
           	    	 		//dns43:		console.log("successful write to " + txt_filename);
           	    	 			//dns43:}
           	    	 //dns43:	});
 /*          	 fs.writeFile(ast_filename, data, function(error)
           	 	{
           	 		if(error)
           	 			{
           	 				console.error("write error: " + error.message);
           	 			}
           	 		else
           	 			{
           	 				console.log("successful write to " + ast_filename);
           	 			}
           	 	});
*/                   
              // };
               
               //fileReader.onerror = function(event) 
         	  //{
         	  //    console.error("File could not be read! Code " + event.target.error.code);
         	  //}; 
             	
               //};
               
        	  //dns43};
        	  //fileReader.readAsBinaryString(file);
           
            	   })(files[i]);
        	  
        	  
           };
       };
 };
       //fromDir('../LiteScript','.html');       
       
 processDir(loc,'.js');
       
       //console.log(js_files);
       
       function processAST(startPath)
       {
    	   
  	 	 
  	 	for(var i=0;i<js_files.length;i++)
        {
  	 		//console.log(i + ' ' + js_files[i]);
  	 		
  	 	 (function(file){
        //dns43: OPEN JS FILE
        console.log(js_files[i]);
        //dns43:this is depricated ant not working on every browser/version
        //dns43: revised it using the File System (fs) Library
        //dns43: var file = new File(js_files[i]);      	 	  
        var f = fs.openSync(js_files[i], "a+");
     	   
         //dns43: EXCHANGE FILE EXTENSIONS
         var exact_filename = js_files[i].slice(0, -3)
     	   	
     	   	   var ast_filename = exact_filename + '.ast'; 
     //console.log(ast_filename);
     		//dns43:this is depricated ant not working on every browser/version
        	//dns43: revised it using the File System (fs) Library
     	    //dns43:var fileReader = new FileReader();
     	    //dns43:fileReader.readAsBinaryString(file, 'utf-8');
            //dns43: READ FILE
            var contents = fs.readFileSync(f,"utf8")
            
        	  //dns43: commented out these lines, no more necessary	
        	  //dns43:fileReader.onload = function(event) 
         	  //dns43:{
        		 //dns43: var  contents = fileReader.result; 
             //dns43: trim hasbang
        		  var processed_content = trimHashbang(contents);
        		//  var module = { exports: {} } (function (require, module, exports) {  processed_content })(require, module, exports)
        		  var data = JSON.stringify(esprima.parse(processed_content, { sourceType: 'script',
        			  sourceType: 'module', jsx: true, tolerant: true, tokens: true, range: true, loc: true, comment: true }),null, 4);
        		  
        		 // var data = esprima.parse(processed_content, { sourceType: 'script',
        		//	  sourceType: 'module', jsx: true, tolerant: true, tokens: true, range: true, loc: true, comment: true });
        		  
        		  /***
    			   * 
    			   * try without JSON
    			   * 
    			   * 
    			   ***/
        		  
        		  //console.log(contents);
        		  //console.log('*****************');
        		  //console.log(ast_filename);
        		//dns43: commented out these lines, no more necessarý
              //dns43: write AST from esprima to astfilname
        		  fs.writeFileSync(ast_filename, data)//dns43:, function(error)
        	           	 	//dns43: commented out these lines, no more necessary
        	           	 	//dns43:{
        	           	 	//dns43:	if(error)
        	           	 	//dns43:		{
        	           	 	//dns43:			console.error("write error: " + error.message);
        	           	 	//dns43:		}
        	           	 	//dns43:	else
        	           	 	//dns43:		{
        	           	 	//dns43:			console.log("successful write to " + ast_filename);
        	           	 	//dns43:		}
        	           	 	//dns43:});
         	  //dns43};
  	 	 })(js_files[i]);  
  	 		
        };
  	 	 
       };
       
       processAST(loc);

       //dns43: commented out the function calles "processDOT"
       //dns43: it generated a filed called .dot that isn't actualla a .dot file
       // dns43: thought this to be confusing
           	    	