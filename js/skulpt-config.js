function outf(text) { 
    var mypre = document.getElementById("print-output"); 
    mypre.innerHTML = mypre.innerHTML + text;
	$("#print-output").scrollTop($("#print-output")[0].scrollHeight);
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

Sk.configure({
   inputfun: function () {
       var mypre = document.getElementById("print-output"); 
		mypre.innerHTML = mypre.innerHTML + "<input id='input'>"; 
	  document.getElementById("input").focus();
      return new Promise(function(resolve,reject){
         $("#input").on("keyup",function(e){
             if (e.keyCode == 13)
             {
                 $("#input").off("keyup");
                 resolve($("#input").val());
				 mypre.innerHTML = mypre.innerHTML + $("#input").val() + "<br>";
				$( "#input" ).remove();
             }
         })
      })
   },
   output: outf,
   read: builtinRead
});



function runit(event) {
	event.preventDefault();
   var mypre = document.getElementById("print-output"); 
   mypre.innerHTML = ''; 
var prog = editor.getValue();
            Sk.configure({output: outf,
                 read: builtinRead,
                 __future__: Sk.python3});
            Sk.canvas = "image";
            if (editor.getValue().indexOf('turtle') > -1 ) {
                $('#image').show()
            }
            Sk.pre = "print-output";
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'image';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       
   },
       function(err) {
       outf(err.toString());
   });
} 