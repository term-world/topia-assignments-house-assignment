[![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml)

# SUDDEN SURGE OF RESIDENTIAL RENTERS: LOCAL LANDLORD MAKES A MODEST MINT

> **The Reporter**
>
> 31 August 2022

`(Ix)` — For months now, the neighborhoods in the suburbs of `term-world` have been ghost towns. The once-bustling streets of communities like `Andra` and `Folivoria` have been host to little more than the occasional tumbleweed ever since local property owner **The Landlord** raised rent rates to untenable levels in an attempt to only bring the best and brightest (and wealthiest) to our fair `term-world`.

In our exclusive interview with **The Landlord**, it was revealed that his able assistant **The Intern** argued that even properties with rock-bottom rent rates bring in more bacon than abandoned abodes. So, in a move that could only be called "inspired," "obvious," or maybe even "capitalistically altruistic," **The Landlord** is slashing rates to less than a tenth of what they once were. That's right, you'll no longer need a six-figure income to call one of these fine houses with three-figure square footage yours.

Word must've gotten out; nearly fifty new tenants have applied to live in the six neighborhoods owned and maintained by **The Landlord**. Only time will tell what these wide-eyed tenants will bring to `term-world`. ...

## Overview

In this activity, we cover:

* basic `term-world` commands
* navigating using your "terminal"
* file management best practices
* executing Python files
* an introduction to using the `git` protocol
* an overview of the GitHub platform

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

takes us back to the folder we were just in. You can always tell where you are by looking at your `command prompt` -- the text before the blocky cursor that indicates where you're typing. The follwing prompt:

```
 user    server   location
|----| |--------| |
dluman@term-world:~$
```

tells us that we're, well, ourselves (for me, it's `dluman`) on the `term-world` server, at the `~` location (think of `~` as a shortcut to your _home_ directory (which is different from your _house_).

This takes some time to adjust to, getting moved in to your house will give you more than enough practice.

### Getting contents of your house

Right now, the house is pretty empty. The output of another command, `ls` will show you this. Like `cd`, `ls` is short for something. In this case: "list." Given that there's nothing there, it would be helpful to have _stuff_. 

If you've navigated away from your `house` folder, `cd` back to it. However, if you're there, we can populate your house with your things. They're currently stored on GitHub, the platform we use to do something called "versioning" our files. As with everything in our time in `term-world`, we'll get plenty more experience with the customs and protocols of living in our digital society.

```
TODO: POST ASSIGNMENT LINK
```

Once you've done that:

```
git pull
```

This will `pull` all of the content for your house into _your_ `house` folder from the mysterious, but generous, "cloud" of `term-world`.

### Map of the house

To assist with your wayfinding, all of the houses built in the various neighborhoods of `term-world` feature the same layout, depicted below.

```
 -----------      --------
|  KITCHEN  | -- | GARDEN |
 -----------      --------
       |
 -------------               ---------
| DINING-ROOM |             | BEDROOM |
 -------------               ---------
       |                     /    
 -------------      ---------      --------
| LIVING-ROOM | -- | HALLWAY | -- | OFFICE |
 -------------      ---------      --------
```

## `Evaluating house Content`

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

The GitHub platform is a place to store your work. So, it makes some sense that should be able to _clone_ (download) from it, and push back (upload) to it. Here, we'll learn this second part.

- [ ] `cd` to your `~` folder
- [ ] Locate the `house` folder and `cd` to it.

Once in this folder, we need to tell git that there have been changes.

- [ ] Type `git add -A` and press `Enter`
* This tells git to look through the _entire_ folder structure for new changes and "stage" them

- [ ] Type `git commit -m "{Commit message}"` to "label" the commit
* This is typically something like `git commit -m "Fixing a typo"` -- the message in quotes should be as descriptive as possible, while remaining somewhat short

- [ ] To send all changes to the server, type `git push
- [ ] At the prompt, input the password associated with the `SSH Key` you created earlier

Once the process finishes successfully, we're done!

## Backup policy reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.