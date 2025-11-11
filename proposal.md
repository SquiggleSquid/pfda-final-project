
# Title
8-Ball Juggle

## Repository
<Link to your project's public GitHub respository>
This site was built using [GitHub Pages](https://github.com/SquiggleSquid/pfda-final-project)

## Description
For my project, I would like to make a juggling (Game&Watch type) game. That will spawn a set amount of balls as time passes, and the goal of the game is to repeatedly bounce back the balls for the longest amount of time and prevent any of the balls from hitting the death plane (bottom of screen). 
It's relevant to media and digital arts because it's a game experience, focusing on multi-tasking as part of its core game loop.

## Features
- 1- Ball translating in random direction
	- Using an update and draw method in a class, and import random
- 2- Making a moving platform/racket
	- Using keyboard inputs or mouse clicks to move the platform to bounce back the ball
- N - Making a death plane
	- So when ball goes inside, game over (using end of screen height)

## Challenges
- Need to refresh memory on organizing class and methods for game functions
- Need to research Pygame documentation on mouse inputs
- Need to refresh memory on how the make text appear in the center of the screen

## Outcomes
Ideal Outcome:
- It will spawns a maximum of 8 balls (based on the title), and will all move in different directions and speeds. As you have to move the mouse to drag your racket (or platform) to make the balls bounce upwards again. 
- With a score system to keep track of how many times you hit the balls, a timer for how long the in game time has gotten to, and a 'game over' screen text that appears if the ball goes into the death plane.

Minimal Viable Outcome:
- As long as one ball works, and a certain type of keyboard input works to control where your racket (or platform) is. With the game simply ending, or freezing when the ball goes into the death plane.

## Milestones

- Week 1
  1. Create class for single ball
  2. Create main function for basic game loop (dt, screen size, etc)

- Week 2
  1. Add update and draw method code inside the ball class
  2. Implement racket (or platform) that moves via keyboard or mouse controls

- Week N (Final)
  1. Implement death plane
  2. Make multiple balls spawn as time goes on (8 in total)
  3. And or debug, debug, and debug!

