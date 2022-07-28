# WagonGame

<h1>Hey lovers, </h1><br>
Here is a new game that I made. Finally finished!<br>
Now, what is it? <br>
See, its a game about a train departing from the warehouse. You job is it to to load each wagon of its maximum hold. <br>
As much as each wagon holds. <b>Behold!</b> Don't be stupid! <br>
You cannot load as much as you want. Each wagon has a maximum weight limit. That of course: <b> You don't know it!</b>
So buckle so seat and guess right! Because if you overweight something, you crash. And its <i>Game over<i>
<p> Of course there are indicators that help you with it, currently I am missing the right symbols to show it but I make here a short one: </p>
<ul style="background-color: blue; color: green">
<li>	front_train = "<[''']>" = start </li>
<li>		wagon_empty = "<|___|>" = empty wagon (0-100)</li>
<li>		wagon_half = "<|---|>" = half full (499-400)</li>
<li>		wagon_full = "<|===|>" = full wagon (800-999) </li>
<li>		wagon_20 = "<|__-|>" = 20% taken (100-199) </li>
<li>		wagon_40 = "<|_--|>" 40% taken (200-399) </li>
<li>		wagon_60 = "<|--=|>"  60% taken (500-599) </li>
<li>		wagon_80 = "<|-==|>"  80% taken (600-799)</li>
<li>		wagon_smashed = "<|###|>" wagon overweighted!</li>
</ul>

You start with the first wagon, choose a certain weight you want to insert. As a result you'll get the train shown and how much you put in.<br>
Now, you are asked again, if you want to enter another weight, press y or Y for yes and n or N for not <br>
Afterwards, you will receive to the next wagon. <br>
As long as you not put to much weight as the wagon can hold. If so, you crash and the game stops. Showing you nice results <br>
You may enter your score at the board table! Currently its just an empty database (except one score, maybe). <br>
I will hopelly make an open score table, so you can have fun with others. 
<br>
Goal: Get the most wagons done and maximal weight you can enter! There is no finish, just go until you crash!
<br>
Lost: Never, everyone is a finisher!
<br>
<br>

<b>Note:</b> This is a terminal game! That only will work currently with python!!! No website or other languages. Sorry! <br>
<br>
<br>
<b>How to install:</b><br>
1. Go and download repository.
2. Open VS Code and install python
3. Run the program through the terminal by typing <i>python game.py</i>
   Make sure you in the location!
4. Have Fun!!!
