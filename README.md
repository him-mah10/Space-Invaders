There is a 8x8 board on terminal
There are 3 different elements (all of them having their own classes): 
 
a. Spaceship​ : Denote/draw this using any character (preferably a special 
character). The spaceship can only be moved horizontally on Row number 1. 
That is, it’s movement is restricted from 1x1 to 1x8. Move it using key ‘A’ to move 
left and key ‘D’ to move it to the right. 
b. Aliens​ : Again, denote them using any random character. The must be randomly 
spawned anywhere in rows 8 and 7. A new alien must be spawned every 10 
seconds and each alien must last for 8 seconds, after which it self destructs.  
c. Missiles​ : There are two types of missiles: 
i.
Used the character ‘i’ to denote a missile. A missile is spawned each time 
the spacebar is clicked and is always spawned in the (row+1, column) 
block if the spaceship is in (row, column) when spacebar is clicked. For 
example, if the spaceship is in (1, 2) when spacebar is hit, the missile 
spawns in (2,2). The missile must move one row up every second. If a 
missile and alien collide, the alien gets destroyed.  
ii.
Used the character ‘l’ to denote the second form of missile. This missile is 
shot when the ‘S’ key is clicked, and unlike the first kind of bullet, will 
move two rows up every second. If this bullet collides with an alien, the 
alien will exist on the board for another 5 seconds. Also slightly change 
the look of the alien when this missile collides with it. 
 
Used inheritance here: with a parent class ‘missile’, and two classes that then inherit from this. 
If the user presses the ‘Q’ button, the game is quit. 
 
Kept a counter for number of aliens shot down by missiles. Aliens that self-destruct obviously 
do not contribute to this counter!. This counter will be score of player. 

The game has been made without using pygame.
