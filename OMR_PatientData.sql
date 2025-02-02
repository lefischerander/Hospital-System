--- Returns most recent weight of patient 
--- Script can be changed to fetch Height or BMI values by replacing 'Weight%' with
--- 'Height%' or 'BMI%'
select top 1 * from omr
where subject_id = 10011398 and result_name like 'Weight%'
order by chartdate desc