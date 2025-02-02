--- Selects data (based on the patients subject_id) from diagnoses_icd and expands it 
--- with the icd_code description from d_icd_diagnoses
select d.subject_id, d.hadm_id, d.seq_num, d.icd_code, d.icd_version, id.long_title from diagnoses_icd AS d
inner join d_icd_diagnoses AS id ON d.icd_code = id.icd_code
where d.subject_id = 10035185
order by d.seq_num