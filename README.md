[![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml)

# SUDDEN SURGE OF RESIDENTIAL RENTERS: LOCAL LANDLORD MAKES A MODEST MINT

> **The Reporter**
>
> 31 August 2022

`(Andra)` — For months now, the neighborhoods in the suburbs of `term-world` have been ghost towns. The once-bustling streets of communities like `Andra` and `Folivoria` have been host to little more than the occasional tumbleweed ever since local property owner **The Landlord** raised rent rates to untenable levels in an attempt to only bring the best and brightest (and wealthiest) to our fair `term-world`.

In our exclusive interview with **The Landlord**, it was revealed that his able assistant **The Intern** argued that even properties with rock-bottom rent rates bring in more bacon than abandoned abodes. So, in a move that could only be called "inspired," "obvious," or maybe even "capitalistically altruistic," **The Landlord** is slashing rates to less than a tenth of what they once were. That's right, you'll no longer need a six-figure income to call one of these fine houses with three-figure square footage yours.

Word must've gotten out; nearly fifty new tenants have applied to live in the six neighborhoods owned and maintained by **The Landlord**. Only time will tell what these wide-eyed tenants will bring to `term-world`...

## Overview

In this activity, we cover:

* basic `term-world` commands
* navigating using your "terminal"
* file management best practices
* executing Python files
* an introduction to using the `git` protocol
* an overview of the GitHub platform

The requirements of this exercise center on your ability to find your way around your house, unpack some boxes, remembering where you put things you unpack. You'll solve a few small puzzles in order to complete your lease and verify that your house is outfitted and working correctly.

### SSH Keys

The activities for your first week in `term-world` all take place in your `house`. In order to access this material, you will first need to set up an `SSH` key. While we'll cover this in the opening days of class, here's a (long-ish) video detailing the process should you need a reminder later:

[![SSH Key video]( http://img.youtube.com/vi/qEPjUGQFmzQ/hqdefault.jpg)](https://www.youtube.com/watch?v=qEPjUGQFmzQ&list=PLsYZRXov75ZHSwWiCk0-jd1RcTuu_-zmD&index=1)

### Basic navigation

Once your SSH key is set up, you'll need to navigate to the `house` folder by running this command in your terminal window:

```
cd ~/house
```

`cd` is short for "change directory," a command which moves you around the terminal to the various physical locations of `term-world`. The above command takes you _forward_, though you can also go _backward_ by using two "dots" (`..`) after your `cd` command _instead_ of the name of the folder you want to go to. For example:

```
cd ..
```

takes us back to the folder we were just in. You can always tell where you are by looking at your `command prompt` -- the text before the blocky cursor that indicates where you're typing. The following prompt:

```
 user    server   location
|----| |--------| |
dluman@term-world:~$
```

tells us that we're, well, ourselves (for me, it's `dluman`) on the `term-world` server, at the `~` location (think of `~` as a shortcut to your _home_ directory, which is different from your _house_).

This takes some time to adjust to; getting moved in to your house will give you more than enough practice.

### Getting the contents of your `house`

Right now, the house is pretty empty. The output of another command, `ls` will show you this. Like `cd`, `ls` is short for something. In this case: "list." Given that there's nothing there, it would be helpful to have _stuff_. Any time you want to _list_ a directory (i.e., see what's there) just type `ls` and press `Enter`.

If you've navigated away from your `house` folder, `cd` back to it. However, if you're there, we can populate your house with your things. They're currently stored on GitHub, the platform we use to do something called "versioning" our files. As with everything in our time in `term-world`, we'll get plenty more experience with the customs and protocols of living in our digital society.

Once you're in your `house folder`, locate the `Version Control` menu at the right side of your VS Code screen and locate the `Pull` option:

![VS Code source control menu](https://user-images.githubusercontent.com/1552764/213094317-4e2f580c-b70b-4a2c-b9b2-91d2eaa39fbe.png)

As with _every_ operation we do with GitHub, you'll need to provide the password for the `SSH` key we made earlier. This is a regular feature of our work; you'll get used to entering this password on a regular basis.

This will `pull` all of the content for your house into _your_ `house` folder from the mysterious, but generous, "cloud" of `term-world`.

### Map of the `house`

To assist with your wayfinding, all of the houses built in the various neighborhoods of `term-world` feature the same layout, depicted below.

```
 ----------- 
|  KITCHEN  | 
 ----------- 
       |
 -------------               ---------
| DINING-ROOM |             | BEDROOM |
 -------------               ---------
       |                     /    
 -------------      ---------      --------
| LIVING-ROOM | -- | HALLWAY | -- | OFFICE |
 -------------      ---------      --------
```

Each of these locations represent folders that you'll need to traverse in order to achieve the goals for this assignment. Notice that in several locations, "you can't get there from here," as the saying goes; in some occasions there are _dead ends_. You'll need to practice moving from folder to folder using both ["forward" and "backward"](#basic-navigation) directions.

### Unpacking a box

There are `5` boxes scattered throughout your house. Your job is to unpack them.

Each box is a Python file -- this is the language that we'll be using to conduct this course. They work, well, "out of the box," so there's no need to change or even look at any code. To open a box, let's say the `FragileBox.py` that's in the `kitchen`:

```
python FragileBox.py
```

`term-world` will narrate some of the story of the world and give you a choice of where to put the contents. You _can_ put items anywhere your house, but do you really need a `Couch.py` in the `kitchen`?

(Someone is reading this right now and thinking "Yeah, I _do_!")

### An important lesson about `term-world`

If there exists only one rule about `term-world`, it's that you can _use anything_ you have the permission to use. Given the lesson we learned about opening boxes above, the `python` command seems to make this happen for us. So, if you were to find a `Couch.py` somewhere in your house, it might be interesting to:

```
python Couch.py
``` 

Something equally curious _might_ happen.

## Evaluating `house` Content

Each week's repository is outfitted with a grader that can be used to evaluate your work for the week. In order to run the this grader for a given week's work, you'll need to first navigate to the "root" folder of the assignment (that is, the base folder containing a given assignment's work, such as `house` for this week):

```
cd ~/house
```

Once there you'll need to run the following command:

```
gatorgrade
```

Once the grader has finished running (it may take a couple minutes) you'll be presented with a series of checks that determine the overall "completeness" of your work. For instance, your output may look something like:

```
✔  Customize the nameplate (no TODOs)
✘  Find the Ink hidden in the couch
✘  Print the lease
✔  Enter the house
✘  Open the UltraHeavyBox
✘  Open the FragileBox
✘  Open the SinisterLookingBox
✘  Open the TubeShapedBox
✘  Open the BeatUpBox

-~-  FAILURES  -~-

✘  Find the Ink hidden in the couch
✘  Print the lease
✘  Open the UltraHeavyBox
✘  Open the FragileBox
✘  Open the SinisterLookingBox
✘  Open the TubeShapedBox
✘  Open the BeatUpBox

        Passed 2/9 (22%) of checks for user-house-solved! ┃

```

As you can tell, there are some checks which have been satisfied, though there are many which have not. Be sure to have *all* of the checks required for your desired grade completed by the due date!

## Submitting the assignment/saving progress

The GitHub platform is a place to store your work. So, it makes some sense that should be able to download from it, and push back (upload) to it. Here, we'll learn this second part.

Bottom line: we need to tell git that there have been changes.

* Observe the list of files you've changed and add them to a `staging` area using the `+` button to the right of each file
* Once these have been "staged," attach a message to what we call a `commit` -- a "packaging" of the files to send to GitHub
* To transmit this newly-assembled packaged, locate the `Commit & Push` option

The steps of the process are illustrated below.

![Staging, commiting and pushing using buttons described](https://user-images.githubusercontent.com/1552764/213094575-cdeca619-05f3-4da6-a641-0002a571d230.png)

### Note on your first time completing this process

It is nearly 100% likely that you will receive a prompt telling you to set your `git config` for `user.name` and/or `user.email`. Two commands in the terminal fix this. Replace the relevant information in the examples below:

```bash
git config --global user.name "YOUR GITHUB USERNAME"
git conifg --global user.email "YOUR ALLEGHENY EMAIL"
```

Then, retry the above process. Once the process finishes successfully, we're done! We can verify the results on GitHub.

## Backup policy reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
