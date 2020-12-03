//configure the editor window
var editor;
var instr;
var colMode = "btnnorm";

function setup() {
	window.editor = ace.edit("source");
	window.editor.setTheme("ace/theme/chrome");
	window.editor.session.setMode("ace/mode/python");
	window.instr = ace.edit("directions");
};

setup();

document.getElementById("run").addEventListener("click", runit);

$("#info_btn").click(function(event){
	event.preventDefault();
	if ($("#directions").css("height") == "0px") {
		$("#directions").css("height", "400px");
		$("#source").css("height", "0px");
		$("#info_btn").removeClass("icon");
		$("#info_btn").addClass("inactive");
		$("#code_btn").removeClass("inactive");
		$("#code_btn").addClass("icon");
		$("#directions").addClass("active");
			
	window.instr.setTheme("ace/theme/chrome");
	window.instr.session.setMode("ace/mode/text");
	window.instr.session.setOption('indentedSoftWrap', false);
	window.instr.session.setUseWrapMode(true);
	window.instr.renderer.setShowGutter(false)
	}
});

$("#code_btn").click(function(event){
	event.preventDefault();
	if ($("#source").css("height") == "0px") {
		$("#directions").css("height", "0px");
		$("#source").css("height", "400px");
		$("#code_btn").removeClass("icon");
		$("#code_btn").addClass("inactive");
		$("#info_btn").removeClass("inactive");
		$("#info_btn").addClass("icon")
	}
});

//event listeners and functions for changing the text size
$("#txt_s").click(function(event){
	event.preventDefault();
	$("#content").css("font-size", "0.8em");
});

$("#txt_m").click(function(event){
	event.preventDefault();
	$("#content").css("font-size", "1em");
});

$("#txt_l").click(function(event){
	event.preventDefault();
	$("#content").css("font-size", "1.6em");
});

//event listeners and functions for changing the colour scheme
$("#col_n").click(function(event){
	event.preventDefault();
	colMode = "btnnorm";
	editor.setTheme("ace/theme/chrome");
	$(".head").css("background-color", "#006666");
	$("#print-output").css("background-color", "#ffffff");
	$("#print-output").css("color", "#4b4e4d");
	$("#callfunctions").css("background-color", "#ffffff");
	$("#callfunctions").css("color", "#4b4e4d");
	$("h1").css("color", "#006666");
	$("body").css("background-color", "#33cccc");
	$("#fname").css("border-color", "#006666");
	$("#image").css("background-color", "#ffffff");
	$(".button").addClass("btnnorm");
	$(".button").removeClass("btndis");
	$(".button").removeClass("btnhigh");
});

$("#col_h").click(function(event){
	event.preventDefault();
	colMode = "btnhigh";
	editor.setTheme("ace/theme/dracula");
	$(".head").css("background-color", "#717773");
	$("#print-output").css("background-color", "#282A36");
	$("#print-output").css("color", "#ffffff");
	$("#callfunctions").css("background-color", "#282A36");
	$("#callfunctions").css("color", "#ffffff");
	$("h1").css("color", "#000000");
	$("body").css("background-color", "#ffffff");
	$("#fname").css("border-color", "#282A36");
	$("#image").css("background-color", "#282A36");
	$(".button").addClass("btnhigh");
	$(".button").removeClass("btndis");
	$(".button").removeClass("btnnorm");
});

$("#col_d").click(function(event){
	event.preventDefault();
	colMode = "btndis";
	editor.setTheme("ace/theme/solarized_light");
	$(".head").css("background-color", "#717773");
	$("#print-output").css("background-color", "#FDF6E3");
	$("#print-output").css("color", "#717773");
	$("#callfunctions").css("background-color", "#FDF6E3");
	$("#callfunctions").css("color", "#717773");
	$("h1").css("color", "#ffffff");
	$("body").css("background-color", "#54B39B");
	$("#fname").css("border-color", "#717773");
	$("#image").css("background-color", "#FDF6E3");
	$(".button").addClass("btndis");
	$(".button").removeClass("btnhigh");
	$(".button").removeClass("btnnorm");
});

//event listener and function for saving as a Python file
$("#saveBtn").click(function(event){
	event.preventDefault();
	var blob = new Blob([editor.getValue()], {type: "text/plain;charset=utf-8"});
	saveAs(blob, $("#fname").val());
});

//event listeners and fucntions for loading a Python file
var fileSelector = document.getElementById('pyfile');
  fileSelector.addEventListener('change', (event) => {
    var file = event.target.files[0];
	reader.readAsText(file);
	$("#fname").val(file.name);
  });
  
var reader = new FileReader();
  reader.addEventListener('load', (event) => {
    editor.session.setValue(event.target.result);
  });
  
//Exports whole page with current code state as an html file
$("#exportBtn").click(function(event){
	event.preventDefault();
	var filen = $("#fname").val();
	var name = filen.replace(".py",".html");
	var code = window.editor.getValue();
	var instructions = window.instr.getValue();
	var source = document.getElementById("source");
	var directions = document.getElementById("directions"); 
    source.innerHTML = code;
	directions.innerHTML = instructions; 
	var blob = new Blob([$("html").html()], {type: "text/html;charset=utf-8"});
	saveAs(blob, name);
	window.editor.destroy();
	window.instr.destroy();
	$editor = $('ACE_ID');
	$editor.remove();
	source.innerHTML = code; 
	directions.innerHTML = instructions; 
	setup();
});

//event listener for a new function call
$("#call").click(function(event){
	event.preventDefault();
	var name = prompt("Function Call");
	var prog = editor.getValue()+"\n"+name;

   var mypre = document.getElementById("print-output"); 
   mypre.innerHTML = ''; 

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
   var btn = document.createElement("BUTTON"); 
	btn.innerHTML = name;
	btn.classList.add("button");
	btn.classList.add("callbtn");
	btn.classList.add(colMode);
   $("#callfunctions").append(btn);
   btn.addEventListener("click", call);
});

try {
	$( ".callbtn" ).on( "click", function(event) {
	event.preventDefault();
   var mypre = document.getElementById("print-output"); 
   mypre.innerHTML = ''; 

            Sk.configure({output: outf,
                 read: builtinRead,
                 __future__: Sk.python3});
            Sk.canvas = "image";
            if (editor.getValue().indexOf('turtle') > -1 ) {
                $('#image').show()
            }
            Sk.pre = "print-output";
            (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'image';
            try {
                Sk.misceval.asyncToPromise(function() {
                    return Sk.importMainWithBody("<stdin>",false,editor.getValue(),true);
                });
            } catch(e) {
                outf(e.toString() + "\n")
            }
	});
} catch {
	
};

//call a function
function call(event){
	event.preventDefault();
	var prog = editor.getValue()+"\n"+event.target.innerText;
   var mypre = document.getElementById("print-output"); 
   mypre.innerHTML = ''; 
   Sk.pre = "print-output";
   Sk.configure({output:outf, read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'image';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       
   },
       function(err) {
       outf(err.toString());
   });
};

//clear function calls
$("#clearfuncs").click(function(event){
	event.preventDefault();
   var funcs = document.getElementById("callfunctions"); 
   funcs.innerHTML = ''; 
});

//about modal window
var modal = document.getElementById("myModal");
var abt = document.getElementById("about");
var spn = document.getElementsByClassName("close")[0];

abt.onclick = function(event) {
	event.preventDefault();
  modal.style.display = "block";
}

spn.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//event listener for a new function call
$("#b0").click(function(event){
	event.preventDefault();
	var mypre = document.getElementById("input"); 
	mypre.value = mypre.value + "0";
	val = mypre.value
	if (val.length == 8) {
		var textArea = document.getElementById('input');
		var keyboardEvent = new KeyboardEvent('keyup', {
        code: 'Enter',
        key: 'Enter',
        charKode: 13,
        keyCode: 13,
        view: window,
		bubbles: true
    });
    textArea.dispatchEvent(keyboardEvent);
	}
});

$("#b1").click(function(event){
	event.preventDefault();
	var mypre = document.getElementById("input"); 
	mypre.value = mypre.value + "1";
	val = mypre.value
	if (val.length == 8) {
		var textArea = document.getElementById('input');
		var keyboardEvent = new KeyboardEvent('keyup', {
        code: 'Enter',
        key: 'Enter',
        charKode: 13,
        keyCode: 13,
        view: window,
		bubbles: true
    });

    textArea.dispatchEvent(keyboardEvent);
	}
});