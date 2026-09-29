# lab04--Team_TEAM-

Group Name: TEAM

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Kaung Thant | kaungthant79 | conftest.py, test_shared.py |
| NayShinThant | Gzilla-ST | test_deposit.py |
| Phyo Thura Chit | Kpthura | test_teardown.py |
| Hein Lwin Oo | Bruce-Oo | test_withdraw.py |

## Our Merge Conflict

When we all edited the Who Did What table at the same time, Git showed this conflict for Hein Lwin Oo:

```
<<<<<<< HEAD
## Who did what

| Member | GitHub Username | File |
|---|---|---|
| Hein Lwin Oo | Bruce-Oo | test_withdrawal.py
=======
## Who Did What
|Member|GitHub Username|File|
|---|---|---|
| Kaung Thant | kaungthant79 | conftest.py |
|NayShinThant|Gzilla-ST|test_deposit.py|
| Phyo Thura Chit | Kpthura | test_teardown.py |
>>>>>>> c2bcc4b88adae6409275aedbba60821de10b4629
```

**What we kept:** We kept all four members' rows, because each row belongs to a different person. We used the "Who Did What" heading, formatted the table consistently, fixed the file name to `test_withdraw.py`, and deleted all the conflict markers.

**Why Git could not resolve it automatically:** Hein Lwin Oo's local commit and the commits already on GitHub changed the same lines of README.md (the heading and the table rows) in different ways. Git cannot know which version is correct or whether both should be kept, so it stopped and asked us to decide.
## Other Problems We Encountered

### VS Code "Failed to save README.md" Error

What happened:
While editing README.md in VS Code, we ran `git pull`, which updated README.md on disk with teammates' changes. When we tried to save, VS Code showed:

> Failed to save 'README.md': The content of the file is newer. Please compare your version with the file contents or overwrite the content of the file with your changes.

What we learned:
Always save the file (Ctrl+S or Cmd+S) before running `git add`, and check that `git commit` says `1 file changed`. Saving a file is not the same as committing it, and an unsaved file is not seen by Git at all.

## Git Contribution Summary

     7  Kpthura
     5  Shine
     4  Bruce-Oo
     3  Kaung Thant
     2  Gzilla-ST
     2  Min Thein Kyaw

## Reflection Questions

1. Why was your push rejected, and how did you fix it?
Our push was rejected because a teammate had already pushed to GitHub, so the remote had commits our local copy did not have. We fixed it by running `git pull` to merge their changes, then `git push`.

2. Why could Git not resolve the README conflict automatically?
Two members changed the same lines of README.md in different commits, so Git could not decide which version to keep. A person had to choose the final content.

3. What is the difference between committing and pushing?
Committing saves a snapshot of our changes in our local repository only. Pushing uploads those commits to GitHub so teammates can see them.

4. How do fixtures reduce duplicated setup code in tests?
A fixture creates the test setup once, for example `BankAccount(100)`, and each test receives it as a parameter. This means we don't repeat the same setup code in every test.