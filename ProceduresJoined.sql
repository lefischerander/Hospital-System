--- Selects data (based on the patients subject_id) from procedures_icd and extends it 
--- with the icd_code's description from d_icd_procedures
select p.subject_id, p.hadm_id, p.seq_num, p.chartdate, p.icd_code, p.icd_version, dp.long_title from procedures_icd AS p
inner join d_icd_procedures AS dp ON p.icd_code = dp.icd_code
where p.subject_id = 10035185
order by p.seq_num