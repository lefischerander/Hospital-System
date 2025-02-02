--- Inserts a new diagnose into diagnoses_icd for a specific patient
--- Uses the newest hadm_id from the admissions table to check for the current hospital visit
--- seq_num needs to be adjusted in Python directly: Fetch the newest seq_num for the current hospital visit 
--- and +1 it. If no records are returned seq_num is 1.
insert into diagnoses_icd
select 10035185, hadm_id, 13, 2761, 9
from admissions
where subject_id = 10035185
order by hadm_id desc