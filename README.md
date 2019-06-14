<h1 align = "center">Space Invaders in Python</h1>

#### Author - Himanshu Maheshwari

This is a basic space invaders game made in python without the use of pygame or similar libraries. 

#### Gameplay
|Key|Action|
|---|------|
|A|Move left|
|D|Move right|
|Space bar|To launch first kind of missile (i)|
|S|To launch second kind of missile(l)|
|Q| to quit the game

#### Libraries required (Some of them may be already stored)
* time
* datetime
* sys
* select
* tty
* termios
* os
* random

__Use python 2.7__

#### How to play?
cd into directory containg the game and write `python Game.py`.

#### Features
- There is a 8x8 board on terminal containg 3 different elements(all of them having their own classes).

	1) Spaceship​ : Denoted by ^. The spaceship can only move horizontally on Row number 1. That is, it’s movement is restricted from 1x1 to 1x8. 

	2) Aliens​ : Denoted by 'O'. If it is hitted by second missile(l) then it changes to '0'.They randomly spawn anywhere in rows 8 and 7. A new alien is spawned every 10 seconds and last for 8 seconds, after which it self destructs.

	3) Missiles​ : There are two types of missiles: 
		1) i Missile - The missile must move one row up every second. If a missile and alien collide, the alien gets destroyed.  
		2) l Missile - Unlike the first kind of bullet, will move two rows up every second. If this bullet collides with an alien, the  alien will exist on the board for another 5 seconds stunned there. The look of the alien changes to 0 when it collides with this missile. 

- There is a counter for number of aliens shot down by missiles. Aliens that self-destruct obviously do not contribute to this counter! This counter is the score of player. 


- The code is modular and has OOPs principal. `missile` is a parent class and two classes for both kind of missiles inherits from it.

#### Cheers!!!
