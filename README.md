# `SUDDEN SURGE OF RESIDENTIAL RENTERS: LOCAL LANDLORD MAKES A MODEST MINT`

*Reported by `The Reporter` from `Andra`, on 31 August, 2022.*

For months now the neighborhoods in the suburbs of `term-world` have been ghost towns. The once-bustling streets of communities like `Andra` and `Folivoria` have been host to little more than the occasional tumbleweed ever since local property owner `The Landlord` raised rent rates to untenable levels in an attempt to only bring the best and brightest (and wealthiest) to our fair `term-world`.

In our exclusive interview with `The Landlord`, he revealed that his able assistant `The Intern` argued that even properties with rock-bottom rent rates bring in more bacon than abandoned abodes. So, in a move that could only be called "inspired", "obvious", or maybe even "capitalistically altruistic", `The Landlord` is slashing rates to less than a tenth of what they once were. That's right, you'll no longer need a six-figure income to call one of these fine houses with three-figure square footage yours.

Word must've gotten out; nearly fifty new tenants have applied to live in the six neighborhoods owned and maintained by `The Landlord`. Only time will tell what these wide-eyed tenants will bring to `term-world`...

## `house Due Date`

**All content for the `house` is due at 11:59pm on Saturday, September 3rd, 2022.**

## `Accessing house Content`

The activities for your first week in `term-world` all take place in your `house`. In order to access this material, you will first need to have an SSH key set up (we'll cover this the first day of class, but below is a video for your convenience as well).

[![SSH Key video]( http://img.youtube.com/vi/qEPjUGQFmzQ/hqdefault.jpg)](https://www.youtube.com/watch?v=qEPjUGQFmzQ&list=PLsYZRXov75ZHSwWiCk0-jd1RcTuu_-zmD&index=1)

Once your SSH key is set up, you'll need to navigate to the `house` folder by running this command in your terminal window:

```
cd ~/house
```

Once there you'll need to `pull` the repository data using the following command:

```
git pull
```

This will `pull` all of the content for Week 0 into your `house` folder.

## `Evaluating house Content`

Each week's repository will be outfitted with a `grader` that can be used to evaluate your work for the week.

In order to run the `grader` for this week's work, you'll need to first navigate to the `house` folder:

```
cd ~/house
```

Once there you'll need to run the following command:

```
gatorgrade
```

Once the `grader` has finished running (it may take a couple minutes) you'll be presented with a series of checks that determine the overall "completeness" of your work. For instance, your output may look something like:

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
   → The command returned the error code 2
✘  Print the lease
   → The command returned the error code 2
✘  Open the UltraHeavyBox
   → Found 1 line(s) in the file or the output
✘  Open the FragileBox
   → Found 1 line(s) in the file or the output
✘  Open the SinisterLookingBox
   → Found 1 line(s) in the file or the output
✘  Open the TubeShapedBox
   → Found 1 line(s) in the file or the output
✘  Open the BeatUpBox
   → Found 1 line(s) in the file or the output

        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Passed 2/9 (22%) of checks for user-house-solved! ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

Be sure to have *all* of the checks required for your desired grade completed by the due date!

## `Submitting house Content`

The GitHub platform is a place to store your work. In the same way that you can `pull` content from a repository stored on GitHub (to get any changes to the repository into your local workspace), you can also `push` changes that you've made in your workspace to the repository stored on GitHub. In order to `push` however, you'll need to first `add` and `commit` changes to the repository.

For all of the steps in question, you'll need to be in the `root` (or uppermost) folder of the repository in question. For Week 0, this is the folder labeled `house`. To navigate to the `house` folder:

```
cd ~/house
```


Once in this folder, we need to tell `git` that there have been changes. Run the command:

```
git add -A
```

This command tells `git` to look through the *entire* folder--including all of the folders contained within that folder, such as the `living-room` and other sections of the `house`--and look for any changes that have been made to the contents of those folders. These changes are then "staged", and ready to be "committed". (The `-A` part is what's telling `git` to look through the entire folder, in case you were curious.)

In order to now commit your work, run the command:

```
git commit -m "DESCRIPTIVE COMMIT LABEL"
```

Here, replace the contents inside the double quote marks with a "label" for the types of changes you are committing to the repository. For instance, if you added your name to the `nameplate` file, you might run the command:

```
git commit -m "Add name to nameplate"
```

...or something to that effect. (These labels will form a "commit history", which can allow you to easily review the changes made to the repository over time...assuming your labels aptly and concisely describe each commit's contents.)

Finally, all these changes need to be actually *sent* to GitHub. In order to do this, we `push` them by running the following command:

```
git push
```

You'll be prompted to enter the password associated with your SSH key. Recall that while typing this password, you won't actually see any characters on-screen for security purposes.

It might seem like a lot at first, but within a few weeks most of this will feel automatic! Just remember to frequently `add`, `commit`, and `push` your work, simply because...

## `term-world Server Backup Policy`

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e., weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.