# PySmallIso

PySmallIso is a isometric game engine written in python. It requires Python and Pygame installed in order to be used. 
## Features
The engine allows to place and manipulate 2.5D (semi 3D) objects in isometric 3D space.It automatically sorts the sprites so that they appear in order, when looking at the scene. The sorting and culling of invisible sprites is done on a seperate thread for performance issuess. It also provides a mechanism to pick sprites by mouse in the isometric world.

## Example
With the engine is provided an example, which you should look at. It shows how the initialization of the engine goes, how to create layers of sprites, add sprites to layers,  and update the sprites. 
To run the file (provided you have Python 2.7 and Pygame installed) enter the project directory and issue the command:
```sh
python Example.py
```
### Notice about game assets
The game assets are the images that the engine uses to render the sprite in isometric world. The sprite are color keyed with a pink color - what means that the pink color is not drawn when the sprite is drawn. Use the **#FF00FF** color value for the places you want to appear transparent during rendering. 

