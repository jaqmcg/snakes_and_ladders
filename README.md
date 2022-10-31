# snakes_and_ladders


Here is one of my first python programs I made in my second year of university.

## Background

Prior to making this program we had learnt some basics about python such as functions and classes. We had also learnt about some data structures such as JSON. THe main goal for this assignment was to use JSON, functions, and classes in one program and create a game. 

## Objectives

  The key objecttives for this assignment are as follows:
  * practice the skill of taking a problem description and how to model and represent the problem in programming code
  * practice the skill of working with functions
  * practice the skill of working with collections
  * practice the skill of working with objects
  * engage in a deeper understanding of the concepts taught and introduced through the process of reflection
  
## Requirements

My requirements for this assignment were to create a snakes and ladders game where a player and computer compete to get to position 100 first. We had to use a JSON string to allocate where the snakes and ladders were on the gameboard as well as what positions these lead to. We also had to create a class for the dice which holds the method `rollDice()`.

The JSON string I had to use was as follows:
```
{
	"name": "snake_lader_Positions",
	"boardPosition": [
		{
			"position": 3,
			"moveTo": 15		
		},
		{
			"position": 8,
			"moveTo": 2		
		},
		{
			"position": 11,
			"moveTo": 9		
		},
		{
			"position": 12,
			"moveTo": 20		
		},
		{
			"position": 30,
			"moveTo": 10		
		},
		{
			"position": 45,
			"moveTo": 55		
		},
		{
			"position": 60,
			"moveTo": 75		
		}											
	]
}
```

## Example

An example of the game is as follows:

```
Welcome to yourName's game of Snakes and Ladders You are playing the computer - all the Best 
Player1: Hit enter to roll 
Player1 rolled a 2, and Player1 moves to 2 
Computer rolled a 6, and Computer moves to 6 

Player1: Hit enter to roll 
Player1 rolled a 6, and Player1 moves to 8 
Landed on a Snake and moving down to 2 
Computer rolled a 4, and Computer moves to 12 
Landed on a Ladder and moving up to 20 .... 
... 
Player1: Hit enter to roll 
Player1 rolled a 6, and Player1 moves to 104 
Must land exactly on 100, staying where you are on 97 
Computer rolled a 4, and Computer moves to 100 
!!!! Computer won !!!!!! End of Game 
```

I hope you enjoy my game!

I hope you enjoy my program!
