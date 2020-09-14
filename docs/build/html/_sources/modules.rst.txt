=======
Modules
=======

Modules have been designed to specifically for Python Adventures to enable you to design graphics and sounds to accompany your creations.

-------
Pattern
-------

The pattern module allows the creation of patterns that can be outputted in the form of 3-bit bitmap graphics or sounds.

This example program shows the pattern module in use::

	import pattern

	print("Pattern [1], Pattern [2], Pattern [3]")
	choice = input("Choice: ")

	if choice == "1":
		#load pre-defined pattern
		pattern.load(pattern.happy)
	elif choice == "2":
		#create custom graphic
		pattern.size(4,4)
		pattern.custom("0011:1100:0011:1100")
	elif choice == "3":
		#set individual pixels in a loop
		pattern.size(6,6)
		for i in range(36):
			pattern.pixel(i,pattern.nextColor())

+--------------------------+----------------------------------------+---------------------+
| Function                 | Description                            | Example             |
|                          |                                        |                     |
+==========================+========================================+=====================+
| size(width, height)      | Creates a blank pattern of a set size. | .size(2,2)          |
+--------------------------+----------------------------------------+---------------------+
| custom(string)           | Defines and displays a custom pattern. | .custom("00:11")    |
+--------------------------+----------------------------------------+---------------------+
| load(pattern name)       | Loads a pre-defined pattern.           | .load("happy")      |
+--------------------------+----------------------------------------+---------------------+
| pixel(pixel no., colour) | Sets an individual pixel, they are     | .pixel(0,2)         |
|                          | numbered starting at 0 in the top left.|                     |
+--------------------------+----------------------------------------+---------------------+
| play()                   | Plays the current pattern using piano  | .play()             |
|                          | notes to represent each colour.        |                     |
+--------------------------+----------------------------------------+---------------------+
| sing()                   | Play the current pattern using the     | .sing()             |
|                          | sofege scale.                          |                     |
+--------------------------+----------------------------------------+---------------------+
| images()                 | Lists the pre-defined patterns.        | .images()           |
+--------------------------+----------------------------------------+---------------------+
| nextColor()              | Returns a different colour each time   | .nextColor          |
|                          | it is called.                          |                     |
+--------------------------+----------------------------------------+---------------------+

^^^^^^^^^^^
Colours
^^^^^^^^^^^

The graphics are represented in 3-bit colour, which allows for 8 colours. The table below indicates the available colours and their codes:

+---------------+-----------+
| Colour        | Code      |
|               |           |
+===============+===========+
| Black         | 0         |
+---------------+-----------+
| Blue          | 1         |
+---------------+-----------+
| Green         | 2         |
+---------------+-----------+
| Cyan          | 3         |
+---------------+-----------+
| Red           | 4         |
+---------------+-----------+
| Magenta       | 5         |
+---------------+-----------+
| Yellow        | 6         |
+---------------+-----------+
| White         | 7         |
+---------------+-----------+

-----
Music
-----

The music module allows the creation of music from piano notes.

This example program shows the music module in use::

	import music

	print("Tune [1], Tune [2]")
	choice = input("Choice: ")

	if choice == "1":
		#load pre-defined tune
		music.play(music.twinkle)
	elif choice == "2":
		#create custom tune
		music.play("c4:5,d4,e4,f4,g4,a4,b4,c5")

+-----------------+----------------------------------------+-------------------------+
| Function        | Description                            | Example                 |
|                 |                                        |                         |
+=================+========================================+=========================+
| play(tune)      | Plays either a pre-defined or custom   | .play(pattern.twinkle)  |
|                 | tune.                                  | .play("c4:4,d4,e4")     |
+-----------------+----------------------------------------+-------------------------+
| tunes()         | Lists the pre-defined tunes   .        | .tunes()                |
+-----------------+----------------------------------------+-------------------------+

^^^^^^^^^^^
Tune Format
^^^^^^^^^^^

Tunes are defined as a string of notes separated by commas. The octave is set using a number straight after the note, for example c4 is middle C.
The duration of a note is set by adding a colon followed the desired duration. For example "c4:5" would play middle C for half a second. The same duration is used for each subsequent note until a new duration is set.