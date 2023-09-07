# Project: 0x06. Regular expression

## Resources

#### Read or watch:

* [Regular expressions - basics](https://intranet.alxswe.com/rltoken/6VeaVMaugIxcFAwA27TBdQ)
* [Regular expressions - advanced](https://intranet.alxswe.com/rltoken/rntjh3-3S86zt0Qy28L10w)
* [Rubular is your best friend](https://intranet.alxswe.com/rltoken/RGkVuw1lZ_hoCCbLsiOAhg)
* [Use a regular expression against a problem: now you have 2 problems](https://intranet.alxswe.com/rltoken/Vwm8lpMUGa4x_FBtlyUQ8g)
* [Learn Regular Expressions with simple, interactive exercises](https://intranet.alxswe.com/rltoken/XsQ6rzS1uy-E6bnswUqIKg)
## Tasks

| Task | File |
| ---- | ---- |
| 0. Simply matching School | [0-simply_match_school.rb](./0-simply_match_school.rb) |
| 1. Repetition Token #0 | [1-repetition_token_0.rb](./1-repetition_token_0.rb) |
| 2. Repetition Token #1 | [2-repetition_token_1.rb](./2-repetition_token_1.rb) |
| 3. Repetition Token #2 | [3-repetition_token_2.rb](./3-repetition_token_2.rb) |
| 4. Repetition Token #3 | [4-repetition_token_3.rb](./4-repetition_token_3.rb) |
| 5. Not quite HBTN yet | [5-beginning_and_end.rb](./5-beginning_and_end.rb) |
| 6. Call me maybe | [6-phone_number.rb](./6-phone_number.rb) |
| 7. OMG WHY ARE YOU SHOUTING? | [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb) |



0. Simply matching School

Requirements:

The regular expression must match School
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$

1. Repetition Token #0

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

2. Repetition Token #1

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

3. Repetition Token #2

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

4. Repetition Token #3

Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Your regex should not contain square brackets

5. Not quite HBTN yet

Requirements:

The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:

sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$

6. Call me maybe

This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

Requirement:

The regular expression must match a 10 digit phone number
Example:

sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$

7. OMG WHY ARE YOU SHOUTING?

Requirement:

The regular expression must be only matching: capital letters
Example:

sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$


