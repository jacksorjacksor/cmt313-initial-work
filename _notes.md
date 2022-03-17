# Assessment view

Have a Green/Red light for right/wrong answers

REQUIREMENTS
So what does this actual need?
- This will PRIMARILY be for ONE student's details.
-- notable exception is for introduction of class ranking

- Student ID should come from LOGGED IN USER
-- While in dev can have a default "user_id==1"

FEATURES REQUIRED
- Course results view [ list view ]
-- Shows all modules so far
-- Shows predicted grade

- Module results view [ list view ]
-- Shows questions and gives breakdown of average/total score so far
-- Should be able to click on an Assessment to go to an Assessment view

- Assessment results view [ list view ]
-- Shows questions and gives breakdown of average/total score so far
-- Should be able to click on a Question to get a Question view


- Question view [ detail view ]
-- Unsure on what this would show but worth considering.

DETAILS REQUIRED
- Assessment results view [ list view ]
-- Calculated fields:

--# PRIMARY
--- Marks achieved
--- Marks possible

--# SECONDARY
--- Answers submitted
--- Answers possible
---- If questions have categories then could have a category breakdown

----- FUNCTIONALITY: 
must be able to export all data as .csv

