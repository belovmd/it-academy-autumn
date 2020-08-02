## Homework2 review

### Homework2 evaluation
- Maximum score is +10 minimum is 0.
- Completed tasks 1, 3-5 are scored as +5.
- Completed tasks 6, 7 are scored as +1.
- 3+ completed **elementary** tasks from external sites scored up to +1.
- 2+ completed **advanced** tasks from external sites scored up to +2.
- +1 is my reserve for styling, namings, etc. 
- You don't need to make elementary tasks if you have advanced. In such case
they would be scored up to +3.
- PR that doesn't pass any of PR checklist checks takes -0,5.
- PR that doesn't pass any 2 of PR checklist checks takes -3.
- If external sites tasks doesn't contain full description they would not be
 checked (and would not be scored).
- All review comments should be addressed. Missed comments causes score 
penalties.

### PR checklist
Please make sure you've passed PR checklist
- [ ] my PR passes CI checks (flake8 and pycodestyle)
- [ ] my PR named according guidelines: `Homework2: Name Surname`
- [ ] my PR contains complete tasks descriptions for all tasks
- [ ] my PR made from fork feature brunch to maxim master branch.
- [ ] my PR don't contain only code that solves Homework2 tasks.
Redundant files (configs, etc. ) are put to .gitignore


### Review notes:
####Styling
1. Failed checklist item (PR name)
2. Missed tasks descriptions.
3. Other HW code in PR
4. Please don't remove `__init__.py` file.
5. Please don't put your code to `__init__.py` file.
6. Redundant comments in task 
7. Please divide tasks with two blank lines if you're doing them in one file
8. Failed CI checks
9. Missed tasks
10. Task 1. Can we use % operator instead of while? 
11. Task 1. This task has one-line solution. It looks too complex.
12. Task 2. Punctuation marks are: `,?.;:{)}['"` and some more.
13. Task 3. Redundant check for !=''.
14. Task 4. Why do we need to copy this string. More of that why do we do it 
with symbols iteration.
15. Task 4. We can just use `if 'a' < char < 'z'` or `char.islower()` function.
same for upper chars.
16. Task 5. There is one-line solution w/o temporary variable for creating next
fibonacci number.
17. Task 6. there is more simple solution (w/o number of digits count).
18. You can add some advanced tasks to improve your scores (take a look at
 evaluation section
 
19. You can add some novice tasks to improve your scores (take a look at 
evaluation section)