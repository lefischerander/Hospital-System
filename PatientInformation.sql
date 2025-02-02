--- Returns all data relevant to the patient from the patients table
select p.subject_id, p.gender, p.anchor_age, p.firstname, p.surname, p.dod from patients AS p